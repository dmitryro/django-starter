from oauth2_provider.models import get_access_token_model
from rest_framework.authentication import TokenAuthentication
from rest_framework import exceptions

class BearerTokenAuthentication(TokenAuthentication):
    keyword = u"Bearer"
