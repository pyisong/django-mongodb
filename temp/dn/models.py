# -*- coding:utf-8 -*-

from django.db import models

# Create your models here.


class MyModel(models.Model):
    my_id = models.IntegerField(verbose_name='ID', auto_created=True, primary_key=True)
    name = models.CharField(verbose_name='名字', max_length=20)
    age = models.IntegerField(verbose_name="年龄")
    class Meta:
        app_label = 'dn'


if __name__ == "__main__":
    my_model = MyModel()
    print my_model._meta.app_label
