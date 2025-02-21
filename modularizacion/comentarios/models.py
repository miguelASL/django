from django.db import models


class comments(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    score = models.IntegerField(null=False, blank=False)
    comment = models.TextField(null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
