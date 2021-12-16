# Generated by Django 3.1.7 on 2021-12-16 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=256)),
                ('cuisines', models.SmallIntegerField(choices=[(1, 'caribbean'), (2, 'vietnamese'), (3, 'korean'), (4, 'indian')])),
                ('avg_cost_for_two', models.DecimalField(decimal_places=3, max_digits=10)),
                ('currency', models.CharField(max_length=50)),
                ('has_table_booking', models.BooleanField()),
                ('has_online_booking', models.BooleanField()),
                ('agg_rating', models.IntegerField()),
                ('rating_color', models.CharField(max_length=200)),
                ('rating_text', models.CharField(max_length=200)),
                ('votes', models.IntegerField()),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
    ]