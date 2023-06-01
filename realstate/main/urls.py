
from . import views
from django.urls import path

urlpatterns = [
 path('',views.index,name='index'),
 path('about/',views.about,name='about'),
 path('create/',views.create_p,name='create'),
 path('addgallery/',views.gallery,name='gallery'),
 path('pro/',views.property,name='pro'),
 path('detail/<int:pk>',views.detail,name='detail'),
 path('chat/',views.chat,name='chat'),
 path('login/',views.loginuser,name='login'),
  path('logout/',views.logout_user,name='logout'),
 path('register/',views.registration,name='register'),

   
]