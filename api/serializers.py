""" USE '__all__' in fields to view all instances of Cuboid"""
from rest_framework import serializers
from my_app.models import Cuboid
from django.contrib.auth.models import User

class CuboidSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    created_by = serializers.ReadOnlyField(source='owner.username')
    last_updated = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Cuboid
        fields = ['length','breath','height','created_by','owner','last_updated']

class UserSerializer(serializers.ModelSerializer):
    cuboids = serializers.PrimaryKeyRelatedField(many=True, queryset=Cuboid.objects.all())
    class Meta:
        model = User
        fields = '__all__'

class UpdateCuboidSerializer(serializers.ModelSerializer):
    last_updated = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Cuboid
        fields = ['length','breath','height','last_updated']
        read_only_fields = ['created_by','owner']

class UserCuboidSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='owner.username')
    last_updated = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Cuboid
        fields = ['length','breath','height','area','volume','created_by','last_updated','creation_date']