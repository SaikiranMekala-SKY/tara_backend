# Generated by Django 5.0.4 on 2025-07-01 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payroll', '0002_employeesalaryhistory_children_education_allowance_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeesalaryhistory',
            name='basic_salary',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='employeesalaryhistory',
            name='bonus',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='employeesalaryhistory',
            name='children_education_allowance',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='employeesalaryhistory',
            name='commission',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='employeesalaryhistory',
            name='conveyance_allowance',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='employeesalaryhistory',
            name='hra',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='employeesalaryhistory',
            name='other_earnings',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='employeesalaryhistory',
            name='overtime_allowance',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='employeesalaryhistory',
            name='special_allowance',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='employeesalaryhistory',
            name='transport_allowance',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='employeesalaryhistory',
            name='travelling_allowance',
            field=models.FloatField(default=0),
        ),
    ]
