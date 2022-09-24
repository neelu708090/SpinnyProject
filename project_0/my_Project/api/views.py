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
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self, request, format=None):
        cuboids = Cuboid.objects.all()
        serializer = CuboidSerializer(cuboids, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CuboidSerializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer,request)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self,serializer,request):
        data = request.data
        length = data.get('length')
        breath = data.get('breath')
        height = data.get('height')
        serializer.save(owner=self.request.user,area=cuboid_area(length,breath,height),volume=cuboid_volume(length,breath,height))

class CuboidDetail(APIView):
    """
    Retrieve, update or delete a cuboids instance.
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

    def put(self, request, pk, format=None):
        cuboids = self.get_object(pk)
        serializer = CuboidSerializer(cuboids, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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

    def put(self, request, pk, format=None):
        cuboids = self.get_object(pk)
        serializer = UpdateCuboidSerializer(cuboids, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserCuboidList(APIView):
    """View the list of cuboids Created by Authenticated user"""
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get_user_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except Cuboid.DoesNotExist:
            raise Http404

    def get(self, request,pk, format=None):
        user = self.get_user_object(pk)
        cuboids = Cuboid.objects.filter(owner=user.id)
        serializer = UserCuboidSerializer(cuboids, many=True)
        return Response(serializer.data)

# def saveData(nihal,ln):
#     cuboid_obj = Cuboid()
#     cuboid_obj.height=132
#     cuboid_obj.length = ln
#     cuboid_obj.author = 1
#     cuboid_obj.owner = 1
#     cuboid_obj.created_by = 'NihalSingh'
#     cuboid_obj.last_updated = 'NihalSingh'
#     cuboid_obj.breath=255
#     cuboid_obj.save()

#     # def test_func(self):
#     #         cuboid = self.get_object()
#     #         if self.request.author == cuboid.author :
#     #             return True
#     #         return False



# @api_view(['GET'])
# def getData(request):
#     cuboids = Cuboid.objects.all()
#     serializer = CuboidSerializer(cuboids , many=True)
#     return Response(serializer.data)

# @api_view(['POST'])
# def addData(request):
#     serializer = CuboidSerializer(data=request.data)

#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['POST'])
# def updateData(request,pk):
#     cuboid = Cuboid.objects.get(pk=pk)
#     serializer = CuboidSerializer(instance=cuboid,data=request.data)

#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['DELETE'])
# def delData(request,pk):
#     try:
#         cuboid = Cuboid.objects.get(pk=pk)
#         if request.method == 'DELETE':
#             cuboid.delete()
#             return Response(status=status.HTTP_204_NO_CONTENT)
#     except Cuboid.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
    
