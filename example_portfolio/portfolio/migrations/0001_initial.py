# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import taggit.managers
import filer.fields.folder
import djangocms_text_ckeditor.fields
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('filer', '0007_auto_20161016_1055'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryWork',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(verbose_name='Title', max_length=255)),
                ('slug', models.SlugField()),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(verbose_name='Title', max_length=200)),
                ('slug', models.SlugField()),
                ('pub_date', models.DateTimeField(verbose_name='Published on', auto_now_add=True)),
                ('description', djangocms_text_ckeditor.fields.HTMLField(verbose_name='Work Description')),
                ('client', models.CharField(verbose_name='Client', max_length=255, blank=True, null=True)),
                ('location', models.CharField(verbose_name='Location', max_length=255, blank=True, null=True)),
                ('category', models.ForeignKey(verbose_name='Category', to='portfolio.CategoryWork')),
                ('folder', filer.fields.folder.FilerFolderField(verbose_name='Gallery Folder', blank=True, null=True, to='filer.Folder')),
                ('head_picture', filer.fields.image.FilerImageField(verbose_name='Head', to='filer.Image')),
                ('tags', taggit.managers.TaggableManager(verbose_name='Tags', help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag')),
            ],
            options={
                'verbose_name': 'Work',
                'verbose_name_plural': 'Works',
            },
        ),
    ]
