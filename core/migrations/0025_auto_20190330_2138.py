# Generated by Django 2.1.7 on 2019-03-30 21:38

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_matchheadline'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('amount', models.FloatField()),
                ('text', models.TextField()),
            ],
            options={
                'db_table': 'transactions',
            },
        ),
        migrations.AddField(
            model_name='customuser',
            name='balance',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='customuser',
            name='paypal_email',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='withdraw_processing',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='transactions',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.CustomUser'),
        ),
        migrations.RunSQL(
            """
CREATE OR REPLACE FUNCTION update_user_balance()
  RETURNS TRIGGER AS $$
DECLARE
    v_rec record;
BEGIN 
    select *
      into v_rec
      from users
     where id = NEW.user_id
       for update;

    update users
       set balance = balance + NEW.amount
     where id = NEW.user_id;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;
            """,
            """DROP FUNCTION update_user_balance();"""
        ),
        migrations.RunSQL(
            """
CREATE TRIGGER trg_update_user_balance
AFTER INSERT ON transactions
FOR EACH ROW EXECUTE PROCEDURE update_user_balance();
            """,
            """DROP TRIGGER trg_update_user_balance ON transactions;"""
        ),
    ]
