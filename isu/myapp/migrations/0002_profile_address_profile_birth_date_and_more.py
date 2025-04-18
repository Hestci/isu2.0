# Generated by Django 5.2 on 2025-04-14 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='address',
            field=models.TextField(default='Не указано', verbose_name='Адрес проживания'),
        ),
        migrations.AddField(
            model_name='profile',
            name='birth_date',
            field=models.DateField(default='2000-01-01', verbose_name='Дата рождения'),
        ),
        migrations.AddField(
            model_name='profile',
            name='birth_place',
            field=models.CharField(default='Не указано', max_length=200, verbose_name='Место рождения'),
        ),
        migrations.AddField(
            model_name='profile',
            name='document_type',
            field=models.CharField(choices=[('passport', 'Паспорт'), ('foreign_passport', 'Заграничный паспорт')], default='passport', max_length=20, verbose_name='Тип документа'),
        ),
        migrations.AddField(
            model_name='profile',
            name='education',
            field=models.TextField(blank=True, null=True, verbose_name='Образование'),
        ),
        migrations.AddField(
            model_name='profile',
            name='first_name',
            field=models.CharField(default='Не указано', max_length=100, verbose_name='Имя'),
        ),
        migrations.AddField(
            model_name='profile',
            name='inn',
            field=models.CharField(blank=True, max_length=12, null=True, verbose_name='ИНН'),
        ),
        migrations.AddField(
            model_name='profile',
            name='last_name',
            field=models.CharField(default='Не указано', max_length=100, verbose_name='Фамилия'),
        ),
        migrations.AddField(
            model_name='profile',
            name='middle_name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Отчество'),
        ),
        migrations.AddField(
            model_name='profile',
            name='passport_division_code',
            field=models.CharField(default='000-000', max_length=7, verbose_name='Код подразделения'),
        ),
        migrations.AddField(
            model_name='profile',
            name='passport_issue_date',
            field=models.DateField(default='2000-01-01', verbose_name='Дата выдачи'),
        ),
        migrations.AddField(
            model_name='profile',
            name='passport_issued_by',
            field=models.CharField(default='Не указано', max_length=200, verbose_name='Кем выдан'),
        ),
        migrations.AddField(
            model_name='profile',
            name='passport_number',
            field=models.CharField(default='000000', max_length=6, verbose_name='Номер паспорта'),
        ),
        migrations.AddField(
            model_name='profile',
            name='passport_series',
            field=models.CharField(default='0000', max_length=4, verbose_name='Серия паспорта'),
        ),
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=models.CharField(default='+7 (000) 000-00-00', max_length=20, verbose_name='Номер телефона'),
        ),
        migrations.AddField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='profile_photos/', verbose_name='Фото'),
        ),
        migrations.AddField(
            model_name='profile',
            name='resume',
            field=models.TextField(blank=True, null=True, verbose_name='Резюме'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='role',
            field=models.CharField(choices=[('admin', 'Администратор'), ('teacher', 'Преподаватель'), ('student', 'Студент'), ('guest', 'Гость')], default='guest', max_length=20),
        ),
    ]
