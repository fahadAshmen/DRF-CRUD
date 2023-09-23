from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager


class UserManager(BaseUserManager):
    # def create_user(self, email, username, password=None, **extra_fields):
    #     print('===>',email,username)
    #     if not email:
    #         raise ValueError('User must have an email address')
        
    #     if not username:
    #         raise ValueError('User must have an username')
        
    #     user = self.model(
    #         email=self.normalize_email(email),
    #         username=username,
    #         **extra_fields
    #     )
    #     print(user)
        
    #     if password is not None:
    #         user.set_password(password)
        
    #     user.is_active = True
    #     user.save(using=self._db)
    #     return user
    def create_user(self, email, username, password=None,  **extra_fields):
        if not email:
            raise ValueError('User must have an email address')
        
        if not username:
            raise ValueError('User must have an username')
        
        user = self.model(
            email = self.normalize_email(email),
            username = username,            
            **extra_fields)   
   
        user.is_active = True  
        user.set_password(password) 
        print(f'Password before save: {user.password}')       
        user.save(using=self._db)
        print(f'Password after save: {user.password}')
        return user
    
    def create_superuser(self, username, email, password=None, **extra_fields):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password=password,
            **extra_fields                 
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        print("Creating SUPPER USER")
        user.save(using=self._db)
        return user




class User(AbstractBaseUser):

    MANAGER = 1
    DOCTOR = 2
    PATIENT = 3

    ROLES = (
        (MANAGER , 'manager'), 
        (DOCTOR , 'doctor'),
        (PATIENT , 'patient')
        )
    

    email = models.EmailField(max_length=50, unique=True)
    password = models.CharField(max_length=128, null=True)
    username = models.CharField(max_length=255, unique=True)
    first_name = models.CharField(max_length=150, null=True, blank=True)
    last_name = models.CharField(max_length=150, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    roles = models.PositiveSmallIntegerField(choices=ROLES,default="")
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_admin     =models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','roles']


    # objects = UserManager()
    
    def __str__(self):
        return self.email
    
    # def __str__(self):
    #     return self.get_roles_display()
    
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, add_label):
        return True
