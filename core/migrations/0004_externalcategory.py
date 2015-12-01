# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20151121_2135'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExternalCategory',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=75)),
                ('parent', models.ForeignKey(null=True, to='core.ExternalCategory', blank=True)),
            ],
        ),
    ]
