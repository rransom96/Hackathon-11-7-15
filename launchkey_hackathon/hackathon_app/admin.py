from django.contrib import admin
from hackathon_app.models import Issue, Post, Comment, PostUpvote, CommentUpvote


# Register your models here.
@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'creation_date_time')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
    'user', 'issue_rel', 'title', 'description', 'url', 'slug', 'creation_time', 'modification_time', 'is_recent',
    'num_upvotes', 'karma')
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment_text', 'user', 'created_time', 'modified_time')


@admin.register(PostUpvote)
class PostUpvoteAdmin(admin.ModelAdmin):
    list_display = ('post_upvotes', 'up_or_down', 'created_time')


@admin.register(CommentUpvote)
class CommentUpvoteAdmin(admin.ModelAdmin):
    list_display = ('comment_upvotes', 'up_or_down', 'created_time')


