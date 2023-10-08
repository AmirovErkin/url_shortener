from django.db import models
import shortuuid


class URL(models.Model):
    original_url = models.URLField()
    shortened_url = models.CharField(max_length=10, unique=True)
    click_count = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.shortened_url:
            self.shortened_url = shortuuid.uuid()[:10]
        super().save(*args, **kwargs)

    def __str__(self):
        return self.original_url