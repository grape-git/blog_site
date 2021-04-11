# Generated by Django 3.1.7 on 2021-04-07 00:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('studyapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('writer', models.CharField(max_length=20)),
                ('email', models.EmailField(blank=True, max_length=50, null=True)),
                ('comment_text', models.TextField()),
                ('create_date', models.DateTimeField(auto_now=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studyapp.post')),
            ],
        ),
    ]
