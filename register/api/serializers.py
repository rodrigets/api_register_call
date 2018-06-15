from rest_framework.serializers import ModelSerializer
from register.models import Register


class RegisterSerializer(ModelSerializer):
    class Meta:
        model = Register
        fields = ('call_type', 'source', 'time', 'destination', 'call_id')
