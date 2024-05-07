from django.db import models

class Record(models.Model):
    medicine_name = models.CharField(max_length=100)
    medicine_description = models.CharField(max_length=255)
    medicine_price=models.CharField(max_length=255)

    

   
