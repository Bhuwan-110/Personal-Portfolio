from django.db import migrations


def seed_achievements_and_certificates(apps, schema_editor):
    Achievement = apps.get_model('core', 'Achievement')
    Certificate = apps.get_model('core', 'Certificate')

    # 1. Seed Achievements (PART A)
    achievements_data = [
        {
            'title': 'Sankalpa Hackathon',
            'role': 'Event Head',
            'organization': 'Himalayan WhiteHouse International College',
            'category': 'hackathon',
            'period': '3-Day Hackathon',
            'metrics_summary': '15 Teams | 60 Participants',
            'description': (
                'Contributed to leading and organizing a three-day hackathon focused on '
                'technology and digital problem-solving. Coordinated teams, mentors, and '
                'challenge logistics across all 3 days.'
            ),
            'key_highlights': (
                'Led overall event coordination, scheduling, and logistics for 15 participating teams (60 total participants).\n'
                'Facilitated mentorship sessions, technical judging rubrics, and project showcase presentations.\n'
                'Ensured seamless collaboration between faculty advisory, student committee, and external judges.'
            ),
            'icon': 'bi-trophy-fill',
            'order': 1,
            'featured': True,
        },
        {
            'title': 'Web Development Program',
            'role': 'Main Lead',
            'organization': 'Himalayan WhiteHouse International College',
            'category': 'workshop',
            'period': 'One-Day Program',
            'metrics_summary': 'Hands-on Web Dev Workshop',
            'description': (
                'Led the organization and coordination of a one-day web development program for students, '
                'providing practical foundations in frontend and backend web architecture.'
            ),
            'key_highlights': (
                'Formulated workshop learning flow focusing on HTML5, CSS3, JavaScript, and introductory backend concepts.\n'
                'Coordinated lab computer setups, software environments, and student attendee onboarding.\n'
                'Delivered introductory walkthroughs and guided students through practical mini-projects.'
            ),
            'icon': 'bi-laptop-fill',
            'order': 2,
            'featured': True,
        },
        {
            'title': 'Drone Workshop',
            'role': 'Organizer & Coordinator',
            'organization': 'Himalayan WhiteHouse International College',
            'category': 'workshop',
            'period': 'Technology Workshop',
            'metrics_summary': 'Hardware & UAV Exposure',
            'description': (
                'Organized a technology-focused drone workshop to provide students with exposure to '
                'drone technology, embedded flight hardware, and practical aerospace learning.'
            ),
            'key_highlights': (
                'Organized technical sessions introducing multi-rotor UAV mechanics, flight controllers, and sensors.\n'
                'Facilitated live flight demonstrations and hands-on assembly exploration for participating students.\n'
                'Sparked curiosity for robotics, IoT, and embedded systems within the campus tech community.'
            ),
            'icon': 'bi-compass-fill',
            'order': 3,
            'featured': True,
        },
        {
            'title': 'Whitehouse Innovators – IT Club',
            'role': 'General Secretary (2025) & Vice President (2026)',
            'organization': 'Himalayan WhiteHouse International College',
            'category': 'leadership',
            'period': '2025 – 2026',
            'metrics_summary': 'Executive Club Tenure',
            'description': (
                'Contributed to student technology activities, event coordination, planning, '
                'documentation, and leadership across consecutive tenures.'
            ),
            'key_highlights': (
                'Served as General Secretary in 2025: structured club records, internal documentation, and student outreach.\n'
                'Appointed Vice President in 2026: driving strategic initiatives, hackathons, and technology workshops.\n'
                'Championed collaborative peer learning and connected students with technical industry opportunities.'
            ),
            'icon': 'bi-award-fill',
            'order': 4,
            'featured': True,
        },
    ]

    achievement_instances = {}
    for data in achievements_data:
        ach, _ = Achievement.objects.update_or_create(title=data['title'], defaults=data)
        achievement_instances[data['title']] = ach

    # 2. Seed Certificates (PART B & C)
    # Temporary photos/files are provided for verification as requested; user will replace later via Django Admin
    certificates_data = [
        {
            'title': 'Certificate of Executive Leadership',
            'issuing_organization': 'Whitehouse Innovators – IT Club / HWIC',
            'issue_date_display': '2025 – 2026',
            'description': (
                'Official certificate of executive leadership honoring dedicated service as '
                'General Secretary (2025) and Vice President (2026) of the Whitehouse Innovators IT Club.'
            ),
            'category': 'leadership',
            'certificate_file': 'certificates/certificate_placeholder.png',
            'achievement': achievement_instances.get('Whitehouse Innovators – IT Club'),
            'is_temporary_placeholder': True,
            'order': 1,
            'is_featured': True,
        },
        {
            'title': 'Certificate of Appreciation – Event Head',
            'issuing_organization': 'Himalayan WhiteHouse International College',
            'issue_date_display': '2025',
            'description': (
                'Awarded for outstanding leadership and management as Event Head for the 3-day '
                'Sankalpa Hackathon, coordinating 15 competitive teams and 60 student participants.'
            ),
            'category': 'hackathon',
            'certificate_file': 'certificates/sample_certificate.pdf',
            'achievement': achievement_instances.get('Sankalpa Hackathon'),
            'is_temporary_placeholder': True,
            'order': 2,
            'is_featured': True,
        },
        {
            'title': 'Web Development Program Organizing Lead',
            'issuing_organization': 'Himalayan WhiteHouse International College',
            'issue_date_display': '2025',
            'description': (
                'Recognition for leading the curriculum delivery and operational planning '
                'for the one-day student Web Development Program.'
            ),
            'category': 'workshop',
            'certificate_file': '',  # Demonstrates graceful fallback without certificate file preview
            'achievement': achievement_instances.get('Web Development Program'),
            'is_temporary_placeholder': False,
            'order': 3,
            'is_featured': True,
        },
        {
            'title': 'Drone Workshop Organizing Committee Recognition',
            'issuing_organization': 'Himalayan WhiteHouse International College',
            'issue_date_display': '2025',
            'description': (
                'Recognition for successfully organizing and coordinating the hands-on '
                'Drone Technology Workshop for undergraduate students.'
            ),
            'category': 'workshop',
            'certificate_file': '',  # Demonstrates graceful fallback without certificate file preview
            'achievement': achievement_instances.get('Drone Workshop'),
            'is_temporary_placeholder': False,
            'order': 4,
            'is_featured': True,
        },
    ]

    for c_data in certificates_data:
        Certificate.objects.update_or_create(title=c_data['title'], defaults=c_data)


def remove_achievements_and_certificates(apps, schema_editor):
    Achievement = apps.get_model('core', 'Achievement')
    Certificate = apps.get_model('core', 'Certificate')
    Certificate.objects.all().delete()
    Achievement.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_achievement_certificate'),
    ]

    operations = [
        migrations.RunPython(seed_achievements_and_certificates, remove_achievements_and_certificates),
    ]
