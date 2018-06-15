from rest_framework.viewsets import ModelViewSet
from register.models import Register
from .serializers import RegisterSerializer


class RegisterViewSet(ModelViewSet):
    queryset = Register.objects.all()
    serializer_class = RegisterSerializer
