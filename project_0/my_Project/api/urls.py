from django.urls import path
from . import views

urlpatterns = [
    path('cuboids/',views.CuboidList.as_view()),
    path('cuboids/<int:pk>/',views.CuboidDetail.as_view()),
    path('user/',views.UserList.as_view()),
    path('user/<int:pk>/',views.UserDetail.as_view()),
]