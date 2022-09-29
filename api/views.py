from functools import partial
from urllib import request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.decorators import api_view
from my_app.models import Cuboid
from .serializers import CuboidSerializer,UserSerializer,UpdateCuboidSerializer,UserCuboidSerializer
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly

#-------Functions------
def cuboid_area(length,breath,height):
    area = 2*(length+breath+height)
    return area

def cuboid_volume(length,breath,height):
    volume = length*breath*height
    return volume


class CuboidList(APIView):
    """
    List all cuboids, or create a new cuboids.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
    def get(self, request, format=None):
        cuboids = Cuboid.objects.all()
        serializer = CuboidSerializer(cuboids, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        is_staff=self.request.user.is_staff
        if is_staff == True:
            serializer = CuboidSerializer(data=request.data)
            if serializer.is_valid():
                self.perform_create(serializer,request)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_403_FORBIDDEN)

    def perform_create(self,serializer,request):
        data = request.data
        length = data.get('length')
        breath = data.get('breath')
        height = data.get('height')
        serializer.save(owner=self.request.user,last_updated=self.request.user.username,area=cuboid_area(length,breath,height),volume=cuboid_volume(length,breath,height))

class CuboidDetail(APIView):
    """
    Retrieve or delete a cuboids instance.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get_object(self, pk):
        try:
            return Cuboid.objects.get(pk=pk)
        except Cuboid.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        cuboids = self.get_object(pk)
        serializer = CuboidSerializer(cuboids)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        cuboids = self.get_object(pk)
        cuboids.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UpdateCuboid(APIView):
    """Cuboid instance Updated by Staff"""
    def get_object(self, pk):
        try:
            return Cuboid.objects.get(pk=pk)
        except Cuboid.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        cuboids = self.get_object(pk)
        serializer = UpdateCuboidSerializer(cuboids)
        return Response(serializer.data)


    def put(self, request, pk, format=None):
        cuboids = self.get_object(pk)
        creator = cuboids.owner
        serializer = UpdateCuboidSerializer(cuboids, data=request.data,partial=True)
        if serializer.is_valid():
            self.perform_create(serializer,request,creator)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self,serializer,request,creator):
        data = request.data
        length = data.get('length')
        breath = data.get('breath')
        height = data.get('height')
        serializer.save(owner=creator,last_updated=self.request.user.username,area=cuboid_area(length,breath,height),volume=cuboid_volume(length,breath,height))

class FilterCuboidList(APIView):
    def get_user_object(self,value,condit,num,pk):
        if pk:
            try:
                print('try1')
                match value:
                    case 'length':
                        if condit == "gt":
                            user = User.objects.get(pk=pk)
                            return Cuboid.objects.filter(length__gt = num,owner=user.pk)
                        else:
                            user = User.objects.get(pk=pk)
                            return Cuboid.objects.filter(length__lt = num,owner=user.pk)
                    case 'breath':
                        if condit == "gt":
                            user = User.objects.get(pk=pk)
                            return Cuboid.objects.filter(breath__gt = num,owner=user.pk)
                        else:
                            user = User.objects.get(pk=pk)
                            return Cuboid.objects.filter(breath__lt = num,owner=user.pk)
                    case 'height':
                        if condit == "gt":
                            user = User.objects.get(pk=pk)
                            return Cuboid.objects.filter(height__gt = num,owner=user.pk)
                        else:
                            user = User.objects.get(pk=pk)
                            return Cuboid.objects.filter(height__lt = num,owner=user.pk)
                    case 'area':
                        if condit == "gt":
                            user = User.objects.get(pk=pk)
                            return Cuboid.objects.filter(area__gt = num,owner=user.pk)
                        else:
                            user = User.objects.get(pk=pk)
                            return Cuboid.objects.filter(area__lt = num,owner=user.pk)
                    case 'volume':
                        if condit == "gt":
                            user = User.objects.get(pk=pk)
                            return Cuboid.objects.filter(volume__gt = num,owner=user.pk)
                        else:
                            user = User.objects.get(pk=pk)
                            return Cuboid.objects.filter(volume__lt = num,owner=user.pk)
            except Cuboid.DoesNotExist:
                raise Http404
        else:
            try:
                match value:
                    case 'length':
                        if condit == "gt":
                            return Cuboid.objects.filter(length__gt = num)
                        else:
                            return Cuboid.objects.filter(length__lt = num)
                    case 'breath':
                        if condit == "gt":
                            return Cuboid.objects.filter(breath__gt = num)
                        else:
                            return Cuboid.objects.filter(breath__lt = num)
                    case 'height':
                        if condit == "gt":
                            return Cuboid.objects.filter(height__gt = num)
                        else:
                            return Cuboid.objects.filter(height__lt = num)
                    case 'area':
                        if condit == "gt":
                            return Cuboid.objects.filter(area__gt = num)
                        else:
                            return Cuboid.objects.filter(area__lt = num)
                    case 'volume':
                        if condit == "gt":
                            return Cuboid.objects.filter(volume__gt = num)
                        else:
                            return Cuboid.objects.filter(volume__lt = num)
            except Cuboid.DoesNotExist:
                raise Http404

    def get(self, request,format=None ,pk=None):
        value=request.headers['value']
        condi=request.headers['condition']
        num=request.headers['number']
        cuboids = self.get_user_object(value,condi,num,pk)
        serializer = UserCuboidSerializer(cuboids, many=True)
        return Response(serializer.data)

        
class UserCuboidList(APIView):
    """View the list of cuboids Created by Authenticated user"""
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get_user_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request,pk, format=None):
        user=User.objects.filter(id=pk).first()
        if self.request.user == user:
            user = self.get_user_object(pk)
            cuboids = Cuboid.objects.filter(owner=user.id)
            serializer = UserCuboidSerializer(cuboids, many=True)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

class UserFilterCuboidList(FilterCuboidList,APIView):
    """View the list of cuboids Created by Authenticated user and filter"""
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
    def get(self, request,pk):
        try:
            user = User.objects.filter(id=pk).first()
            if self.request.user == user:
                return super(UserFilterCuboidList,self).get(request,pk=pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)