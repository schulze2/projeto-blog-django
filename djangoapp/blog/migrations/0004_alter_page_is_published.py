# Generated by Django 4.2.8 on 2023-12-19 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_page'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='is_published',
            field=models.BooleanField(default=False, help_text='Este campo precisará estar marcadopara a página ser exibida publicamente.'),
        ),
    ]
