# Generated by Django 2.1.7 on 2019-05-21 20:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0044_matchnotification'),
    ]

    operations = [
        migrations.AddField(
            model_name='matchnotification',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.CustomUser'),
        ),
    ]
