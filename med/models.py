# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Gongju(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    gname = models.CharField(db_column='GName', max_length=100, db_collation='Chinese_PRC_CI_AS')  # Field name made lowercase.
    price = models.DecimalField(db_column='Price', max_digits=10, decimal_places=2)  # Field name made lowercase.
    many = models.IntegerField(db_column='Many')  # Field name made lowercase.
    about = models.CharField(db_column='About', max_length=500, db_collation='Chinese_PRC_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'gongju'


class Medicine(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    mname = models.CharField(db_column='MName', max_length=100, db_collation='Chinese_PRC_CI_AS')  # Field name made lowercase.
    price = models.DecimalField(db_column='Price', max_digits=10, decimal_places=2)  # Field name made lowercase.
    many = models.IntegerField(db_column='Many')  # Field name made lowercase.
    about = models.CharField(db_column='About', max_length=500, db_collation='Chinese_PRC_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Medicine'
