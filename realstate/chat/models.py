from email.policy import default
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class ChatMessage(models.Model):
    from_u=models.ForeignKey(User,related_name='from_id',db_column='from_user',on_delete=models.SET_NULL,null=True,blank=True)
    to_u=models.ForeignKey(User,related_name='to_id',db_column='to_user',on_delete=models.SET_NULL,null=True,blank=True)
    message=models.TextField()
    time=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.message
