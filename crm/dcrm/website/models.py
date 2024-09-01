from django.db import models

# Create your models here.
class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50)
    last_name =  models.CharField(max_length=50)
    email =  models.CharField(max_length=100)
    phone = models.CharField(max_length=12)
    address =  models.CharField(max_length=100)
    Govrment =  models.CharField(max_length=50)
    city =  models.CharField(max_length=50)
    id_number =  models.CharField(max_length=14)

def __str__(self):
		return(f"{self.first_name} {self.last_name}")
