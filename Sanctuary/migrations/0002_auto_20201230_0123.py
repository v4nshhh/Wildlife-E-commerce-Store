# Generated by Django 3.0.8 on 2020-12-29 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sanctuary', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Specie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('count', models.IntegerField(default=1)),
            ],
        ),
        migrations.AddField(
            model_name='bookingform',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]