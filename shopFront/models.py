from django.db import models
from django.contrib.auth.models import User

MEMBERSHIP_BRONZE = 'BRONZE'
MEMBERSHIP_SILVER = 'SILVER'
MEMBERSHIP_GOLD = 'GOLD'

MEMPERSHIP_CHOICES = [
    (MEMBERSHIP_BRONZE , 'BRONZE'),
    (MEMBERSHIP_SILVER , 'SILVER'),
    (MEMBERSHIP_GOLD , 'GOLD'),
]

PAYMENT_STATUS_PENDING = 'PENDING'
PAYMENT_STATUS_COMPLETE = 'COMPLETE'
PAYMENT_STATUS_FAILED = 'FAILED'

PAYMENT_STATUS_CHOICES = [
    (PAYMENT_STATUS_PENDING , 'PENDING'),
    (PAYMENT_STATUS_COMPLETE , 'COMPLETE'),
    (PAYMENT_STATUS_FAILED , 'FAILED'),

]

# Create your models here.


class Promotion(models.Model):
    description = models.CharField(max_length=255)
    discount = models.FloatField()
    
    def __str__(self):
        return self.description


class Product(models.Model):
    CATEGORY = (
			('Hot', 'Hot'),
			('Cold', 'Cold'),
			)
    HOLIDAYS = (
        ('Eid al-Fitr', 'Eid al-Fitr'),
        ('Christmas', 'Christmas'),
        ('Halloween', 'Halloween'),
    ) 
    title = models.CharField(max_length=255)
    description = models.TextField()
    unit_price = models.DecimalField(max_digits=6,decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)
    promotions = models.CharField(max_length=200, null=True, choices=HOLIDAYS)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)

    def __str__(self):
        return self.title


class Customer(models.Model):
    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    profile_pic = models.ImageField(null=True,blank=True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True)
    membership = models.CharField(max_length=6,choices=MEMPERSHIP_CHOICES,default=MEMBERSHIP_BRONZE)

    def __str__(self):
        return self.last_name
    
class Order(models.Model):
    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=20,choices=PAYMENT_STATUS_CHOICES,default=PAYMENT_STATUS_PENDING)
    customer = models.ForeignKey(Customer,on_delete=models.PROTECT)
    product = models.ForeignKey(Product,null=True, on_delete=models.PROTECT)
    note = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return self.product.title
