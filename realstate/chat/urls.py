from django.urls import path
from . import views

urlpatterns = [
    # path('',views.index),
    path('chat/<int:pk>/',views.chat_v,name='chat')
]