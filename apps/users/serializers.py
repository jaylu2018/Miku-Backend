from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer


class MyTokenSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)
        data['token'] = data.pop('access')
        return data


class MyTokenRefreshSerializer(TokenRefreshSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        data['token'] = data.pop('access')
        return data
