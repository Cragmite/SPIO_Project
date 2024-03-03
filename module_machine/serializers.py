from rest_framework.serializers import ModelSerializer
from .models import Machine

class MachineSerializer(ModelSerializer):
    class Meta:
        model = Machine
        fields = '__all__'