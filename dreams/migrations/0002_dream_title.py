# Generated by Django 2.2.7 on 2020-03-02 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dreams', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dream',
            name='title',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
