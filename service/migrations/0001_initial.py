# Generated by Django 4.0.6 on 2022-07-28 13:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='название')),
                ('description', models.TextField(blank=True, null=True, verbose_name='описание')),
                ('image', models.ImageField(upload_to='', verbose_name='картинка')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='дата изменения')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True, verbose_name='описание')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='дата создания')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='service.post')),
            ],
        ),
    ]
