from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.contrib.gis.db import models


# class temp(models.Model):

class UsersData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    usertype = models.CharField(max_length=100) #change to option type
    mobile = models.CharField(max_length=20)
    image = models.ImageField(upload_to='pics/', null=True) 
    address = models.CharField(max_length=500)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    reg_date = models.DateField(auto_now_add=True)
    token = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.user.username


class RentHome(models.Model): #geo
    uid = models.ForeignKey(UsersData, on_delete=models.CASCADE)
    address= models.CharField(max_length=400, unique=True)
    image1 = models.ImageField(upload_to='img/house/', null=True)
    image2 = models.ImageField(upload_to='img/house/', null=True)
    image3 = models.ImageField(upload_to='img/house/', null=True)
    image4 = models.ImageField(upload_to='img/house/', null=True)
    description = models.CharField(max_length=500, default=' ')
    rent_capacity = models.CharField(max_length=5, default=1)
    rent = models.FloatField()
    location = models.PointField(srid=4326)
    #dateAdded = models.DateTimeField('date added', auto_now_add=True)
    is_available = models.BooleanField()

    def __str__(self):
        return self.address
class locator(models.Model): #geo
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100, unique=True)
    country = models.CharField(max_length=100)
    code = models.CharField(max_length=10, default="1")
    geom = models.PolygonField(srid=4326)
    def __str__(self):
        return str((self.city + " "+  self.state))

class street(models.Model): # geo
    streeName = models.CharField("Street Name", max_length=80 , unique=True )
    description = models.TextField()
    geometry = models.LineStringField(srid=4326)
    def __str__(self):
        return self.streeName


class Transactions(models.Model):
    uid = models.ForeignKey(UsersData, on_delete=models.CASCADE)  # User id
    hid = models.ForeignKey(RentHome, on_delete=models.CASCADE)  # House id
    date = models.DateField(auto_now_add=True)
    amount = models.FloatField()

    def __str__(self):
        return self.name


class Contract(models.Model):
    uid = models.ForeignKey(UsersData, on_delete=models.CASCADE)  # User id
    hid = models.ForeignKey(RentHome, on_delete=models.CASCADE)  # House id
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    duration = models.IntegerField(null=True,blank=True)
    # Active, Completed
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.name