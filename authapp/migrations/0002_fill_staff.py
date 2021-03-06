# Generated by Django 3.0.5 on 2020-05-18 20:10

from django.db import migrations


def forwards_func(apps, schema_editor):
    HoHooUser = apps.get_model('authapp', 'HoHooUser')
    HoHooUser.objects.bulk_create([
        HoHooUser(
            username='ilf_petrov',
            occupation='Авторы',
            first_name='Илья Ильф',
            last_name='Евгений Петров'
        ),
        HoHooUser(
            username='bender_o',
            occupation='Учредитель',
            first_name='Остап',
            middle_name='Ибрагимович',
            last_name='Бендер',
            userpic='userpic/up_bender.jpg',
            public=True
        ),
        HoHooUser(
            username='balag_s',
            occupation='Уполномоченный по копытам',
            first_name='Шура',
            last_name='Балаганов',
            userpic='userpic/up_balag.jpg',
            public=True
        ),
        HoHooUser(
            username='panik_m',
            occupation='Курьер',
            first_name='Михаил',
            middle_name='Самуэлевич',
            last_name='Паниковский',
            userpic='userpic/up_panik.jpg',
            public=True
        ),
    ])


def reverse_func(apps, schema_editor):
    HoHooUser = apps.get_model('authapp', 'HoHooUser')
    HoHooUser.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]
