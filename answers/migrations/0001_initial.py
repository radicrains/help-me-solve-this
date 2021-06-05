# Generated by Django 3.2.3 on 2021-05-30 05:00

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('question', '0012_delete_answer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('answer', models.TextField(null=True)),
                ('ansimg', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='answers_user', to=settings.AUTH_USER_MODEL)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers_qn', to='question.question')),
            ],
        ),
    ]