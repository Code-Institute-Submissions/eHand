from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.

class Notice(models.Model):
    title = models.CharField(max_length=100)
    short_description = models.CharField(max_length=100)
    long_description = models.TextField()
    duration = models.DecimalField(
        max_digits=4, decimal_places=2,
        verbose_name="Duration / Time Payment"
    )
    event_date_time = models.DateTimeField(
        verbose_name="Event Date and Time"
    )
    event_location_postcode = models.CharField(max_length=10)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='author')
    accepted = models.BooleanField(default=False)
    accepted_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                    related_name='accepted_by', null=True, blank=True)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('notice-detail', kwargs={'pk': self.pk})
