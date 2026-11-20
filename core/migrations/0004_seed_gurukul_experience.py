from django.db import migrations


def add_gurukul_experience(apps, schema_editor):
    Experience = apps.get_model('core', 'Experience')

    # Update existing experience orders to keep GURUKUL as top professional experience
    club = Experience.objects.filter(title__icontains='Whitehouse Innovators').first()
    if club:
        club.order = 2
        club.save()

    hackathon = Experience.objects.filter(title__icontains='Sankalpa').first()
    if hackathon:
        hackathon.order = 3
        hackathon.save()

    web = Experience.objects.filter(title__icontains='Web Development Program').first()
    if web:
        web.order = 4
        web.save()

    drone = Experience.objects.filter(title__icontains='Drone Workshop').first()
    if drone:
        drone.order = 5
        drone.save()

    # Add GURUKUL – शिक्षा
    Experience.objects.update_or_create(
        title='GURUKUL – शिक्षा',
        defaults={
            'role': 'Online Educator & entire management handler',
            'institution': 'GURUKUL – शिक्षा',
            'category': 'professional',
            'period': 'Online Education Platform',
            'duration_stats': 'Loksewa and Security Forces Examination Preparation',
            'description': (
                "Working with GURUKUL – शिक्षा, an online educational platform focused on Loksewa "
                "and security forces examination preparation. My responsibilities combine online teaching, "
                "student communication, educational content development, and promotional activities "
                "to attract students to the platform."
            ),
            'responsibilities': (
                "Teaching & Mentorship: Conduct online classes for students preparing for Nepal Army, APF, and Nepal Police examinations.\n"
                "Teaching & Mentorship: Explain academic concepts and examination-related topics.\n"
                "Teaching & Mentorship: Support students in their learning and examination preparation.\n"
                "Student Communication: Communicate with students regarding classes and learning activities.\n"
                "Student Communication: Respond to student questions and provide guidance.\n"
                "Student Communication: Maintain positive student engagement.\n"
                "Content Creation & Promotion: Create educational content and learning materials.\n"
                "Content Creation & Promotion: Prepare social media posts to promote educational programs.\n"
                "Content Creation & Promotion: Develop engaging promotional content to attract prospective students.\n"
                "Content Creation & Promotion: Support the platform's online visibility and student engagement."
            ),
            'skills': (
                "Online Teaching, Communication, Educational Content Creation, Student Engagement, "
                "Social Media Content Development, Presentation Skills, Time Management, Mentorship"
            ),
            'icon': 'bi-mortarboard-fill',
            'order': 1,
        }
    )


def remove_gurukul_experience(apps, schema_editor):
    Experience = apps.get_model('core', 'Experience')
    Experience.objects.filter(title='GURUKUL – शिक्षा').delete()


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_experience_skills_alter_experience_category_and_more'),
    ]

    operations = [
        migrations.RunPython(add_gurukul_experience, remove_gurukul_experience),
    ]
