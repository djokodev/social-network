from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from core.abstract.serializers import AbstractSerializer
from core.post.models import Post
from core.user.models import User


class PostSerializer(AbstractSerializer):
    liked = serializers.SerializerMethodField()
    likes_count = serializers.SerializerMethodField()

    author = serializers.SlugRelatedField(
        queryset=User.objects.all(), slug_field="public_id"
    )

    def validate_author(self, value):
        if self.context["request"].user != value:
            raise ValidationError("You can't create a post for another user.")
        return value

    def get_liked(self, instance):
        request = self.context.get("request", None)
        if request is None or request.user.is_anonymous:
            return False
        return request.user.has_liked(instance)

    def get_likes_count(self, instance):
        return instance.liked_by.count()

    class Meta:
        model = Post
        fields = [
            "id",
            "author",
            "body",
            "liked",
            "likes_count",
            "edited",
            "created",
            "updated",
        ]
        read_only_fields = ["edited"]
