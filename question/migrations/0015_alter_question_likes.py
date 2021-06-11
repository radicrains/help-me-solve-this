# Generated by Django 3.2.4 on 2021-06-11 14:18

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('question', '0014_alter_question_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='likes',
            field=models.ManyToManyField(default='', related_name='qns_post', to=settings.AUTH_USER_MODEL),
        ),
    ]
