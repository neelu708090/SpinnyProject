from django.urls import path
from . import views

urlpatterns = [
    path('cuboids/',views.CuboidList.as_view()), #view all Cuboid objects
    path('cuboids/<int:pk>/',views.CuboidDetail.as_view()),#view cuboid object with respect to their primary key 
    path('user/',views.UserList.as_view()), #view all User objects
    path('user/<int:pk>/',views.UserDetail.as_view()), #view User object with respect to their Primary keys
    path('update/<int:pk>/',views.UpdateCuboid.as_view()), # Update cuboid data
    path('user-profile/<int:pk>/',views.UserCuboidList.as_view()), #view user profile with all their added data
]