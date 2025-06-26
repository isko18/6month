from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email обязателен")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Суперпользователь должен иметь is_staff=True")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Суперпользователь должен иметь is_superuser=True")
        
        return self.create_user(email=email, password=password, **extra_fields)
    
class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        unique=True,
        verbose_name="email"
    )
    full_name = models.CharField(
        max_length=255,
        verbose_name="ФИО"
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="Активный"
    )
    is_staff = models.BooleanField(
        default=False,
        verbose_name="Стаф"
    )
    date_joined = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания"
    )
    
    objects = CustomUserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']
    
    def __str__(self):
        return self.email
    
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        