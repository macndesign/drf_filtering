# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_externalcategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='Association',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('match', models.BooleanField(default=False)),
                ('category', models.ForeignKey(to='core.Category', related_name='categories')),
                ('external_category', models.ForeignKey(to='core.ExternalCategory', related_name='external_categories')),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='match',
            field=models.ManyToManyField(to='core.ExternalCategory', through='core.Association'),
        ),
    ]
