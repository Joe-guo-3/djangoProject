from django.db import models

# Create your models here.
class UserInfo(models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    age = models.IntegerField()
    # add_1 = models.IntegerField(default=2)
    # add_2 = models.IntegerField(null=True, blank=True)

# 会创建一个表单
"""
create table app01_userinfo(
    id bigint auto_increment primary key
    name varchar(32)
    password varchar(64)
    age int
)
"""

# class Role(models.Model):
#     caption = models.CharField(max_length=1

class Department(models.Model):
    title = models.CharField(max_length=16)

Department.objects.create(title="销售部")