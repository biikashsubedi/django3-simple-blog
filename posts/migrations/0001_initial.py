# Generated by Django 3.2.6 on 2021-08-28 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('image', models.ImageField(blank=True, default='posts.png', null=True, upload_to='images')),
                ('content', models.TextField()),
                ('createdBy', models.CharField(blank=True, max_length=30, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Post',
                'db_table': 'posts',
            },
        ),
    ]
