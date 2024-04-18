from rest_framework.routers import DefaultRouter
from post.api.views import *

router = DefaultRouter()
router.register(r'post', PostViewSet, basename='post')
router.register(r'category', CategoryViewSet, basename='category')
router.register(r'tag', TagViewSet, basename='tag')
router.register(r'comment', CommentViewSet, basename='comment')
urlpatterns = router.urls