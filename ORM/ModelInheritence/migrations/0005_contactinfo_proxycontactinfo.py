# Generated by Django 3.0.8 on 2020-07-25 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ModelInheritence', '0004_child_parent_subchild'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=64)),
                ('Email', models.EmailField(max_length=254)),
                ('Address', models.CharField(max_length=264)),
                ('RollNo', models.IntegerField()),
                ('Marks', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ProxyContactInfo',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('ModelInheritence.contactinfo',),
        ),
    ]
