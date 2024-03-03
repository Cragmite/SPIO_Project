from rest_framework.serializers import ModelSerializer
from .models import Failure

class FailureSerializer(ModelSerializer):
    class Meta:
        model = Failure
        fields = '__all__'