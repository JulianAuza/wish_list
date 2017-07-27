# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import bcrypt
import re

class User(models.Model):
    name = models.CharField(max_length = 128)
    user_name = models.CharField(max_length = 128)
    email = models.CharField(max_length = 128)
    password = models.CharField(max_length = 128)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Item(models.Model):
    name=models.CharField(max_length = 128)
    add_by = models.ForeignKey(User)
    added_at = models.DateTimeField(auto_now_add=True)

class Wishlist(models.Model):
    owner = models.ForeignKey(User)
    item = models.ForeignKey(Item)
    added_at = models.DateTimeField(auto_now_add=True)