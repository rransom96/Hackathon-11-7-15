from django.contrib import admin
from hackathon_app.models import Issue, Post, Comment, PostUpvote, CommentUpvote, SubIssue, SubComment


# Register your models here.
@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'creation_date_time')


@admin.register(SubIssue)
class SubIssueAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'creation_date_time')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
    'user', 'subissue_rel', 'title', 'description', 'creation_time', 'modification_time', 'is_recent',
    'num_upvotes')



@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment_text', 'user', 'created_time', 'modified_time')


@admin.register(SubComment)
class SubCommentAdmin(admin.ModelAdmin):
    list_display = ('comment_text', 'user', 'created_time', 'modified_time')


@admin.register(PostUpvote)
class PostUpvoteAdmin(admin.ModelAdmin):
    list_display = ('post_upvotes', 'up_or_down', 'created_time')


@admin.register(CommentUpvote)
class CommentUpvoteAdmin(admin.ModelAdmin):
    list_display = ('comment_upvotes', 'up_or_down', 'created_time')


