# Generated by Django 5.0 on 2024-12-11 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_post', '0001_initial'),
        ('core_user', '0004_alter_user_created_alter_user_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='posts_liked',
            field=models.ManyToManyField(related_name='liked_by', to='core_post.post'),
        ),
    ]
