# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-25 04:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Games',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_id', models.IntegerField(db_column='Game_ID')),
                ('description', models.TextField(blank=True, db_column='Description', null=True)),
                ('image', models.TextField(blank=True, db_column='Image', null=True)),
                ('max_players', models.IntegerField(blank=True, db_column='Max_players', null=True)),
                ('min_age', models.IntegerField(blank=True, db_column='Min_age', null=True)),
                ('min_players', models.IntegerField(blank=True, db_column='Min_players', null=True)),
                ('name', models.TextField(blank=True, db_column='Name', null=True)),
                ('playing_time', models.IntegerField(blank=True, db_column='Playing_time', null=True)),
                ('year_published', models.IntegerField(blank=True, db_column='Year_published', null=True)),
                ('boardgame_artist', models.TextField(blank=True, db_column='Boardgame_artist', null=True)),
                ('category', models.TextField(blank=True, db_column='Category', null=True)),
                ('designer', models.TextField(blank=True, db_column='Designer', null=True)),
                ('boardgame_family', models.TextField(blank=True, db_column='Boardgame_family', null=True)),
                ('implementation', models.TextField(blank=True, db_column='Implementation', null=True)),
                ('integration', models.TextField(blank=True, db_column='Integration', null=True)),
                ('mechanics', models.TextField(blank=True, db_column='Mechanics', null=True)),
                ('publisher', models.TextField(blank=True, db_column='Publisher', null=True)),
                ('rating', models.FloatField(blank=True, db_column='Rating', null=True)),
                ('language_dependence', models.TextField(blank=True, db_column='Language_dependence', null=True)),
                ('suggested_numplayers_1', models.TextField(blank=True, db_column='Suggested_numplayers.1', null=True)),
                ('suggested_numplayers_10', models.TextField(blank=True, db_column='Suggested_numplayers.10', null=True)),
                ('suggested_numplayers_2', models.TextField(blank=True, db_column='Suggested_numplayers.2', null=True)),
                ('suggested_numplayers_3', models.TextField(blank=True, db_column='Suggested_numplayers.3', null=True)),
                ('suggested_numplayers_4', models.TextField(blank=True, db_column='Suggested_numplayers.4', null=True)),
                ('suggested_numplayers_5', models.TextField(blank=True, db_column='Suggested_numplayers.5', null=True)),
                ('suggested_numplayers_6', models.TextField(blank=True, db_column='Suggested_numplayers.6', null=True)),
                ('suggested_numplayers_7', models.TextField(blank=True, db_column='Suggested_numplayers.7', null=True)),
                ('suggested_numplayers_8', models.TextField(blank=True, db_column='Suggested_numplayers.8', null=True)),
                ('suggested_numplayers_9', models.TextField(blank=True, db_column='Suggested_numplayers.9', null=True)),
                ('suggested_numplayers_over', models.TextField(blank=True, db_column='Suggested_numplayers.Over', null=True)),
                ('suggested_player_age', models.TextField(blank=True, db_column='Suggested_player_age', null=True)),
            ],
        ),
    ]
