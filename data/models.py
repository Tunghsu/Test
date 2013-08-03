from django.db import models

# Create your models here.
from __future__ import unicode_literals

from django.db import models

class Category(models.Model):
    id_category = models.IntegerField(primary_key=True)
    name_category = models.CharField(max_length=255L, blank=True)
    intro = models.CharField(max_length=255L, blank=True)
    class Meta:
        db_table = 'category'

class CollectionPage(models.Model):
    id_collection_page = models.IntegerField(primary_key=True)
    id_category = models.IntegerField(null=True, blank=True)
    name_collection_page = models.CharField(max_length=255L, blank=True)
    tag = models.TextField(blank=True)
    class Meta:
        db_table = 'collection_page'

class Comment(models.Model):
    id_comment = models.IntegerField(primary_key=True)
    id_video = models.IntegerField(null=True, blank=True)
    id_page = models.IntegerField(null=True, blank=True)
    id_user = models.IntegerField(null=True, blank=True)
    date = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = 'comment'

class Group(models.Model):
    id_group = models.IntegerField(primary_key=True)
    name_group = models.CharField(max_length=255L, blank=True)
    grights = models.CharField(max_length=100L, blank=True)
    class Meta:
        db_table = 'group'

class User(models.Model):
    id_user = models.IntegerField(primary_key=True)
    id_group = models.IntegerField(null=True, blank=True)
    name_user = models.CharField(max_length=255L, blank=True)
    points = models.IntegerField(null=True, blank=True)
    role = models.IntegerField(null=True, blank=True)
    avatar = models.CharField(max_length=255L, blank=True)
    time_creation = models.CharField(max_length=45L, blank=True)
    class Meta:
        db_table = 'user'

class Video(models.Model):
    id_video = models.IntegerField(primary_key=True)
    time_length = models.IntegerField(null=True, blank=True)
    intro = models.TextField(blank=True)
    source_type = models.IntegerField(null=True, blank=True)
    count = models.IntegerField(null=True, blank=True)
    name_video = models.CharField(max_length=255L, blank=True)
    source_url = models.CharField(max_length=255L, blank=True)
    date = models.CharField(max_length=45L, blank=True)
    class Meta:
        db_table = 'video'

class Videocollection(models.Model):
    id_collection = models.IntegerField(primary_key=True)
    id_page = models.IntegerField(null=True, blank=True)
    date = models.CharField(max_length=45L, blank=True)
    id_collection_page = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'videocollection'

class Videopage(models.Model):
    id_page = models.IntegerField(primary_key=True)
    id_category = models.IntegerField(null=True, blank=True)
    name_page = models.CharField(max_length=255L, blank=True)
    intro = models.TextField(blank=True)
    time_length = models.IntegerField(null=True, blank=True)
    tag = models.TextField(blank=True)
    id_comment = models.IntegerField(null=True, blank=True)
    id_admin = models.IntegerField(null=True, blank=True)
    count = models.TextField(blank=True)
    date = models.CharField(max_length=45L, blank=True)
    class Meta:
        db_table = 'videopage'
