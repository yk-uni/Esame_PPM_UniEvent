from django.db import models
from django.conf import settings


class Event(models.Model):

    title = models.CharField(max_length=200)

    description = models.TextField()

    date = models.DateTimeField()

    location = models.CharField(max_length=200)

    organizer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title
    
    @property
    def participants_count(self):
        return self.registration_set.count()


class Registration(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:

        unique_together = ('user', 'event')

    def __str__(self):
        return f"{self.user.username} -> {self.event.title}"