from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User)
    age = models.IntegerField()
    gender = models.CharField(max_length=8)

    # Link karma for the user
    # Comment karma for the user
    # Average up-votes
    # Average down-votes
    # Total counts for comments and links

    def post_karma(self):
        k = self.user.post_set.karma().all()
        return k

    def comment_karma(self):
        pass

    def average_upvotes(self):
        pass

    def average_downvotes(self):
        pass

    def total_upvotes(self):
        pass

    def __str__(self):
        return "{} Age: {} Gender: {}".format(self.user.username, self.age, self.gender)


