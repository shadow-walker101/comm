from django.db import models

from django.contrib.auth.base_user import(BaseUserManager, AbstractBaseUser, Pe)

class MyUserManager(BaseUserManager):
    pass

class User(AbstractBaseUser):
    USER_TYPES_CHOICES = (
        
        (1, 'SuperAdmin'),
        (2, 'Admin'),
        (3, 'Employee'),
        
    )
    
    DEPARTMENTS = (
        
        (1, 'Human Resource'),
        (2, 'Inventory' ),
        (3, 'Finance'),
        (4, 'Marketing'),
        (5, 'Information Technology'),
    )
    
    email = models.EmailField(max_length=,100, unique=True)
    username = models.CharField(max_length=200)
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPES_CHOICES)
    is_active = models.BooleanField(default=True) 
    is_admin = models.BooleanField(default=False)
    departments = models.PositiveSmallIntegerField(choices=DEPARTMENTS)   
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'user_type']
    
    def __str__(self):
        return self.username
    
    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
