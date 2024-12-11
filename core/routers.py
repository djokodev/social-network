from rest_framework import routers
from core.user.viewsets import UserViewset
from core.auth.viewsets.register import RegisterViewSet
from core.auth.viewsets.login import LoginViewSet


router = routers.SimpleRouter()
router.register(r'user', UserViewset, basename='user')
router.register(r'auth/register', RegisterViewSet, basename='auth-register')
router.register(r'auth/login', LoginViewSet, basename='auth-login')

urlpatterns = [
    *router.urls,
]