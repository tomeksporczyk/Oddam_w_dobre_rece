from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
# Create your models here.


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_active', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    """
    User model. Describes both, customer user and additionaly
    is a base for workshop instance (:model:`workshop.Workshop`)
    """
    username = None
    email = models.EmailField('user email', unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()


class Gift(models.Model):
    items = models.ManyToManyField("Item")
    quantity = models.IntegerField()
    institution = models.ForeignKey('Institution', on_delete=models.CASCADE)
    pick_up_address = models.ForeignKey('PickUpAddress', on_delete=models.CASCADE)
    courier_information = models.ForeignKey('CourierInformation', on_delete=models.CASCADE)
    created_date = models.DateField(auto_now_add=True)
    picked_up = models.BooleanField(default=False)
    picked_up_date = models.DateField()


class Item(models.Model):
    name = models.CharField(max_length=128)
    type = models.CharField(max_length=128, blank=True)
    description = models.CharField(max_length=128, blank=True)


class PickUpAddress(models.Model):
    street = models.CharField(max_length=256)
    city = models.CharField(max_length=64)
    postal_code = models.CharField(max_length=6)
    phone_number = models.CharField(max_length=15)


class CourierInformation(models.Model):
    date = models.DateField()
    time = models.TimeField()
    message = models.TextField(max_length=1024)


class Institution(models.Model):
    name = models.CharField(max_length=126)
    mission_description = models.TextField(max_length=1024)
    province = models.ForeignKey('Province', on_delete=models.DO_NOTHING)
    target = models.ForeignKey('Target', on_delete=models.DO_NOTHING)


class Target(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Province(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name



# class ItemType(models.Model):
#     name = models.CharField(max_length=128)
#     description = models.ManyToManyField('ItemDescription')
#
#
# class ItemDescription(models.Model):
#     description = models.CharField(max_length=256)
