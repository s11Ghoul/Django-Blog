# Generated by Django 4.0.2 on 2022-12-28 19:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0006_reply'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reply',
            name='post',
        ),
        migrations.AlterField(
            model_name='reply',
            name='comment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='post.comment'),
        ),
    ]