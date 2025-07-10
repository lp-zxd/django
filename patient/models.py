# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Bed(models.Model):
    bid = models.AutoField(db_column='BID', primary_key=True)  # Field name made lowercase.
    kid = models.ForeignKey('Keshi', models.DO_NOTHING, db_column='KID', blank=True, null=True)  # Field name made lowercase.
    roomnumber = models.CharField(db_column='RoomNumber', max_length=20, db_collation='Chinese_PRC_CI_AS')  # Field name made lowercase.
    bednumber = models.CharField(db_column='BedNumber', max_length=20, db_collation='Chinese_PRC_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Bed'
        unique_together = (('kid', 'roomnumber', 'bednumber'),)


class Bedallocation(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    pid = models.ForeignKey('Patient', models.DO_NOTHING, db_column='PID', blank=True, null=True)  # Field name made lowercase.
    bid = models.ForeignKey(Bed, models.DO_NOTHING, db_column='BID', blank=True, null=True)  # Field name made lowercase.
    startdate = models.DateTimeField(db_column='StartDate')  # Field name made lowercase.
    enddate = models.DateTimeField(db_column='EndDate', blank=True, null=True)  # Field name made lowercase.
    onusing = models.IntegerField(db_column='OnUsing')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BedAllocation'


class Patient(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    pname = models.CharField(db_column='PName', max_length=50, db_collation='Chinese_PRC_CI_AS')  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=2, db_collation='Chinese_PRC_CI_AS')  # Field name made lowercase.
    pdate = models.DateTimeField(db_column='PDate')  # Field name made lowercase.
    kid = models.ForeignKey('Keshi', models.DO_NOTHING, db_column='KID', blank=True, null=True)  # Field name made lowercase.
    condition = models.TextField(db_column='Condition', db_collation='Chinese_PRC_CI_AS', blank=True, null=True)  # Field name made lowercase.
    did = models.ForeignKey('Dr', models.DO_NOTHING, db_column='DID', blank=True, null=True)  # Field name made lowercase.
    roomnumber = models.CharField(db_column='RoomNumber', max_length=20, db_collation='Chinese_PRC_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bednumber = models.CharField(db_column='BedNumber', max_length=20, db_collation='Chinese_PRC_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Patient'
