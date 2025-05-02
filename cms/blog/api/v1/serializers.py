from rest_framework import serializers
from cms.blog.models import Category, Tag, Comment, Bookmark, Post, Notification, LikeDislike


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'slug', 'created', 'updated']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name', 'slug', 'created', 'updated']


class CommentSerializer(serializers.ModelSerializer):
    post_title = serializers.ReadOnlyField(source='post.title')  # Include post title

    class Meta:
        model = Comment
        fields = ['id', 'slug', 'user', 'post', 'post_title', 'comment', 'created', 'updated', 'is_approved']
        lookup_fields = ['user',]


class BookmarkSerializer(serializers.ModelSerializer):
    post_title = serializers.ReadOnlyField(source='post.title')  # Include post title

    class Meta:
        model = Bookmark
        fields = ['id', 'slug', 'user', 'post', 'post_title', 'created', 'updated']


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'id', 'author', 'title', 'slug', 'content', 'excerpt', 'featured_image',
            'categories', 'tags', 'status', 'publish_date', 'bookmark_count',
            'comment_count', 'like_count', 'dislike_count', 'view_count', 'comments', 'bookmarks',
            'created', 'updated',
        ]


class LikeDislikeSerializer(serializers.ModelSerializer):
    post_title = serializers.ReadOnlyField(source='post.title')  # Include post title

    class Meta:
        model = LikeDislike 
        fields = ['id', 'user', 'post', 'post_title', 'choice']


class NotificationSerializer(serializers.ModelSerializer):
    # Custom fields to include related data
    user = serializers.StringRelatedField()  # Display the username for the user
    related_post = serializers.StringRelatedField()  # Display the title of the related post
    related_comment = serializers.StringRelatedField()  # Display the text of the related comment

    class Meta:
        model = Notification
        fields = ['id', 'user', 'slug', 'message', 'is_read', 'notification_type', 'related_post', 'related_comment', 'created']

    def update(self, instance, validated_data):
        """Custom update method to mark notifications as read."""
        instance.is_read = validated_data.get('is_read', instance.is_read)
        instance.save()
        return instance
