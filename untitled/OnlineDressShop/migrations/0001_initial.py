# Generated by Django 2.0.9 on 2023-11-21 18:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='dress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dressname', models.CharField(max_length=200)),
                ('dressphoto', models.CharField(max_length=200)),
                ('dressprice', models.CharField(max_length=200)),
                ('details', models.CharField(max_length=200)),
                ('count', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='dress_category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('usertype', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=200)),
                ('housename', models.CharField(max_length=200)),
                ('place', models.CharField(max_length=200)),
                ('post', models.CharField(max_length=200)),
                ('pincode', models.CharField(max_length=200)),
                ('paymentstatus', models.CharField(max_length=200)),
                ('paymentdate', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='order_sub',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.CharField(max_length=200)),
                ('DRESS', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='OnlineDressShop.dress')),
                ('ORDER', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='OnlineDressShop.order')),
            ],
        ),
        migrations.CreateModel(
            name='rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ratings', models.CharField(max_length=200)),
                ('date', models.CharField(max_length=200)),
                ('DRESS', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='OnlineDressShop.dress')),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('phonenumber', models.BigIntegerField()),
                ('LOGIN', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='OnlineDressShop.login')),
            ],
        ),
        migrations.AddField(
            model_name='rating',
            name='USER',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='OnlineDressShop.user'),
        ),
        migrations.AddField(
            model_name='order',
            name='USER',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='OnlineDressShop.user'),
        ),
        migrations.AddField(
            model_name='dress',
            name='DRESS_CATEGORY',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='OnlineDressShop.dress_category'),
        ),
        migrations.AddField(
            model_name='cart',
            name='DRESS',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='OnlineDressShop.dress'),
        ),
        migrations.AddField(
            model_name='cart',
            name='USER',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='OnlineDressShop.user'),
        ),
    ]