# Generated by Django 5.0.4 on 2025-06-26 14:55

import django.db.models.deletion
import docwallet.models
import gst.helpers
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('servicetasks', '0001_initial'),
        ('usermanagement', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BasicBusinessInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_type', models.CharField(default='GST', editable=False, max_length=20)),
                ('legal_name_of_business', models.CharField(blank=True, max_length=255)),
                ('trade_name_of_business', models.CharField(blank=True, max_length=255)),
                ('business_pan', models.FileField(blank=True, null=True, storage=docwallet.models.PrivateS3Storage(), upload_to=gst.helpers.upload_business_pan)),
                ('constitution_of_business', models.CharField(blank=True, max_length=255, null=True)),
                ('certificate_of_incorporation', models.FileField(blank=True, null=True, storage=docwallet.models.PrivateS3Storage(), upload_to=gst.helpers.upload_certificate_of_incorporation)),
                ('MOA_AOA', models.FileField(blank=True, null=True, storage=docwallet.models.PrivateS3Storage(), upload_to=gst.helpers.upload_moa_aoa)),
                ('business_commencement_date', models.DateField()),
                ('nature_of_business', models.TextField(blank=True, null=True)),
                ('email_address', models.EmailField(blank=True, max_length=254, null=True)),
                ('mobile_number', models.CharField(blank=True, max_length=15, null=True)),
                ('status', models.CharField(choices=[('in progress', 'In Progress'), ('completed', 'Completed'), ('sent for approval', 'Sent for Approval'), ('revoked', 'Revoked')], default='in progress', max_length=20)),
                ('assignee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assigned_basic_business_info', to=settings.AUTH_USER_MODEL)),
                ('reviewer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reviewed_basic_business_info', to=settings.AUTH_USER_MODEL)),
                ('service_request', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='basic_business_info', to='usermanagement.servicerequest')),
                ('service_task', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='service_task_basic_business_info', to='servicetasks.servicetask')),
            ],
        ),
        migrations.CreateModel(
            name='GSTReviewFilingCertificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_type', models.CharField(default='GST', editable=False, max_length=20)),
                ('review_certificate', models.FileField(blank=True, null=True, storage=docwallet.models.PrivateS3Storage(), upload_to=gst.helpers.review_filing_certificate)),
                ('status', models.CharField(choices=[('in progress', 'In Progress'), ('completed', 'Completed'), ('sent for approval', 'Sent for Approval'), ('revoked', 'Revoked')], default='in progress', max_length=20)),
                ('draft_filing_certificate', models.FileField(blank=True, null=True, storage=docwallet.models.PrivateS3Storage(), upload_to=gst.helpers.draft_filing_certificate)),
                ('review_certificate_status', models.CharField(blank=True, choices=[('in progress', 'In Progress'), ('completed', 'Completed'), ('sent for approval', 'Sent for Approval'), ('revoked', 'Revoked')], default=None, max_length=20, null=True)),
                ('filing_status', models.CharField(blank=True, choices=[('in progress', 'In Progress'), ('filed', 'Filed'), ('sent for approval', 'Sent for Approval'), ('resubmitted', 'Resubmitted')], default=None, max_length=20, null=True)),
                ('approval_status', models.CharField(blank=True, choices=[('pending', 'Pending'), ('resubmission', 'Resubmission'), ('sent for approval', 'Sent for Approval'), ('rejected', 'Rejected'), ('approved', 'Approved')], default=None, max_length=20, null=True)),
                ('assignee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assigned_gst_review_filing_certificate', to=settings.AUTH_USER_MODEL)),
                ('reviewer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reviewed_gst_review_filing_certificate', to=settings.AUTH_USER_MODEL)),
                ('service_request', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='GST_review_filing_certificate', to='usermanagement.servicerequest')),
                ('service_task', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='ServiceTask_GST_review_filing_certificate', to='servicetasks.servicetask')),
            ],
        ),
        migrations.CreateModel(
            name='PrincipalPlaceDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_type', models.CharField(default='GST', editable=False, max_length=20)),
                ('principal_place', models.JSONField(blank=True, default=dict, null=True)),
                ('nature_of_possession_of_premise', models.CharField(blank=True, choices=[('own', 'Own'), ('rented', 'Rented'), ('leased', 'Leased')], max_length=255, null=True)),
                ('address_proof', models.CharField(blank=True, choices=[('Electricity Bill', 'Electricity Bill'), ('Lease deed/Rental agreement', 'Lease Deed/Rental Agreement'), ('Property tax receipt', 'Property Tax Receipt')], max_length=255, null=True)),
                ('address_proof_file', models.FileField(blank=True, null=True, storage=docwallet.models.PrivateS3Storage(), upload_to=gst.helpers.upload_address_proof_file)),
                ('rental_agreement_or_noc', models.FileField(blank=True, null=True, storage=docwallet.models.PrivateS3Storage(), upload_to=gst.helpers.upload_rental_agreement)),
                ('bank_statement_or_cancelled_cheque', models.FileField(blank=True, null=True, storage=docwallet.models.PrivateS3Storage(), upload_to=gst.helpers.upload_bank_statement)),
                ('status', models.CharField(choices=[('in progress', 'In Progress'), ('completed', 'Completed'), ('sent for approval', 'Sent for Approval'), ('revoked', 'Revoked')], default='in progress', max_length=20)),
                ('assignee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assigned_principal_place_details', to=settings.AUTH_USER_MODEL)),
                ('reviewer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reviewed_principal_place_details', to=settings.AUTH_USER_MODEL)),
                ('service_request', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='principal_place_details', to='usermanagement.servicerequest')),
                ('service_task', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='service_task_principal_place_details', to='servicetasks.servicetask')),
            ],
        ),
        migrations.CreateModel(
            name='PromoterSignatoryDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_type', models.CharField(default='GST', editable=False, max_length=20)),
                ('status', models.CharField(choices=[('in progress', 'In Progress'), ('completed', 'Completed'), ('sent for approval', 'Sent for Approval'), ('revoked', 'Revoked')], default='in progress', max_length=20)),
                ('assignee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assigned_promoter_signatory_details', to=settings.AUTH_USER_MODEL)),
                ('reviewer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reviewed_promoter_signatory_details', to=settings.AUTH_USER_MODEL)),
                ('service_request', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='promoter_signatory_details', to='usermanagement.servicerequest')),
                ('service_task', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='service_task_promoter_signatory_details', to='servicetasks.servicetask')),
            ],
        ),
        migrations.CreateModel(
            name='PromoterSignatoryInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('gender', models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], max_length=10)),
                ('mobile', models.CharField(blank=True, max_length=15, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('pan', models.FileField(blank=True, null=True, storage=docwallet.models.PrivateS3Storage(), upload_to=gst.helpers.upload_promoter_pan)),
                ('aadhaar', models.FileField(blank=True, null=True, storage=docwallet.models.PrivateS3Storage(), upload_to=gst.helpers.upload_promoter_aadhaar)),
                ('photo', models.FileField(blank=True, null=True, storage=docwallet.models.PrivateS3Storage(), upload_to=gst.helpers.upload_promoter_photo)),
                ('designation', models.CharField(blank=True, max_length=255, null=True)),
                ('residential_same_as_aadhaar_address', models.BooleanField(default=False)),
                ('residential_address', models.TextField(blank=True, null=True)),
                ('promoter_detail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='info_list', to='gst.promotersignatorydetails')),
            ],
        ),
        migrations.CreateModel(
            name='RegistrationInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_type', models.CharField(default='GST', editable=False, max_length=20)),
                ('is_this_voluntary_registration', models.BooleanField(default=False)),
                ('applying_for_casual_taxable_person', models.BooleanField(default=False)),
                ('opting_for_composition_scheme', models.BooleanField(default=False)),
                ('any_existing_registration', models.BooleanField(default=False)),
                ('registration_number', models.CharField(blank=True, max_length=100, null=True)),
                ('date_of_registration', models.DateField(blank=True, null=True)),
                ('status', models.CharField(choices=[('in progress', 'In Progress'), ('completed', 'Completed'), ('sent for approval', 'Sent for Approval'), ('revoked', 'Revoked')], default='in progress', max_length=20)),
                ('assignee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assigned_registration_info', to=settings.AUTH_USER_MODEL)),
                ('reviewer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reviewed_registration_info', to=settings.AUTH_USER_MODEL)),
                ('service_request', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='registration_info', to='usermanagement.servicerequest')),
                ('service_task', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='service_task_registration_info', to='servicetasks.servicetask')),
            ],
        ),
    ]
