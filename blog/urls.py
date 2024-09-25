from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/',views.post_detail,name='post_detail'),
    path('post/<int:pk>/edit/',views.post_edit,name='post_edit'),
    path('post/new/', views.post_new, name='post_new'),

    #path('post/new/', views.post_new, name='post_new'),
    #doesnt work when being included.
    #path('/test',views.post_new,name='post_list')
    #urls when put in from the main application, dont start with a forward slash, it will be a 404, instead start with
    #no front slash. like the post example above.
    #redoing the test route.
  
     #creates  a new post associated with a user which is not set up.
     # path('test',views.post_new,name='post_list')  
     #lets create a listing of animals from the sql db from another vi
     path('testdb',views.animal_list,name='animal_list')

]
