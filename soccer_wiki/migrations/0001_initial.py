# Generated by Django 2.1.7 on 2019-04-02 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SoccerWikiPlayer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('import_id', models.IntegerField(unique=True)),
                ('first_name', models.TextField(null=True)),
                ('second_name', models.TextField(null=True)),
                ('birth_date', models.DateField(null=True)),
                ('height', models.IntegerField(null=True)),
                ('weight', models.IntegerField(null=True)),
                ('image', models.TextField(null=True)),
                ('internal_image_status', models.IntegerField(choices=[(1, 'Unknown'), (2, 'Success'), (3, 'Error')], default=1)),
                ('internal_image_url', models.TextField(null=True)),
            ],
            options={
                'db_table': 'soccer_wiki_players',
            },
        ),
    ]
