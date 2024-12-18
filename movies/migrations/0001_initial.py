# Generated by Django 5.0.6 on 2024-07-06 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='movies/images')),
                ('trailer', models.FileField(upload_to='movies/trailer')),
                ('video', models.FileField(upload_to='movies/videos')),
                ('published_date', models.DateField()),
                ('genre', models.CharField(choices=[('adventure', 'Adventure'), ('comedy', 'Comedy'), ('crime', 'Crime'), ('fantasy', 'Fantasy'), ('historical', 'Historical'), ('horror', 'Horror'), ('romance', 'Romance'), ('sci-fi', 'Sci-fi'), ('thriller', 'Thriller'), ('western', 'Western'), ('animation', 'Animation'), ('drama', 'Drama'), ('documentary', 'Documentary')], max_length=20)),
                ('isseries', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='MovieList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('type', models.CharField(choices=[('movies', 'Movies'), ('series', 'Series')], max_length=15)),
                ('content', models.ManyToManyField(to='movies.movies')),
            ],
        ),
    ]