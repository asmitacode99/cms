from django.contrib import admin
from cms.blog.models import Post, Category, Tag, Bookmark, Comment, LikeDislike, Notification


# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'slug', 'name',)  
    search_fields = ('name',)  
    ordering = ('name',) 

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'slug', 'name',)  
    search_fields = ('name',)  
    ordering = ('name',) 

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1
    fields = ['user', 'comment']


class BookmarkInline(admin.TabularInline):
    model = Bookmark
    extra = 0
    fields = ['user',]
    

class LikeDislikeInline(admin.TabularInline):
    model = LikeDislike
    extra = 0
    fields = ['user',]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'slug', 'title', 'author', 'publish_date', 'comment_count', 'bookmark_count', 'like_count', 'dislike_count', 'view_count']
    search_fields = ['title', 'author__username']
    inlines = [CommentInline, BookmarkInline, LikeDislikeInline]


@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ['id', 'slug', 'user', 'post']
    search_fields = ['user__username', 'post__title']
   

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'slug', 'user', 'post', 'comment', 'is_approved']
    search_fields = ['user__username', 'post__title', 'comment']

@admin.register(LikeDislike)
class LikeDislikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'slug', 'post', 'user', 'choice')
    search_fields = ('post__title', 'user__username')
    list_filter = ('choice',)
    
@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('id', 'slug', 'user', 'notification_type', 'related_post', 'related_comment', 'is_read')   
    search_fields = ('message', 'user__username', 'notification_type')
    list_filter = ('is_read', 'notification_type')
        