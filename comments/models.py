from django.db import models
from django.contrib.auth.models import User
from notices.models import Notice


class Comment(models.Model):
    """ Model for comments """
    notice = models.ForeignKey(
        Notice, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['timestamp']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.user.username)
