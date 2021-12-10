from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import *
from .views.common import PostViewSet, SearchApiView, PostCreate
from .views.employee import ApplyPostApiView, AppliedPostsAPIView, already_applied_api_view

router = DefaultRouter()
router.register('posts', PostViewSet)

urlpatterns = [
    path('create/', PostCreate.as_view()),
    path('search/', SearchApiView.as_view()),
    path('apply-post/<int:post_id>', ApplyPostApiView.as_view()),
    path('applied-posts', AppliedPostsAPIView.as_view()),
    path('applied-for-post/<int:post_id>', already_applied_api_view),
]

urlpatterns += router.urls
