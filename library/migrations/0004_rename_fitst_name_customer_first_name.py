# Generated by Django 4.1.5 on 2023-02-13 17:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_remove_customer_age_remove_customer_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='fitst_name',
            new_name='first_name',
        ),
    ]