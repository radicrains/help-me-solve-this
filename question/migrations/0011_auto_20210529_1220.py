# Generated by Django 3.2.3 on 2021-05-29 12:20

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('question', '0010_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='ansimg',
            field=cloudinary.models.CloudinaryField(default=1, max_length=255, verbose_name='image'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='answer',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='answers_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers_qn', to='question.question'),
        ),
    ]
