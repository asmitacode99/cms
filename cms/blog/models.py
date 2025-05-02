from django.db import models
from django.conf import settings
from cms.core.utils import generate_slug
from django_ckeditor_5.fields import CKEditor5Field  
from cms.core.models import BaseModel
# from django.urls import reverse


class Category(BaseModel):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='category_images/', null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug: 
            self.slug = generate_slug(self.name)
        super().save(*args, **kwargs)  


class Tag(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:  
            self.slug = generate_slug(self.name)
        super().save(*args, **kwargs)  


class Comment(BaseModel):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_comments')
    comment = models.TextField()
    is_approved = models.BooleanField(default=True)
   

    def __str__(self):
        return f"Comment by {self.user} on {self.post.title}"
    
    def save(self, *args, **kwargs):
        if not self.slug:  
            self.slug = generate_slug(self.user)
        super().save(*args, **kwargs)  



class Bookmark(BaseModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='bookmarked_posts')
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='bookmarks')

    class Meta:
        unique_together = ('user', 'post')

    def __str__(self):
        return f"Bookmark by {self.user} for {self.post.title}"
    
    def save(self, *args, **kwargs):
        if not self.slug:  
            self.slug = generate_slug(self.user)
        super().save(*args, **kwargs)  



class Post(BaseModel):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('archived', 'Archived'), 
    ]

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, related_name='blog_posts')
    title = models.CharField(max_length=255)
    content = CKEditor5Field('content', config_name='extends', null=True, blank=True)  
    excerpt = models.TextField(max_length=300, blank=True, help_text="Short summary for the blog post.")
    featured_image = models.ImageField(upload_to='blog_images/', null=True, blank=True)
    categories = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='blog_posts', null=True, blank=True)
    tags = models.ManyToManyField(Tag, related_name='blog_posts', blank=True) 
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    publish_date = models.DateTimeField(null=True, blank=True)
    bookmark_count = models.PositiveIntegerField(default=0)
    comment_count = models.PositiveIntegerField(default=0) 
    like_count = models.PositiveIntegerField(default=0)
    dislike_count = models.PositiveIntegerField(default=0)
    view_count = models.PositiveIntegerField(default=0) 


    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        is_new_instance = self.pk is None
        if not is_new_instance:
            self.comment_count = self.comments.filter(is_approved=True).count()
            self.bookmark_count = self.bookmarks.count()
            self.like_count = self.like_dislike.filter(choice=LikeDislike.LIKE).count()
            self.dislike_count = self.like_dislike.filter(choice=LikeDislike.DISLIKE).count()

        if not self.slug:
            self.slug = generate_slug(self.title)  

        super().save(*args, **kwargs)


class LikeDislike(BaseModel):
    LIKE = 'like'
    DISLIKE = 'dislike'
    CHOICE_TYPES = [
        (LIKE, 'Like'),
        (DISLIKE, 'Dislike'),
    ]
 
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='like_dislike')
    choice = models.CharField(max_length=7, choices=CHOICE_TYPES)

    class Meta:
        unique_together = ('user', 'post')  # Ensure each user can like or dislike a post only once

    def __str__(self):
        return f'{self.user} {self.choice}s {self.post.title}'   
     
    def save(self, *args, **kwargs):
        if not self.slug:  
            self.slug = generate_slug(self.user)
        super().save(*args, **kwargs)  
    


class Notification(BaseModel):
    NOTIFICATION_CHOICES = [
        ('like', 'Like'),
        ('dislike', 'Dislike'),
        ('comment', 'Comment'),
        ('bookmark', 'Bookmark'),
        ('general', 'General'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='notifications')
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    notification_type = models.CharField(max_length=10, choices=NOTIFICATION_CHOICES)
    related_post = models.ForeignKey('Post', on_delete=models.CASCADE, null=True, blank=True, related_name='notifications')
    related_comment = models.ForeignKey('Comment', on_delete=models.CASCADE, null=True, blank=True, related_name='notifications')

    def __str__(self):
        return f"Notification for {self.user.username} - {self.message[:50]}"
    
    def save(self, *args, **kwargs):
        if not self.slug:  
            self.slug = generate_slug(self.notification_type)
        super().save(*args, **kwargs)  

