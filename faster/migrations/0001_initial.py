# Generated by Django 3.2.23 on 2023-12-03 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=254)),
                ('Subject', models.CharField(max_length=100)),
                ('Message', models.TextField(max_length=250)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=254)),
                ('Subject', models.CharField(max_length=100)),
                ('Message', models.TextField(max_length=250)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Customer_Name', models.CharField(max_length=50)),
                ('Origin', models.CharField(max_length=100)),
                ('Destination', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=254)),
                ('Payment', models.CharField(max_length=1)),
                ('Service', models.CharField(max_length=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sign_In',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=50)),
                ('Password', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Sign_Up',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=50)),
                ('Password', models.CharField(max_length=10)),
                ('Repeat_Password', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=250)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]