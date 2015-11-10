import datetime
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Issue(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length= 255, default='empty')
    creation_date_time = models.DateField(auto_now_add=True)


    def all_posts(self):
        return self.post_set.all()


    def current_count(self):
        self.post_set.all().count()

    def today_count(self):
        return self.post_set.filter(creation_date_time__gte=(timezone.now() - datetime.timedelta(days=1))).count()

    def daily_average(self):
        total_posts = self.post_set.all().count
        post_last_seven = total_posts.filter(creation_date_time__gte=(timezone.now() - datetime.timedelta(days=7)))
        average_last_seven = post_last_seven/7
        average_last_seven = round(average_last_seven, 1)
        return average_last_seven


    def __str__(self):
        return self.name


class Post(models.Model):
    user = models.ForeignKey(User, null=True, blank=True)
    title = models.CharField(max_length= 255)
    description = models.CharField(max_length= 255, default='empty')
    url = models.URLField(blank=True, null=True)
    slug = models.SlugField()
    creation_time = models.DateTimeField(auto_now_add=True)
    modification_time = models.DateTimeField(auto_now=True)
    issue_rel = models.ForeignKey(Issue, default=1)


    def is_recent(self):
        return timezone.now() - datetime.timedelta(days=1) <= self.creation_time

    def is_hot(self):
        if timezone.now() - datetime.timedelta(hours=3) <= self.comment_set.created_time:
            return True
        else:
            return False

    def num_upvotes(self):
        return self.postupvote_set.all().count()

    def karma(self):
        upvotes = self.postupvote_set.filter(up_or_down = True).count()
        downvotes = self.postupvote_set.filter(up_or_down = False).count()
        karma = upvotes - downvotes
        return karma

    def __str__(self):
        return "Title:{}".format(self.title)

class Comment(models.Model):
    user = models.ForeignKey(User)
    comment_text = models.CharField(max_length= 255, default='empty')
    post_rel = models.ForeignKey(Post)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "User:{}, comment_text: {}, post_rel: {}, created_time: {}, last_modified".format(self.user,
                                                                                    self.comment_text, self.post_rel,
                                                                                    self.created_time,
                                                                                    self.modified_time)

class PostUpvote(models.Model):
    post_upvotes = models.ForeignKey(Post)
    up_or_down = models.BooleanField()
    created_time = models.DateTimeField(auto_now_add=True)

class CommentUpvote(models.Model):
    comment_upvotes = models.ForeignKey(Comment)
    up_or_down = models.BooleanField()
    created_time = models.DateTimeField(auto_now_add=True)








