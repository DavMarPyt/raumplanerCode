# Generated by Django 3.0.7 on 2020-06-29 13:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('planning', '0003_auto_20200629_1157'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='bookedRoom',
        ),
        migrations.AddField(
            model_name='booking',
            name='date',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='planning.Calendar'),
        ),
        migrations.AddField(
            model_name='booking',
            name='slot',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='planning.Timeslot'),
        ),
        migrations.AddField(
            model_name='booking',
            name='space',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='planning.Space'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='planning.User'),
        ),
        migrations.DeleteModel(
            name='BookedRoom',
        ),
    ]
