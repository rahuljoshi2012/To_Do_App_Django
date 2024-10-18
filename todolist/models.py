from django.db import models
from django.contrib.auth.models import User

class todo(models.Model):
    srno = models.AutoField(primary_key=True)
    title = models.TextField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
