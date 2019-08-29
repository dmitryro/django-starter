from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    uuid = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    author = models.CharField(max_length=200, blank=True, null=True)
    aspect_ratio = models.FloatField(blank=True, default=0.0)
    duration = models.FloatField(blank=True, default=0.0)
    source = models.CharField(max_length=1200, blank=True, null=True)
    extension = models.CharField(max_length=200, blank=True, null=True)
    time_published = models.DateTimeField(auto_now_add=True)
    time_created = models.DateTimeField(blank=True, null=True)
    meta = models.CharField(max_length=1500, blank=True, null=True)

    class Meta:
        verbose_name = 'Video'
        verbose_name_plural = 'Videos'


    def __str__(self):
        return self.title
 
