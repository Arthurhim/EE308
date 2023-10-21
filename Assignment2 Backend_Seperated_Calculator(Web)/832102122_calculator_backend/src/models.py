from django.db import models


# Create your models here.
class calData(models.Model):  # mode data
    rad_deg = models.CharField(max_length=3)
    inv = models.DecimalField(max_digits=1, decimal_places=0)

    objects = models.Manager()


class calHistory(models.Model): # history storage data
    formula = models.CharField(max_length=300)
    result = models.CharField(max_length=300)

    objects = models.Manager()  # 启用ORM功能（开启数据库访问）
