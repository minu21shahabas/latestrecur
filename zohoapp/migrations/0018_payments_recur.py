# Generated by Django 4.1.7 on 2023-06-22 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zohoapp', '0017_recur_itemtable_ri'),
    ]

    operations = [
        migrations.CreateModel(
            name='payments_recur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Terms', models.CharField(blank=True, max_length=100, null=True)),
                ('Days', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
