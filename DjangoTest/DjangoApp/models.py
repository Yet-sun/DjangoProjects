from django.db import models


class Event(models.Model):  # 会议表
    name = models.CharField(max_length=100)  # 会议标题
    limit = models.IntegerField()  # 参加人数
    status = models.BooleanField()  # 状态
    address = models.CharField(max_length=200)  # 地址
    start_time = models.DateTimeField('events time')  # 发布时间
    create_time = models.DateTimeField(auto_now=True)  # 创建时间（自动获取当前时间）

    def __str__(self):
        return self.name


class Guest(models.Model):  # 参会人员
    event = models.ForeignKey(Event, on_delete=models.CASCADE)  # 外键
    realname = models.CharField(max_length=64)  # 姓名
    phone = models.CharField(max_length=16)  # 手机号
    email = models.EmailField()
    sign = models.BooleanField()  # 签到
    create_time = models.DateTimeField(auto_now=True)  # 创建时间

    def __str__(self):
        return self.realname
