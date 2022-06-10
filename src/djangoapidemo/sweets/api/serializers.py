from rest_framework import serializers
from sweets.models import Sweet

class SweetSerializer(serializers.ModelSerializer):
    class Meta:
        fields=('id','description','title')
        model=Sweet 