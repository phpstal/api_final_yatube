from django.urls import path, include
from django.urls import path
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView,)
from .views import PostViewSet, CommentViewSet

router_v1 = DefaultRouter()
router_v1.register('posts', PostViewSet)
#router_v1.register(
#    r'posts/(?P<post_id>\d+)/comments',
#    CommentViewSet,
#    basename='comments'
#)


urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),    
] 