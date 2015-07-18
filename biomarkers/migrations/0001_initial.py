# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PlasmidBiomarker',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('pmid', models.IntegerField(verbose_name='PMID')),
                ('transcript', models.CharField(max_length=200)),
                ('ensembl_id', models.CharField(max_length=100)),
                ('biotype', models.CharField(max_length=100)),
                ('direction', models.CharField(max_length=100)),
                ('disease', models.CharField(max_length=200)),
                ('fluid', models.CharField(max_length=100)),
                ('patients', models.CharField(blank=True, max_length=200, null=True)),
                ('controls', models.CharField(blank=True, max_length=100, null=True)),
                ('method', models.CharField(blank=True, max_length=100, null=True)),
                ('primer_f', models.CharField(blank=True, max_length=200, null=True)),
                ('primer_r', models.CharField(blank=True, max_length=200, null=True)),
                ('date_annotated', models.DateField()),
                ('notes', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
