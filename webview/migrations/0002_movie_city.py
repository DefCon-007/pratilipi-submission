# Generated by Django 2.1.5 on 2019-01-19 09:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webview', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='city',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='city_movie', to='webview.citites'),
            preserve_default=False,
        ),
    ]
