from django.db import models
from django.utils import timezone
# following is user table that Django has already created and we can use it with other tables
from django.contrib.auth.models import User


# For user table, Django already has user and authentication functionality out of the box.
# WE just use that here and create other table connected to that


# class Role(models.Model):
#     role_id = models.AutoField(primary_key=True, )  # Field name made lowercase.
#     role_name = models.CharField(db_column='role_name', max_length=50)  # Field name made lowercase.
#
#     def __str__(self):
#         return self.role_name


class Client_Profile(models.Model):
    user_id = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)  # Field name made lowercase.
    first_name = models.CharField(db_column='First_name', max_length=50)  # Field name made lowercase.
    last_name = models.CharField(db_column='Last_name', max_length=50)  # Field name made lowercase.
    phone_number = models.PositiveIntegerField(db_column='Phone_number', max_length=10)  # Field name made lowercase.
    # role_id = models.ForeignKey(Role, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name


class Consultant_Profile(models.Model):
    user_id = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)  # Field name made lowercase.
    first_name = models.CharField(db_column='First_name', max_length=50)  # Field name made lowercase.
    last_name = models.CharField(db_column='Last_name', max_length=50)  # Field name made lowercase.
    phone_number = models.PositiveIntegerField(db_column='Phone_number', max_length=10)  # Field name made lowercase.
    # role_id = models.ForeignKey(Role, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name


class Event(models.Model):
    event_id = models.AutoField(db_column='event_id', primary_key=True)
    client_id = models.ForeignKey(Client_Profile, db_column='Client_ID', on_delete=models.CASCADE)  # Field name made lowercase.
    consultant_id = models.ForeignKey(Consultant_Profile, db_column='Consultant_ID', on_delete=models.CASCADE)  # Field name made lowercase.

    def __str__(self):
        return str(self.event_id)


class Document(models.Model):
    document_id = models.AutoField(db_column='document_id', primary_key=True)
    document_name = models.CharField(db_column='document_name', max_length=50, null=True, blank=True)  # Field name made lowercase.
    path = models.FileField(null=True, upload_to='files/')
    date_uploaded = models.DateTimeField(default=timezone.now, null=True, blank=True)
    event_id = models.ForeignKey(Event, db_column='Client_ID', on_delete=models.CASCADE)  # Field name made lowercase.

    def __str__(self):
        return self.document_name + ": " + str(self.path)  # this specifies how should instance of this class should be printed.


