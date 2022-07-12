from rest_framework.generics import CreateAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated

from .serializers import UserSerializer, UserUpdateSerializer, UserChangePasswordSerializer, RegisterSerializer


class RegisterView(CreateAPIView):
    serializer_class = RegisterSerializer


class UserView(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class UserUpdateView(UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserUpdateSerializer

    def get_object(self):
        return self.request.user


class UserChangePasswordView(UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserChangePasswordSerializer

    def get_object(self):
        return self.request.user
