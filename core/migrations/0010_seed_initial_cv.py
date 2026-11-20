from django.db import migrations


def seed_initial_active_cv(apps, schema_editor):
    CurriculumVitae = apps.get_model('core', 'CurriculumVitae')
    # If no CV exists, create the initial active CV record pointing to the real file
    if not CurriculumVitae.objects.exists():
        CurriculumVitae.objects.create(
            title='Bhuwan Raj Pandey - Professional CV (BIT / Python & AI)',
            pdf_file='cv/Bhuwan_Raj_Pandey_CV.pdf',
            is_active=True,
            notes='Initial professional CV seeded from academic profile.'
        )


def remove_initial_active_cv(apps, schema_editor):
    CurriculumVitae = apps.get_model('core', 'CurriculumVitae')
    CurriculumVitae.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_contactmessage_curriculumvitae'),
    ]

    operations = [
        migrations.RunPython(seed_initial_active_cv, remove_initial_active_cv),
    ]
