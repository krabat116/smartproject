from django.db import models
import datetime
import os

# Create your models here.

def filepath(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    filename = "%s%s",(timeNow, old_filename)
    return os.path.join('uploads/, filename')

class Item(models.Model):
    name =models.TextField(max_length=191)
    price =models.TextField(max_length=50)
    description =models.TextField(max_length=500, null=True)
    image = models.ImageField(upload_to=filepath, null=True, blank=True)





class Lang(models.Model):
    id = models.CharField(primary_key=True, max_length=45)
    name = models.CharField(max_length=45)
    description = models.CharField(max_length=45)
    study = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'lang'
        unique_together = (('id', 'name', 'description', 'study'),)