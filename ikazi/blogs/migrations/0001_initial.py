# Generated by Django 4.0.5 on 2022-08-07 10:14

import ckeditor.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('blog_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('blog_image', models.ImageField(upload_to='uploads')),
                ('blog_title', models.CharField(max_length=100)),
                ('blog_slug', models.CharField(default='', max_length=100)),
                ('content', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('views', models.IntegerField(default=0)),
                ('rating', models.IntegerField(default=1)),
                ('date_posted', models.DateField(default=django.utils.timezone.now)),
                ('minute_read', models.CharField(default='1 min read', help_text='Minutes taken to read the blog. This will be auto-calculated, no need to fill it', max_length=50)),
            ],
            options={
                'verbose_name': 'Blog',
                'verbose_name_plural': 'Blogs',
            },
        ),
    ]
