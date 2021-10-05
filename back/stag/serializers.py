from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login


from rest_framework import exceptions, serializers

from rest_framework_simplejwt.settings import api_settings
from rest_framework_simplejwt.tokens import RefreshToken


class StagTokenObtainPairSerializer(serializers.Serializer):
    """
    Custom serializer based on `rest_framework_simplejwt.serializers.TokenObtainPairSerializer` to
    allow authentication with just `first_name` and `last_name`, and to implement custom error
    strings
    """

    first_name = serializers.CharField()
    last_name = serializers.CharField()

    @classmethod
    def get_token(cls, user):
        return RefreshToken.for_user(user)

    def validate(self, attrs):
        """
        Perform authentication using the supplied `first_name` and `last_name`
        """
        data = {}

        authenticate_kwargs = {
            "first_name": attrs["first_name"],
            "last_name": attrs["last_name"],
            "password": None,
        }

        self.user = authenticate(**authenticate_kwargs)
        # If a vaid user isn't returned following authentication, raise error
        if not api_settings.USER_AUTHENTICATION_RULE(self.user):
            raise exceptions.AuthenticationFailed(
                self.error_messages["no_active_account"],
                "You are not known to this stag!",
            )

        refresh = self.get_token(self.user)

        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)

        if api_settings.UPDATE_LAST_LOGIN:
            update_last_login(None, self.user)

        return data
