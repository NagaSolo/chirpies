from django.db import models

from django.utils import timezone
from django.contrib.auth.models import User

from django.urls import reverse

class Chirp(models.Model):
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.id

    def get_absolute_url(self):
        return reverse('chirp-detail', kwargs={ 'pk' : self.pk }) # return full path to view as a string