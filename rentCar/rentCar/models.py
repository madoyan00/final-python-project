from django.db import models


class Car(models.Model):
  brand = models.CharField(max_length=100) 
  model = models.CharField(max_length=100)
  year = models.IntegerField()
  price = models.DecimalField(max_digits=10, decimal_places=2)
  transmission = models.CharField(max_length=20)
  phoneNumber = models.IntegerField()
  location = models.CharField(max_length=20)
  image = models.ImageField(upload_to='car_images/', null=True, blank=True)



  def __str__(self):
    return f"{self.brand} {self.model} {self.year} {self.price} {self.transmission} {self.phoneNumber} {self.location}"
