# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    GENDER = {
        ('Male',1),
        ('Female',0),
    }
    userid = models.AutoField(primary_key=True)
    username = models.CharField("用户名",max_length = 12)
    nickname = models.CharField("用户昵称",max_length = 30)
    avatoridx = models.IntegerField('头像索引号')
    gender = models.IntegerField("用户性别",choices=GENDER)
    cellphone = models.CharField("手机号码", max_length = 11 )
    password = models.CharField("密码", max_length = 40)
    gold = models.IntegerField('金币')
    diamond = models.IntegerField('钻石')
    createtime = models.DateTimeField(auto_now=True)
    agentid = models.ForeignKey('Agent', db_column='agentid' , blank=True, null=True, on_delete = models.SET_NULL)
    promoteid = models.ForeignKey('Promote', db_column='promoteid',blank=True, null=True, on_delete = models.SET_NULL)
    disable = models.BooleanField('是否账号被禁用',default=False)

    class Meta:
        db_table = 'User'



class Agent(models.Model):
    agentid = models.AutoField(primary_key=True)
    name = models.CharField("代理名称",max_length = 50)
    cellphone = models.CharField("手机号码",max_length = 11)
    password = models.CharField("密码",max_length = 40)
    createtime = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Agent'


class Promote(models.Model):
    promoteid = models.AutoField(primary_key=True)
    code = models.CharField('推广码', max_length = 20)
    name = models.CharField('推广名称', max_length = 30)
    detail = models.CharField('描述',max_length = 100)
    createtime = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Promote'


class Game(models.Model):
    gameid = models.AutoField(primary_key=True)
    name = models.CharField('游戏名',max_length = 30)
    minplayers = models.IntegerField('最下游戏人数')
    maxplayers = models.IntegerField('最大游戏人数')
    enable = models.BooleanField('游戏是否启用',default = True)

    class Meta:
        db_table = 'Game'


class GameRoom(models.Model):
    roomid = models.AutoField(primary_key=True)
    gameid = models.ForeignKey('Game',db_column='gameid',blank=True,null=True,on_delete=models.SET_NULL)
    name = models.CharField('房间名',max_length=30)
    minentry = models.IntegerField('最小准入')
    maxentry = models.IntegerField('最下准入')
    enable = models.BooleanField('房间是否启用',default=True)

    class Meta:
        db_table = 'GameRoom'


class ForbiddenIp(models.Model):
    forbidid = models.AutoField(primary_key=True)
    ip = models.CharField('ip', max_length = 32)

    class Meta:
        db_table = 'ForbiddenIp'


class ForbiddenUser(models.Model):
    forbidid = models.AutoField(primary_key=True)
    userid = models.ForeignKey('User',db_column='userid',blank=True,null=True, on_delete=models.SET_NULL)

    class Meta:
        db_table = 'ForbiddenUser'


class LoginRecord(models.Model):
    id = models.AutoField(primary_key=True)
    userid = models.ForeignKey('User',db_column='userid',blank=True,null=True, on_delete=models.SET_NULL)
    logintime = models.DateTimeField()
    loginip = models.CharField(max_length=32)

    class Meta:
        db_table = 'LoginRecord'
