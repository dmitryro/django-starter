from api.video.models import Video
from rest_framework import serializers


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ('id', 'uuid', 'title', 'author', 'description', 
                  'duration', 'source', 'extension', 'aspect_ratio', 
                  'time_published', 'time_created', 'meta')
