# Generated by Django 2.0.2 on 2018-05-03 06:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('home_score', models.PositiveIntegerField(default=0)),
                ('opponent_score', models.PositiveIntegerField(default=0)),
                ('total_games', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('games_played', models.IntegerField(default=0)),
                ('games_won', models.IntegerField(default=0)),
                ('win_ratio', models.DecimalField(decimal_places=2, default=0, max_digits=50)),
            ],
        ),
        migrations.CreateModel(
            name='PlayerSeason',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('games_played', models.PositiveIntegerField(default=0)),
                ('games_won', models.PositiveIntegerField(default=0)),
                ('win_ratio', models.DecimalField(decimal_places=2, default=0, max_digits=50)),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backgammon.Player')),
            ],
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True)),
                ('active', models.BooleanField(default=True)),
                ('minimum_games', models.IntegerField(default=30)),
                ('date_start', models.DateField()),
                ('date_end', models.DateField()),
                ('winner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='backgammon.Player')),
            ],
        ),
        migrations.AddField(
            model_name='playerseason',
            name='season',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backgammon.Season'),
        ),
        migrations.AddField(
            model_name='game',
            name='home',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='home_player', to='backgammon.PlayerSeason'),
        ),
        migrations.AddField(
            model_name='game',
            name='opponent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='opponent', to='backgammon.PlayerSeason'),
        ),
        migrations.AddField(
            model_name='game',
            name='season',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='backgammon.Season'),
        ),
    ]
