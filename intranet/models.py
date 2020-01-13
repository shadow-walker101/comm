from django.db import models
from django.contrib.auth.models import(BaseUserManager, AbstractBaseUser, PermissionsMixin)

class MyUserManager(BaseUserManager):
    def create_user(self, email, user_type, departments, username, password=None):
        
    
        if not email:
            raise ValueError('Users must have an email address')
        
        user = self.models(
            email=self.normalize_email(email),
            username=username,
            user_type=user_type,
            departments=departments,
        )
        
        user.set_password(password)
        use.save(using=self._db)
        return user
    
    def create_superuser(self, email, user_type, departments, username, password=None):
        user = self.create_user(
            
            email,
            user_type=user_type,
            departments=departments,
            username=username,
            password=password,
        )
    

class User(AbstractBaseUser, PermissionsMixin):
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