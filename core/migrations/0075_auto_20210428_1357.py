# Generated by Django 2.2 on 2021-04-28 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0074_customuser_moderator'),
    ]

    operations = [
        migrations.RunSQL(
            """update users set name = replace(name, ' ', '_');""",
            """"""
        ),
        migrations.RunSQL(
            """create index users_name_unique on users(lower(name));""",
            """drop index users_name_unique;"""
        )
    ]
