# Generated by Django 3.2.6 on 2021-09-06 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='biz_num',
            field=models.CharField(blank=True, db_column='biz_num', max_length=45, null=True),
        ),
    ]
