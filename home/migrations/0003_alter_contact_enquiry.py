# Generated by Django 4.2 on 2023-05-13 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_remove_contact_option1_remove_contact_option2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='enquiry',
            field=models.TextField(),
        ),
    ]