# Generated by Django 3.0.7 on 2020-06-08 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FakeID', '0002_id_phonenumber'),
    ]

    operations = [
        migrations.AddField(
            model_name='id',
            name='address',
            field=models.CharField(max_length=30, null=True, verbose_name='주소'),
        ),
    ]
