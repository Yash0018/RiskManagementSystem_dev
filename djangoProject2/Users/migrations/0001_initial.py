# Generated by Django 3.1.7 on 2021-05-16 05:40

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client_Profile',
            fields=[
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('first_name', models.CharField(db_column='First_name', max_length=50)),
                ('last_name', models.CharField(db_column='Last_name', max_length=50)),
                ('phone_number', models.PositiveIntegerField(db_column='Phone_number', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Consultant_Profile',
            fields=[
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('first_name', models.CharField(db_column='First_name', max_length=50)),
                ('last_name', models.CharField(db_column='Last_name', max_length=50)),
                ('phone_number', models.PositiveIntegerField(db_column='Phone_number', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('role_id', models.AutoField(primary_key=True, serialize=False)),
                ('role_name', models.CharField(db_column='role_name', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('event_id', models.AutoField(db_column='event_id', primary_key=True, serialize=False)),
                ('client_id', models.ForeignKey(db_column='Client_ID', on_delete=django.db.models.deletion.CASCADE, to='Users.client_profile')),
                ('consultant_id', models.ForeignKey(db_column='Consultant_ID', on_delete=django.db.models.deletion.CASCADE, to='Users.consultant_profile')),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('document_id', models.AutoField(db_column='document_id', primary_key=True, serialize=False)),
                ('document_name', models.CharField(blank=True, db_column='document_name', max_length=50, null=True)),
                ('path', models.FileField(null=True, upload_to='files/')),
                ('date_uploaded', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('event_id', models.ForeignKey(db_column='Client_ID', on_delete=django.db.models.deletion.CASCADE, to='Users.event')),
            ],
        ),
        migrations.AddField(
            model_name='consultant_profile',
            name='role_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Users.role'),
        ),
        migrations.AddField(
            model_name='client_profile',
            name='role_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Users.role'),
        ),
    ]
