from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__' 

# class ItemUpdateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Cuboid
#         fields = ['length','breath','height']