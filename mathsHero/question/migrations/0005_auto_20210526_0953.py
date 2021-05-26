# Generated by Django 3.2.3 on 2021-05-26 09:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0004_auto_20210524_1503'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='categories',
        ),
        migrations.AddField(
            model_name='category',
            name='question',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='question.question'),
        ),
    ]
