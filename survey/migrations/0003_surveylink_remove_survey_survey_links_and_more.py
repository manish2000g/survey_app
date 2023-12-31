# Generated by Django 4.2.4 on 2023-08-13 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0002_alter_survey_hero_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SurveyLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='survey_images/')),
                ('link', models.URLField()),
            ],
        ),
        migrations.RemoveField(
            model_name='survey',
            name='survey_links',
        ),
        migrations.AddField(
            model_name='survey',
            name='survey_links',
            field=models.ManyToManyField(to='survey.surveylink'),
        ),
    ]
