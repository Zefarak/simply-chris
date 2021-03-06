# Generated by Django 2.0.7 on 2019-06-02 10:08

from django.db import migrations, models
import sample_templates.models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('sample_templates', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='templatesample',
            name='image',
            field=models.ImageField(blank=True, help_text='400*400', upload_to=sample_templates.models.upload_image_location, validators=[sample_templates.models.validate_image_size]),
        ),
        migrations.AddField(
            model_name='templatesample',
            name='notes',
            field=tinymce.models.HTMLField(blank=True),
        ),
    ]
