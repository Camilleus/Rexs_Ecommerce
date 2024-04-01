from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
import datetime


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name    
    
    class Meta:
        verbose_name_plural = 'Categories'


class Customer(models.Model):
    user_name = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    
    def __str__(self):
        return f'{self.user_name}, {self.first_name} {self.last_name}'
    
    
class Product(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', unique=True)
    name = models.CharField(max_length=100)
    price = models.DecimalField(default=0, max_digits=7, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=500, default='', blank=True, null=True)
    image = models.ImageField(upload_to='uploads/product/')

    # Sale Stuff
    is_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(default=0, max_digits=7, decimal_places=2)
    # Bestseller Stuff
    is_bestseller = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name   
    
    
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=100, default='', null=True, blank=True)
    phone = models.CharField(max_length=15, default='', null=True, blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.product  


# Create A User Profile Model
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	follows = models.ManyToManyField("self", 
		related_name="followed_by",
		symmetrical=False,
		blank=True)	
	
	date_modified = models.DateTimeField(User, auto_now=True)	
	profile_image = models.ImageField(null=True, blank=True, upload_to="images/")
	
	profile_bio = models.CharField(null=True, blank=True, max_length=500)
	homepage_link = models.CharField(null=True, blank=True, max_length=100)
	facebook_link = models.CharField(null=True, blank=True, max_length=100)
	instagram_link = models.CharField(null=True, blank=True, max_length=100) 
	linkedin_link = models.CharField(null=True, blank=True, max_length=100)
	
	def __str__(self):
		return self.user.username

# Create Profile When New User Signs Up
#@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
	if created:
		user_profile = Profile(user=instance)
		user_profile.save()
		# Have the user follow themselves
		user_profile.follows.set([instance.profile.id])
		user_profile.save()

post_save.connect(create_profile, sender=User)


