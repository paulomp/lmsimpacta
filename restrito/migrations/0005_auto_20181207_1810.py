# Generated by Django 2.1.3 on 2018-12-07 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restrito', '0004_auto_20181205_0848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrega',
            name='status',
            field=models.CharField(blank=True, default='ENTREGUE', max_length=20, null=True),
        ),
    ]