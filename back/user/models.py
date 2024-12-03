from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class UserAccountManager(BaseUserManager):
    def create_user(self, email, password=None, issuper=False, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)

        user.set_password(password)
        user.save()
        if not issuper:
            cliente = Cliente.objects.create(user=user)
            cliente.save()

        return user

    def create_superuser(self, email, password, **extra_fields):
        user = self.create_user(
            email, password, True, ** extra_fields)

        user.is_superuser = True
        user.is_staff = True
        user.is_client = False
        user.save()

        return user


class UserAccount(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_client = models.BooleanField(default=True)

    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    class Meta:
        ordering = ['email']

    def get_full_name(self):
        return self.first_name + ' ' + self.last_name

    def get_short_name(self):
        return self.first_name

    def __str__(self):
        return self.email


class Cliente(models.Model):
    direccion = models.CharField(max_length=255)
    num_telefono = models.CharField(max_length=20, default='')
    user = models.OneToOneField(UserAccount, on_delete=models.CASCADE)


class Empleado(models.Model):
    cargo = models.CharField(max_length=255)
    user = models.OneToOneField(UserAccount, on_delete=models.CASCADE)
