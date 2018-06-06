from django.db import models


class Books(models.Model):
    name = models.CharField(max_length=120)
    author = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
