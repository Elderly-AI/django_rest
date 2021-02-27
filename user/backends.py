import hashlib
from user.models import CustomUser


class AuthenticationBackend:

    def authenticate(self, request, username=None, password=None):
        username = self.__get_username(username, password)
        try:
            user = CustomUser.objects.get(username=username)
            return user
        except CustomUser.DoesNotExist:
            return None

    def get_user(self, user_id):
        return CustomUser.objects.get(pk=user_id)

    def __get_username(self, email, password):
        string = (str(email) + str(password)).encode('utf-8')
        return hashlib.sha512(string).hexdigest()


