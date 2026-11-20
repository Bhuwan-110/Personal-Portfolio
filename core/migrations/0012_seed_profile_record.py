from django.db import migrations


def seed_bhuwan_profile(apps, schema_editor):
    Profile = apps.get_model('core', 'Profile')

    if not Profile.objects.exists():
        Profile.objects.create(
            full_name='Bhuwan Raj Pandey',
            professional_title='Aspiring Software Developer | Python & AI Enthusiast',
            short_bio=(
                "I am an Information Technology student interested in Python development, "
                "backend technologies, web applications, and Artificial Intelligence. "
                "I enjoy learning new technologies, exploring practical solutions, and developing "
                "my technical skills through academic projects and independent learning.\n\n"
                "I am currently strengthening my Python programming and Object-Oriented Programming "
                "fundamentals while exploring Django and AI technologies. "
                "My long-term ambition is to become an AI Engineer."
            ),
            detailed_bio=(
                "I am an Information Technology student currently pursuing my Bachelor of "
                "Information Technology (BIT) at Himalayan WhiteHouse International College, Kathmandu.\n\n"
                "I have a strong interest in software development, Python programming, backend "
                "technologies, web applications, and Artificial Intelligence. I enjoy exploring "
                "technologies, understanding how systems work, and applying my knowledge through "
                "academic projects and practical learning.\n\n"
                "Throughout my academic journey, I have participated in different technology-related "
                "projects and leadership activities. These experiences have helped me develop teamwork, "
                "coordination, planning, documentation, and problem-solving skills.\n\n"
                "I am currently strengthening my Python fundamentals and Object-Oriented Programming "
                "knowledge while exploring Django and modern software development practices. "
                "My long-term ambition is to become an AI Engineer."
            ),
            profile_photo='profile/profile-picture.png',
            email='officialbhuwan454@gmail.com',
            location='Kathmandu, Nepal',
            phone='',
            linkedin_url='https://www.linkedin.com/in/bhuwan-pandey-2b829a2ba/',
            github_url='https://github.com/Bhuwan-110',
            career_objective=(
                "My immediate goal is to obtain an IT internship where I can apply my programming "
                "knowledge, learn from experienced professionals, and contribute to real-world software "
                "development projects. I am particularly interested in Python development, backend "
                "engineering, and Artificial Intelligence."
            ),
            availability_status='Available for IT Internships',
            institution='Himalayan WhiteHouse International College',
            degree='Bachelor of Information Technology (BIT)',
            current_semester='7th Semester',
            graduation_year='2027 (Expected)',
            is_active=True,
        )


def remove_bhuwan_profile(apps, schema_editor):
    Profile = apps.get_model('core', 'Profile')
    Profile.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_profile_achievement_event_photo_and_more'),
    ]

    operations = [
        migrations.RunPython(seed_bhuwan_profile, remove_bhuwan_profile),
    ]
