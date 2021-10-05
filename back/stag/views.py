from rest_framework_simplejwt.views import TokenViewBase

from stag import serializers


class StagTokenObtainPairView(TokenViewBase):
    """
    Custom view based on rest_framework_simplejwt.views.TokenObtainPairView allowing use of our
    custom serializer
    Takes a set of user credentials and returns an access and refresh JSON web
    token pair to prove the authentication of those credentials.
    """
    serializer_class = serializers.StagTokenObtainPairSerializer
