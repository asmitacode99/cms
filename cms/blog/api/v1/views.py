from rest_framework.generics import (RetrieveUpdateDestroyAPIView, ListAPIView, ListCreateAPIView)
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from cms.blog.models import Post, Category, Tag, Comment, Bookmark, LikeDislike, Notification
from .serializers import (PostSerializer, CategorySerializer, TagSerializer, CommentSerializer, BookmarkSerializer, LikeDislikeSerializer, NotificationSerializer)


# Post Views
class PostListAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostListCreateAPIView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'

    def get(self, request, *args, **kwargs):
        post = self.get_object()  # Get the specific post object
        post.view_count += 1  # Increment the view count
        post.save()  # Save the updated view count
        serializer = self.get_serializer(post)
        return Response(serializer.data)


# Category Views
class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryListCreateAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'


# Tag Views
class TagListAPIView(ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class TagListCreateAPIView(ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class TagRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    lookup_field = 'slug'


# Bookmark Views
class BookmarkListAPIView(ListAPIView):
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer

class BookmarkListCreateAPIView(ListCreateAPIView):
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer

class BookmarkRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer
    lookup_field = 'slug'


# LikeDislike Views
class LikeDislikeListAPIView(ListAPIView):
    queryset = LikeDislike.objects.all()
    serializer_class = LikeDislikeSerializer

class LikeDislikeListCreateAPIView(ListCreateAPIView):
    queryset = LikeDislike.objects.all()
    serializer_class = LikeDislikeSerializer

class LikeDislikeRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = LikeDislike.objects.all()
    serializer_class = LikeDislikeSerializer
    lookup_field = 'slug'


# Comment Views
class CommentListAPIView(ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentListCreateAPIView(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = 'slug'


# Notification View
class NotificationListAPIView(ListAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
  
class NotificationListCreateAPIView(ListCreateAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

class NotificationRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    lookup_field = 'slug'

    @action(detail=True, methods=['post'])
    def mark_as_read(self, request, *args, **kwargs):
        notification = self.get_object()
        notification.is_read = True
        notification.save()
        return Response({'status': 'Notification marked as read'}, status=status.HTTP_200_OK)
