# Generated by Django 4.1.5 on 2023-04-07 03:39

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_booking_tour_alter_blogs_post_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='tour',
            name='includesexcludes',
            field=tinymce.models.HTMLField(default=''),
        ),
        migrations.AlterField(
            model_name='tour',
            name='description',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='tour',
            name='noofdays',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='tour',
            name='price',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='tour',
            name='type',
            field=models.CharField(choices=[('Religious', 'Religious'), ('Adventurous', 'Adventurous'), ('Honeymoon', 'Honeymoon'), ('Sports', 'Sports'), ('Medical', 'Medical'), ('Student', 'Student'), ('Wildlife', 'Wildlife'), ('Inbound', 'Inbound'), ('Hill Station', 'Hill Station')], max_length=200),
        ),
    ]
