# Generated by Django 3.2.6 on 2021-10-19 07:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0008_auto_20211017_1759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='review',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tag', to='board.review'),
        ),
    ]
