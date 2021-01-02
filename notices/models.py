from django.db import models
from django.utils import Timezone
from django.contrib.auth.models import User


# Create your models here.

class notice(models.Model):
    title = models.CharField(max_length=100)
    short_description = models.CharField(max_length=100)
    long_description = models.TextField()
    duration = models.DecimalField(max_digits=4, decimal_places=2)
    event_date_time = models.DateTimeField(
        default=timezone.now,
        verbose_name="Expecting Date and Time"
    )
    event_location_postcode = models.CharField(max_length=10)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # accepted =
    # accepted_by =
    date_posted = models.DateTimeField(default)





