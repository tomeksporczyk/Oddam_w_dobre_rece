from django.db import models

# Create your models here.


class Gift(models.Model):
    items = models.ManyToManyField("ItemType")
    quantity = models.IntegerField()
    institution = models.ForeignKey('Institution', on_delete=models.CASCADE)
    pick_up_address = models.ForeignKey('PickUpAddress', on_delete=models.CASCADE)
    courier_information = models.ForeignKey('CourierInformation', on_delete=models.CASCADE)
    created_date = models.DateField(auto_now_add=True)
    picked_up = models.BooleanField(default=False)
    picked_up_date = models.DateField()


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


class Province(models.Model):
    name = models.CharField(max_length=50)


class ItemType(models.Model):
    name = models.CharField(max_length=128)
    description = models.ManyToManyField('ItemDescription')


class ItemDescription(models.Model):
    description = models.CharField(max_length=256)
