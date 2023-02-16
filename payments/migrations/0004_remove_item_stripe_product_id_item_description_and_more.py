# Generated by Django 4.1.6 on 2023-02-11 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0003_remove_item_description_remove_item_price_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='stripe_product_id',
        ),
        migrations.AddField(
            model_name='item',
            name='description',
            field=models.TextField(default=1, max_length=800, verbose_name='Description'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='price',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(max_length=70, verbose_name='Product Name'),
        ),
        migrations.DeleteModel(
            name='Price',
        ),
    ]
