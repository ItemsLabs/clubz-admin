# Generated by Django 2.2 on 2021-06-22 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0084_auto_20210622_1216'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='subscription_tier',
            field=models.IntegerField(choices=[(0, 'None'), (1, 'Premium'), (2, 'Lite')], default=0),
        ),
        migrations.RunSQL(
            '''update games set subscription_tier = 1 where premium = true;''',
            ''''''
        )
    ]
