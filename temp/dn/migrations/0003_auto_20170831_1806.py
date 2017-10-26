# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dn', '0002_mymodel_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mymodel',
            name='id',
        ),
        migrations.AddField(
            model_name='mymodel',
            name='age',
            field=models.IntegerField(default=1, verbose_name=b'\xe5\xb9\xb4\xe9\xbe\x84'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mymodel',
            name='my_id',
            field=models.IntegerField(default=1, verbose_name=b'ID', serialize=False, auto_created=True, primary_key=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='mymodel',
            name='name',
            field=models.CharField(max_length=20, verbose_name=b'\xe5\x90\x8d\xe5\xad\x97'),
        ),
    ]
