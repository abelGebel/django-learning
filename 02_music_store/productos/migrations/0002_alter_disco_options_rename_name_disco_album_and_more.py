# Generated by Django 4.1.7 on 2023-03-25 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='disco',
            options={'ordering': ['-created'], 'verbose_name': 'disco', 'verbose_name_plural': 'discos'},
        ),
        migrations.RenameField(
            model_name='disco',
            old_name='name',
            new_name='album',
        ),
        migrations.RemoveField(
            model_name='disco',
            name='description',
        ),
        migrations.AddField(
            model_name='disco',
            name='band',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='disco',
            name='price',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='disco',
            name='image',
            field=models.ImageField(upload_to='discos', verbose_name='image'),
        ),
    ]
