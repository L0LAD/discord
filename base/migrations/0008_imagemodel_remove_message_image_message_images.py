# Generated by Django 4.1.7 on 2023-03-19 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_remove_room_image_message_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, default=None, null=True, upload_to='')),
                ('name', models.CharField(max_length=200, null=True, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='message',
            name='image',
        ),
        migrations.AddField(
            model_name='message',
            name='images',
            field=models.ManyToManyField(blank=True, related_name='images', to='base.imagemodel'),
        ),
    ]