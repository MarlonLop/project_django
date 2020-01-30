from django.db import models


class Topic(models.Model):
  top_name = models.CharField(max_length=264)
