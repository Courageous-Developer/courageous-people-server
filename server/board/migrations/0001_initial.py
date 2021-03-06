# Generated by Django 3.2.6 on 2021-09-03 10:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(db_column='id', primary_key=True, serialize=False)),
                ('content', models.CharField(blank=True, db_column='content', max_length=200, null=True)),
                ('updt_dt', models.DateTimeField(auto_now=True, db_column='updt_dt')),
                ('insrt_dt', models.DateTimeField(auto_now_add=True, db_column='insrt_dt')),
                ('usage_fg', models.CharField(blank=True, db_column='usage_fg', default='Y', max_length=1, null=True)),
            ],
            options={
                'db_table': 'review',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(db_column='id', primary_key=True, serialize=False)),
                ('tag_content', models.CharField(db_column='tag_content', max_length=200)),
                ('type', models.IntegerField(choices=[(1, 'Product'), (2, 'Bowl')], db_column='type', default=1)),
                ('updt_dt', models.DateTimeField(auto_now=True, db_column='updt_dt')),
                ('insrt_dt', models.DateTimeField(auto_now_add=True, db_column='insrt_dt')),
                ('usage_fg', models.CharField(blank=True, db_column='usage_fg', default='Y', max_length=1, null=True)),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='board.review')),
            ],
            options={
                'db_table': 'tag',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(db_column='id', primary_key=True, serialize=False)),
                ('store_name', models.CharField(db_column='store_name', max_length=45)),
                ('address', models.CharField(db_column='address', max_length=200)),
                ('post', models.CharField(blank=True, db_column='post', max_length=500, null=True)),
                ('picture', models.CharField(blank=True, db_column='picture', max_length=200, null=True)),
                ('biz_num', models.CharField(db_column='biz_num', max_length=45)),
                ('latitude', models.DecimalField(blank=True, db_column='latitude', decimal_places=15, max_digits=18, null=True)),
                ('longitude', models.DecimalField(blank=True, db_column='longitude', decimal_places=15, max_digits=18, null=True)),
                ('updt_dt', models.DateTimeField(auto_now=True, db_column='updt_dt')),
                ('insrt_dt', models.DateTimeField(auto_now_add=True, db_column='insrt_dt')),
                ('usage_fg', models.CharField(blank=True, db_column='usage_fg', default='Y', max_length=1, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'store',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ReviewImg',
            fields=[
                ('id', models.BigAutoField(db_column='id', primary_key=True, serialize=False)),
                ('review_img', models.CharField(blank=True, db_column='review_img', max_length=200, null=True)),
                ('updt_dt', models.DateTimeField(auto_now=True, db_column='updt_dt')),
                ('insrt_dt', models.DateTimeField(auto_now_add=True, db_column='insrt_dt')),
                ('usage_fg', models.CharField(blank=True, db_column='usage_fg', default='Y', max_length=1, null=True)),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='board.review')),
            ],
            options={
                'db_table': 'review_img',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='review',
            name='store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='board.store'),
        ),
        migrations.AddField(
            model_name='review',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(db_column='id', primary_key=True, serialize=False)),
                ('menu', models.CharField(db_column='menu', max_length=45)),
                ('updt_dt', models.DateTimeField(auto_now=True, db_column='updt_dt')),
                ('insrt_dt', models.DateTimeField(auto_now_add=True, db_column='insrt_dt')),
                ('usage_fg', models.CharField(blank=True, db_column='usage_fg', default='Y', max_length=1, null=True)),
                ('store', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='board.store')),
            ],
            options={
                'db_table': 'menu',
                'managed': True,
            },
        ),
    ]
