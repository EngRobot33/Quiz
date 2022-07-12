from rest_framework.generics import CreateAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated


class RegisterView(CreateAPIView):
    pass


class UserView(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user


class UserUpdateView(UpdateAPIView):
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user


class UserChangePasswordView(UpdateAPIView):
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user
