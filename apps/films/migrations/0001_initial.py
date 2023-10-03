# Generated by Django 4.2.5 on 2023-09-30 18:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('actors', '0001_initial'),
        ('languages', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('genders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('description', models.TextField()),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('duration', models.PositiveIntegerField(blank=True, null=True)),
                ('average_rating', models.DecimalField(decimal_places=1, default=0, max_digits=2)),
                ('release', models.PositiveIntegerField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='films')),
                ('link', models.URLField(unique=True)),
                ('actors', models.ManyToManyField(blank=True, related_name='films_actor', to='actors.actor')),
                ('genders', models.ManyToManyField(blank=True, related_name='films', to='genders.gender')),
                ('languages', models.ManyToManyField(blank=True, related_name='films', to='languages.language')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='FavoriteFilm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorite_films', to='films.film')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorite_films', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Favorites Films',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews_films', to='films.film')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews_films', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Reviews',
                'unique_together': {('film', 'user')},
            },
        ),
    ]