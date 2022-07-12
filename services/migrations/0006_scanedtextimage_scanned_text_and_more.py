# Generated by Django 4.0.5 on 2022-06-26 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0005_alter_translatetext_translate_to'),
    ]

    operations = [
        migrations.AddField(
            model_name='scanedtextimage',
            name='scanned_text',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='translatetext',
            name='translated_text',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='translatetext',
            name='translate_to',
            field=models.CharField(choices=[('es', 'Spanish'), ('fr', 'French'), ('gm', 'German')], max_length=100),
        ),
    ]