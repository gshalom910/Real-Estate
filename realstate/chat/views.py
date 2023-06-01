from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import ChatMessage
from django.db.models import Q
# Create your views here.
@login_required
def index(request):
    u=User.objects.exclude(id=request.user.id)
    return render(request,'index.html',{'users':u})

@login_required
def chat_v(request,pk):
    user=User.objects.get(id=pk)
    if request.method == 'POST':
        from_u=request.user
        to_u=user
        message=request.POST['mess']
        c=ChatMessage.objects.create(from_u=from_u,to_u=to_u,message=message)
        c.save()
    m=ChatMessage.objects.filter(Q(from_u=request.user,to_u=user)|Q(from_u=user,to_u=request.user)).order_by('time')
    return render(request,'main/chat.html',{'chats':m})
