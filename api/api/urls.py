"""demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from api.video import views
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_swagger.views import get_swagger_view
from rest_framework_swagger.renderers import OpenAPIRenderer, SwaggerUIRenderer
from rest_framework.schemas import get_schema_view
from api.video.views import VideoList, VideoARList, VideoRecordsView
from api.video.views import CustomAuthToken

schema_view = get_swagger_view(title='Pastebin API')



urlpatterns = [
    path('index/', views.index),
    path('admin/', admin.site.urls),
    path('openapi', get_schema_view(
        title="Your Project",
        description="API for all things …"
    ), name='openapi-schema'),
    path('swagger-ui/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='swagger-ui'),
    path('redoc/', TemplateView.as_view(
        template_name='redoc.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='redoc'),
    path('uuids/<str:uuid>/', VideoList.as_view()),
    path('aspects/<str:aspect_ratio>/', VideoARList.as_view()),
    path('videos/', VideoRecordsView.as_view()),
    path('docapi', schema_view),
    path('api-token-auth/', CustomAuthToken.as_view()),
]
