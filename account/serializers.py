from django.core.exceptions import ValidationError
from rest_framework import serializers
from .models import Account


class RegistrationSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = Account
        fields = ['email', 'username', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        account = Account(
            email=self.validated_data['email'],
            username=self.validated_data['username']
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError(
                {'password': 'Passwords must match.'})
        account.set_password(password)
        account.save()
        return account


class AccountSerializer(serializers.ModelSerializer):

    image = serializers.SerializerMethodField('get_profile_image')

    class Meta:
        model = Account
        fields = ['email', 'username', 'id',  'image']

    def get_profile_image(self, profile):
        image = profile.profile.image.url
        return image
