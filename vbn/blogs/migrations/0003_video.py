# Generated by Django 2.2.4 on 2019-08-10 08:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_news'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('categories', models.CharField(choices=[('Health', 'health'), ('Education', 'edu'), ('Sports', 'sports'), ('Politics', 'politics')], default='Education', max_length=40)),
                ('content', models.FileField(upload_to='profile_pics', verbose_name="['video/x-msvideo', 'application/pdf', 'video/mp4', 'audio/mpeg', ]")),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]