# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Dr(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    drname = models.CharField(db_column='DrName', max_length=50, db_collation='Chinese_PRC_CI_AS')  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=2, db_collation='Chinese_PRC_CI_AS')  # Field name made lowercase.
    position = models.CharField(db_column='Position', max_length=50, db_collation='Chinese_PRC_CI_AS')  # Field name made lowercase.
    birthdate = models.DateField(db_column='BirthDate')  # Field name made lowercase.
    whentowork = models.DateField(db_column='Whentowork')  # Field name made lowercase.
    joindate = models.DateField(db_column='JoinDate')  # Field name made lowercase.
    salary = models.DecimalField(db_column='Salary', max_digits=10, decimal_places=2)  # Field name made lowercase.
    about = models.CharField(db_column='About', max_length=500, db_collation='Chinese_PRC_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bid = models.ForeignKey('Bumen', models.DO_NOTHING, db_column='BID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Dr'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150, db_collation='Chinese_PRC_CI_AS')

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255, db_collation='Chinese_PRC_CI_AS')
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100, db_collation='Chinese_PRC_CI_AS')

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128, db_collation='Chinese_PRC_CI_AS')
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150, db_collation='Chinese_PRC_CI_AS')
    first_name = models.CharField(max_length=150, db_collation='Chinese_PRC_CI_AS')
    last_name = models.CharField(max_length=150, db_collation='Chinese_PRC_CI_AS')
    email = models.CharField(max_length=254, db_collation='Chinese_PRC_CI_AS')
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Bumen(models.Model):
    bid = models.CharField(db_column='BID', primary_key=True, max_length=20, db_collation='Chinese_PRC_CI_AS')  # Field name made lowercase.
    bname = models.CharField(db_column='BName', unique=True, max_length=50, db_collation='Chinese_PRC_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bumen'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100, db_collation='Chinese_PRC_CI_AS')
    model = models.CharField(max_length=100, db_collation='Chinese_PRC_CI_AS')

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255, db_collation='Chinese_PRC_CI_AS')
    name = models.CharField(max_length=255, db_collation='Chinese_PRC_CI_AS')
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40, db_collation='Chinese_PRC_CI_AS')
    session_data = models.TextField(db_collation='Chinese_PRC_CI_AS')
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Keshi(models.Model):
    kid = models.CharField(db_column='KID', primary_key=True, max_length=20, db_collation='Chinese_PRC_CI_AS')  # Field name made lowercase.
    kname = models.CharField(db_column='KName', unique=True, max_length=50, db_collation='Chinese_PRC_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'keshi'


class Uer(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    pass_word = models.CharField(db_column='Pass_word', max_length=50, db_collation='Chinese_PRC_CI_AS')  # Field name made lowercase.
    username = models.CharField(db_column='UserName', unique=True, max_length=50, db_collation='Chinese_PRC_CI_AS')  # Field name made lowercase.
    is_staff = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'uer'
