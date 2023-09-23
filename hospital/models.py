from django.db import models
from accounts.models import User


# class Department(models.Model):
#     name = models.CharField(max_length=255)

#     def __str__(self):
#         return self.name
    
class Todo(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    modified_at=models.DateTimeField(auto_now=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
