import datetime
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Issue(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length= 255, default='empty')
    creation_date_time = models.DateField(auto_now_add=True)

    @property
    def all_sub_issues(self):
        return self.subissue_set.all()

    def __str__(self):
        return self.name


class SubIssue(models.Model):
    name = models.CharField(max_length=255,null=True,blank=True)
    description = models.CharField(max_length= 255, null=True,blank=True)
    creation_date_time = models.DateField(auto_now_add=True,null=True,blank=True)
    issue_rel = models.ForeignKey(Issue, default=1)

    @property
    def all_posts(self):
        return self.post_set.all()

    def __str__(self):
        return self.name


class Post(models.Model):
    user = models.ForeignKey(User, null=True, blank=True)
    title = models.CharField(max_length= 255)
    description = models.CharField(max_length= 255, default='empty')
    creation_time = models.DateTimeField(auto_now_add=True)
    modification_time = models.DateTimeField(auto_now=True)
    subissue_rel = models.ForeignKey(SubIssue, default=1)

    @property
    def all_comments(self):
        return self.comment_set.all()

    @property
    def all_sub_comments(self):
        return self.comment_set.all().subcomment_set.all()


    def is_recent(self):
        return timezone.now() - datetime.timedelta(days=1) <= self.creation_time

    def num_upvotes(self):
        return self.postupvote_set.all().count()


    def __str__(self):
        return "Title:{}".format(self.title)

class Comment(models.Model):
    user = models.ForeignKey(User)
    comment_text = models.CharField(max_length= 255, default='empty')
    post_rel = models.ForeignKey(Post)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    @property
    def all_sub_comments(self):
        return self.subcomment_set.all()

    def __str__(self):
        return "comment_text: {}".format(self.comment_text)

class SubComment(models.Model):
    user = models.ForeignKey(User)
    comment_text = models.CharField(max_length= 255, default='empty')
    comment_rel = models.ForeignKey(Comment)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "comment_text: {}".format(self.comment_text)

class PostUpvote(models.Model):
    post_upvotes = models.ForeignKey(Post)
    up_or_down = models.BooleanField()
    created_time = models.DateTimeField(auto_now_add=True)

class CommentUpvote(models.Model):
    comment_upvotes = models.ForeignKey(Comment)
    up_or_down = models.BooleanField()
    created_time = models.DateTimeField(auto_now_add=True)








