# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Board(models.Model):
    name = models.CharField(max_length=30, unique=True) # 强制数据库级别字段的唯一性
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name + ' module'



class Topic(models.Model):
    subject = models.CharField(max_length=255)
    last_updated = models.DateTimeField(auto_now_add=True)
    board = models.ForeignKey(Board, related_name='topics')
    starter = models.ForeignKey(User, related_name='topics')


class Post(models.Model):
    message = models.TextField(max_length=4000)
    topic = models.ForeignKey(Topic, related_name='posts')
    #  可选字段，auto_now_add设置为True会自动填充创建时的日期时间
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(null=True)
    # 设置related_name,可以使用 user.posts 来查看这个用户创建了哪些 post
    created_by = models.ForeignKey(User, related_name='posts')
    updated_by = models.ForeignKey(User, null=True, related_name='+')

