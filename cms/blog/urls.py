from django.urls import path
from cms.blog.api.v1.views import (PostListAPIView, PostListCreateAPIView, PostRetrieveUpdateDestroyAPIView, CategoryListAPIView, CategoryListCreateAPIView, CategoryRetrieveUpdateDestroyAPIView, TagListAPIView, TagListCreateAPIView, TagRetrieveUpdateDestroyAPIView,
                                    CommentListAPIView,  CommentListCreateAPIView, CommentRetrieveUpdateDestroyAPIView,
                                    LikeDislikeListAPIView, LikeDislikeListCreateAPIView, LikeDislikeRetrieveUpdateDestroyAPIView, BookmarkListAPIView,
                                    BookmarkListCreateAPIView, BookmarkRetrieveUpdateDestroyAPIView, NotificationListAPIView, NotificationListCreateAPIView, NotificationRetrieveUpdateDestroyAPIView)

app_name = "blog"
urlpatterns = [
    # Post URLs
    path('post/', PostListAPIView.as_view(), name='post-list'),
    path('post/create/', PostListCreateAPIView.as_view(), name='post-create'),
    path('post/<slug:slug>/', PostRetrieveUpdateDestroyAPIView.as_view(), name='post-detail'),

    # Category URLs
    path('category/', CategoryListAPIView.as_view(), name='category-list'),
    path('category/create/', CategoryListCreateAPIView.as_view(), name='category-create'),
    path('category/<slug:slug>/', CategoryRetrieveUpdateDestroyAPIView.as_view(), name='category-detail'),

    # Tag URLs
    path('tag/', TagListAPIView.as_view(), name='tag-list'),
    path('tag/create/', TagListCreateAPIView.as_view(), name='tag-create'),
    path('tag/<slug:slug>/', TagRetrieveUpdateDestroyAPIView.as_view(), name='tag-detail'),

    # Comment URLs
    path('comment/', CommentListAPIView.as_view(), name='comment-list'),
    path('comment/create/', CommentListCreateAPIView.as_view(), name='comment-create'),
    path('comment/<slug:slug>/', CommentRetrieveUpdateDestroyAPIView.as_view(), name='comment-detail'),

    # Bookmark URLs
    path('bookmark/', BookmarkListAPIView.as_view(), name='bookmark-list'),
    path('bookmark/create/', BookmarkListCreateAPIView.as_view(), name='bookmark-create'),
    path('bookmark/<slug:slug>/', BookmarkRetrieveUpdateDestroyAPIView.as_view(), name='bookmark-detail'),

    # LikeDislike URLs
    path('like-dislike/', LikeDislikeListAPIView.as_view(), name='like-dislike-list'),
    path('like-dislike/create/', LikeDislikeListCreateAPIView.as_view(), name='like-dislike-create'),
    path('like-dislike/<slug:slug>/', LikeDislikeRetrieveUpdateDestroyAPIView.as_view(), name='like-dislike-detail'),
    
    # Notification URLs
    path('notification/', NotificationListAPIView.as_view(), name='notification-list'),
    path('notification/create/', NotificationListCreateAPIView.as_view(), name='notification-create'),
    path('notification/<slug:slug>/', NotificationRetrieveUpdateDestroyAPIView.as_view(), name='notification-detail'),


]
