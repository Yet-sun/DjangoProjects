from django.db import models


class Image(models.Model):
    photo = models.ImageField(upload_to='upload', null=True, blank=True)

    def __str__(self):
        return self.photo


class Guest(models.Model):
    username = models.CharField(primary_key=True,max_length=50)
    password = models.CharField(max_length=50)
    name = models.CharField(max_length=30)
    # id = models.AutoField(primary_key=True)
    age = models.IntegerField(default=0)
    sex = models.CharField(max_length=10)
    # level-->权限级别：0：普通用户；1：vip
    level = models.IntegerField(default=0)



    def __str__(self):
        return self.username
