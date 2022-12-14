# Generated by Django 3.2.15 on 2022-08-28 02:34
"""
        This migration adds the identification of an author to a
        comment.
    """

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    """
        This describes the fourth migration
    """

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0003_comment_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.
                                    deletion.CASCADE,
                                    related_name='post_comment',
                                    to=settings.AUTH_USER_MODEL),
        ),
    ]
