# SpinnyProject

Do following steps to run this project.

1. Create a Virtual Environment
2. Install modules. Used modules are provided in requirement.txt file.
3. Create super user in django.
4. After creating super user if you want more users create users in admin/ url of django.
5. Following urls are provided in urls of my_app.
	1-'cuboids/' - 1)returns all cuboid instances., 2) create new cuboid if logged user is staff. 
    	2-'cuboids/<int:pk>/' - 1)returns cuboid instance with respect to cuboid id as pk., 2) user can delete cuboid instance if logged user is owner of cuboid.
    3-'users/' - 1)returns all users list. 
    4-'user/<int:pk>/' - 1)return user with respect to their id. 
    5-'cuboid-update/<int:pk>/' - 1)update cuboid with respect to cuboid id. 
    6-'user-profile/<int:pk>/' - 1)returns cuboid instance with respect to user id.
    7-'user-filter/<int:pk>/' - 1)returns filterd cuboid of logged user. In this url we have to provide headers details regarding heades is provided in api/urls.
    8-'filter/' - 1)returns filtered cuboid from all cuboid instances. In this url we have to provide headers details regarding heades is provided in api/urls.
    
    
    All Done! Thank You.

