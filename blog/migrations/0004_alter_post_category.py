# Generated by Django 4.2.3 on 2023-07-18 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('일반', '일반'), ('질문', '질문'), ('후기', '후기'), ('공지', '공지')], max_length=30),
        ),
    ]
