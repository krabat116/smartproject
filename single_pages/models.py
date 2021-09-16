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


class Jinmae(models.Model):
    코드 = models.CharField(primary_key=True, max_length=20)
    제품명 = models.CharField(max_length=40)
    브랜드 = models.CharField(max_length=20)
    제품상세분류 = models.CharField(max_length=20)
    제공량 = models.IntegerField()
    에너지 = models.IntegerField()
    단백질 = models.IntegerField()
    지질 = models.IntegerField()
    탄수화물 = models.IntegerField()
    총당류 = models.IntegerField()
    나트륨 = models.IntegerField()
    콜레스테롤 = models.IntegerField()
    총포화지방산 = models.IntegerField()
    트랜스지방산 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jinmae'