"""
We have to provide headers in user-filter and filter url. In headers we have to mention these three values
1- value = length or breath or height or area or volume 
2- condition = {
    gt - for grater than or
    lt - for less than
}
3- number = number you want to filter from

e.g. - value = length,condition = gt, number = 10  | This gives filtered objects in return

"""

from django.urls import path
from . import views

urlpatterns = [
    path('cuboids/',views.CuboidList.as_view()), 
    path('cuboids/<int:pk>/',views.CuboidDetail.as_view()),
    path('users/',views.UserList.as_view()), 
    path('user/<int:pk>/',views.UserDetail.as_view()), 
    path('cuboid-update/<int:pk>/',views.UpdateCuboid.as_view()), 
    path('user-profile/<int:pk>/',views.UserCuboidList.as_view()),
    path('user-filter/<int:pk>/',views.UserFilterCuboidList.as_view()),
    path('filter/',views.FilterCuboidList.as_view()),

]