from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from cms.blog.models import Comment, Bookmark, LikeDislike, Notification


@receiver(post_save, sender=Comment)
@receiver(post_delete, sender=Comment)
def update_post_comment_count(sender, instance, **kwargs):
    post = instance.post
    if post.pk:  # Ensure the Post has been saved
        post.save()


@receiver(post_save, sender=Bookmark)
@receiver(post_delete, sender=Bookmark)
def update_post_bookmark_count(sender, instance, **kwargs):
    post = instance.post
    if post.pk:  # Ensure the Post has been saved
        post.save()


@receiver(post_save, sender=LikeDislike)
@receiver(post_delete, sender=LikeDislike)
def update_post_like_dislike_count(sender, instance, **kwargs):
    post = instance.post
    if post.pk:  # Ensure the Post has been saved
        post.save()


@receiver(post_save, sender=LikeDislike)
def create_like_dislike_notification(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(
            user=instance.post.author,  # Notify the post author
            message=f"Your post '{instance.post.title}' was {instance.choice}d by {instance.user.username}.",
            notification_type=instance.choice,
            related_post=instance.post
        )


@receiver(post_save, sender=Comment)
def create_comment_notification(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(
            user=instance.post.author,  # Notify the post author
            message=f"{instance.user.username} commented on your post '{instance.post.title}'.",
            notification_type='comment',
            related_post=instance.post,
            related_comment=instance
        )
        

@receiver(post_save, sender=Bookmark)
def create_bookmark_notification(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(
            user=instance.post.author,  # Notify the post author
            message=f"Your post '{instance.post.title}' was bookmarked by {instance.user.username}.",
            notification_type='bookmark',
            related_post=instance.post
        )
