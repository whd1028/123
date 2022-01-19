# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class N_Category(models.Model):
    c_id = models.AutoField(primary_key=True)
    c_name = models.CharField(unique=True, max_length=5)

    class Meta:
        managed = False
        db_table = 'N_category'


class N_CategoryDetail(models.Model):
    cd_id = models.AutoField(primary_key=True)
    c = models.ForeignKey(N_Category, models.DO_NOTHING)
    cd_name = models.CharField(unique=True, max_length=10)

    class Meta:
        managed = False
        db_table = 'N_category_detail'


class News(models.Model):
    n_id = models.AutoField(primary_key=True)
    p = models.ForeignKey('Press', models.DO_NOTHING, blank=True, null=True)
    cd = models.ForeignKey(N_CategoryDetail, models.DO_NOTHING, blank=True, null=True)
    n_title = models.CharField(max_length=1024)
    nd_img = models.CharField(max_length=1024, blank=True, null=True)
    n_input = models.DateTimeField(blank=True, null=True)
    o_link = models.CharField(unique=True, max_length=768, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'News'


class N_content(models.Model):
    nc_id = models.AutoField(primary_key=True)
    n = models.ForeignKey('News', models.DO_NOTHING, blank=True, null=True)
    n_content = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'N_content'


class N_summarization(models.Model):
    ns_id = models.AutoField(primary_key=True)
    n = models.ForeignKey('News', models.DO_NOTHING, blank=True, null=True)
    ns_content = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'N_summarization'


class Press(models.Model):
    p_id = models.AutoField(primary_key=True)
    p_name = models.CharField(unique=True, max_length=10)

    class Meta:
        managed = False
        db_table = 'Press'
