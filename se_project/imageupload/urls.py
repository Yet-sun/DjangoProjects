from django.urls import path
from imageupload import views
from .views import UserManageSet # , UserViewSet
from rest_framework import routers
from imageupload import views


router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)
router.register(r'user_manage', UserManageSet),
