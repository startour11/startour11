from django.db import models
import datetime
from tinymce.models import HTMLField

# Create your models here.

class contact(models.Model):
    fullname=models.CharField(max_length=100)
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=200)
    message=models.TextField()
    class Meta:
        db_table="contact"


         
    
class blogs(models.Model):
    title=models.CharField(max_length=100)
    description=HTMLField()
    photo=models.ImageField(upload_to='blogs/')
    post_by=models.CharField(max_length=50,default="Admin")
    post_on=models.DateField(default=datetime.date.today())
    class Meta:
         db_table="blogs"
    def __str__(self):
        return self.title
    

class Hotels(models.Model):
    name=models.CharField(max_length=100)
    location=models.CharField(max_length=10)
    maplocation=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    photo1=models.ImageField(upload_to='cover/', default="")
    photo2=models.ImageField(upload_to='room pic/', default="")
    photo3=models.ImageField(upload_to='reception/')
    description=models.TextField()
    rating=models.CharField(max_length=100)
    from_price=models.FloatField()
    to_price=models.FloatField()
    class Meta:
         db_table="Hotels"
    def __str__(self):
        return self.name    
         
class Touristplaces(models.Model):
    name=models.CharField(max_length=100)
    addresslocation=models.CharField(max_length=10)
    maplocation=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    photo1=models.ImageField(upload_to='cover/', default="")
    photo2=models.ImageField(upload_to='room pic/', default="")
    photo3=models.ImageField(upload_to='reception/', default="")
    description=models.TextField()
    class Meta:
         db_table="Touristplaces"
    def __str__(self):
        return self.name 
       
class faqs(models.Model):
    question=models.TextField()
    answer=models.TextField()
    class Meta:
        db_table="faqs"
    def __str__(self):
        return self.question 
    
class booking(models.Model):
    FirstName=models.CharField(max_length=100, default="") 
    LastName=models.CharField(max_length=100, default="") 
    No_of_Children=models.CharField(max_length=100, default="") 
    ContactNumber=models.CharField(max_length=100,default="") 
    No_of_Adults=models.CharField(max_length=100, default="") 
    EmailId=models.CharField(max_length=100, default="") 
    CheckIn=models.CharField(max_length=100,default="") 
    Checkout=models.CharField(max_length=100,default="")
    Tourtype=models.CharField(max_length=100, default="")
    instructions=models.TextField(default="")
    class Meta:
        db_table="booking" 
 

    def __str__(self):
        return self.FirstName 

TOURTYPE=(
    ('Religious','Religious'),
    ('Adventurous','Adventurous'),
    ('Honeymoon','Honeymoon'),
    ('Sports','Sports'),
    ('Student','Student'),
    ('Wildlife','Wildlife'),
    ('Hill Station','Hill Station'),
    ('Traditional','Traditional'),
    ('Vocation','Vocation'),
)

class tour(models.Model):
    type=models.CharField(max_length=200,choices=TOURTYPE)
    title=models.TextField(max_length=100)
    noofdays=models.CharField(max_length=100)
    Image=models.ImageField(upload_to='tour/', default="",blank=True,null=True)
    description=HTMLField()
    price=models.FloatField()
    includesexcludes=HTMLField(default="")
    class Meta:
      db_table="tour"
    def __str__(self):
        return self.title 
     
       
         
    

    
