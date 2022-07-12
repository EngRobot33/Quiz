from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=True, write_only=True)
    confirm_password = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'confirm_password', 'first_name', 'last_name',)

    @staticmethod
    def clean_validated_data(validated_data):
        validated_data.pop('confirm_password')
        return validated_data

    def validate(self, attrs):
        validate_password(attrs.get('password'))

        if attrs.get('password') != attrs.get('confirm_password'):
            raise serializers.ValidationError('password and confirm password are not equal!')

        return attrs

    def create(self, validated_data):
        user = self.Meta.model.objects.create_user(**self.clean_validated_data(validated_data))
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'avatar')


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'avatar')


class UserChangePasswordSerializer(serializers.ModelSerializer):
    old_password = serializers.CharField(required=True, write_only=True)
    new_password = serializers.CharField(required=True, write_only=True)
    confirm_password = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = User
        fields = ('old_password', 'new_password', 'confirm_password',)


    def validate(self, attrs):
        password_validation(attrs.get('new_password'))

        if attrs.get('new_password') != attrs.get('confirm_password'):
            raise serializers.ValidationError("New password and Confirmation password are not equal!")

        return attrs


    def update(self, instance, validated_data):
        if instance.check_passowrd(validated_data.get('old_password')):
            instance.set_password(validated_data.get('new_password'))
            instance.save()

            return instance
        
        else:
            raise serializers.ValidationError("Old password is not correct!")