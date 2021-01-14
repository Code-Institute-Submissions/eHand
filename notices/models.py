from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from operator import itemgetter


TIME_OPTIONS = {
    ('0hrs', 'Not Specified'),
    ('1hrs', '1 Hour'),
    ('2hrs', '2 Hours'),
    ('3hrs', '3 Hours'),
    ('4hrs', '4 Hours'),
    ('5hrs', '5 Hours'),
    ('6hrs', '6 Hours'),
    ('7hrs', '7 Hours'),
    ('8hrs', '8 Hours')
}


class Notice(models.Model):
    title = models.CharField(max_length=100)
    short_description = models.CharField(max_length=100)
    long_description = models.TextField()
    duration = models.CharField(max_length=10,
        choices=sorted(TIME_OPTIONS, key=itemgetter(0)),
        verbose_name="Duration / Time Payment"
    )
    event_date_time = models.DateTimeField(
        verbose_name="Event Date and Time"
    )
    event_location_postcode = models.CharField(max_length=10)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='author')
    commit = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='commit_to_help',
                               default=1)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('notice-detail', kwargs={'pk': self.pk})


class Commitments(models.Model):
    title = models.CharField(max_length=100)
    short_description = models.CharField(max_length=100)
    long_description = models.TextField()