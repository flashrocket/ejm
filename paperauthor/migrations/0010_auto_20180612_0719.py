# Generated by Django 2.0.2 on 2018-06-12 07:19

import django.core.files.storage
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paperauthor', '0009_paper_submission_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='paper',
            name='all_authors',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='paper',
            name='abstract',
            field=models.TextField(blank=True, max_length=8000),
        ),
        migrations.AlterField(
            model_name='paper',
            name='title',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='paper',
            name='upload',
            field=models.FileField(storage=django.core.files.storage.FileSystemStorage(location='/home/amardhruva/data/project/ejm/protected'), upload_to='', validators=[django.core.validators.FileExtensionValidator(['pdf'])]),
        ),
        migrations.AlterField(
            model_name='paperresubmission',
            name='performed_corrections',
            field=models.FileField(storage=django.core.files.storage.FileSystemStorage(location='/home/amardhruva/data/project/ejm/protected'), upload_to='', validators=[django.core.validators.FileExtensionValidator(['pdf'])]),
        ),
        migrations.AlterField(
            model_name='paperresubmission',
            name='suggested_corrections',
            field=models.FileField(storage=django.core.files.storage.FileSystemStorage(location='/home/amardhruva/data/project/ejm/protected'), upload_to='', validators=[django.core.validators.FileExtensionValidator(['pdf'])]),
        ),
    ]
