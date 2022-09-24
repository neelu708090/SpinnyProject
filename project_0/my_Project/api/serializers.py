from rest_framework import serializers
from my_app.models import Cuboid
from django.contrib.auth.models import User

class CuboidSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Cuboid
        fields = ['length','breath','height','created_by','owner','last_updated']

class UserSerializer(serializers.ModelSerializer):
    cuboids = serializers.PrimaryKeyRelatedField(many=True, queryset=Cuboid.objects.all())
    class Meta:
        model = User
        fields = '__all__'