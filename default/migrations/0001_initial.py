# Generated by Django 2.1.3 on 2019-03-27 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='選填標題')),
                ('count', models.IntegerField(verbose_name='票數')),
                ('poll_id', models.IntegerField(verbose_name='投票主題')),
            ],
        ),
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=250, verbose_name='投票主題')),
                ('date_created', models.DateField(auto_now_add=True, verbose_name='建立目標')),
            ],
        ),
    ]
