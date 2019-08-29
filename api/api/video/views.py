from django.http import HttpResponse
from django.template import loader
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, pagination
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from api.video.serializers import VideoSerializer
from api.video.models import Video
from api.video.pagination import CustomPagination

def index(request):
    template = loader.get_template('api/index.html')
    return HttpResponse(template.render())

class VideoList(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = VideoSerializer

    def get_queryset(self):
        ""
        ""
        uuid = self.kwargs['uuid']
        return Video.objects.filter(uuid=uuid)


class VideoARList(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = VideoSerializer

    def get_queryset(self):
        ""
        ""
        aspect_ratio = float(self.kwargs['aspect_ratio'])
        return Video.objects.filter(aspect_ratio=aspect_ratio)


class VideoRecordsView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    pagination_class = CustomPagination


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):

        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })

