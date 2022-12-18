# Generated by Django 4.1.4 on 2022-12-08 18:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('name', models.TextField(primary_key=True, serialize=False)),
                ('biografy', models.TextField()),
                ('birthDate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('ISBN', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('subject', models.TextField()),
                ('overview', models.TextField()),
                ('publisher', models.CharField(max_length=50)),
                ('publicationDate', models.DateField(auto_now_add=True)),
                ('lang', models.CharField(choices=[('EN', 'English'), ('FR', 'French'), ('DE', 'German'), ('ES', 'Spanish'), ('IT', 'Italian')], max_length=50)),
                ('authors', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.author')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='author',
            name='books',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.book'),
        ),
    ]
