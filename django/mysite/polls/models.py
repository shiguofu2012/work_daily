from django.db import models
import time
# Create your models here.


class user(models.Model):
    uid = models.AutoField(primary_key=True)
    nickname = models.CharField(max_length=255)
    password = models.CharField(max_length=255, default='123456')
    reg_time = models.BigIntegerField(default=int(time.time()))

    class Meta:
        db_table = 'user'
