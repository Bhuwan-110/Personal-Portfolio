import os
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.http import FileResponse, Http404
from django.shortcuts import get_object_or_404, redirect, render
from .forms import ContactForm
from .models import (
    Achievement, Certificate, ContactMessage, CurriculumVitae,
    Experience, LearningGoal, Profile, Project, ProjectScreenshot, Skill
)


def home(request):
    """
    Renders the professional portfolio homepage for Bhuwan Raj Pandey.
    Passes personal background, education, technical interests, featured projects, and contact info.
    Dynamically loads from the active Profile model with fallback to defaults.
    """
    active_profile = Profile.get_active_profile()

    personal_info = {
        'name': active_profile.full_name if active_profile else 'Bhuwan Raj Pandey',
        'title': active_profile.professional_title if active_profile else 'Aspiring Software Developer | Python & AI Enthusiast',
        'location': active_profile.location if active_profile else 'Kathmandu, Nepal',
        'email': active_profile.email if active_profile else 'officialbhuwan454@gmail.com',
        'linkedin': active_profile.linkedin_url if active_profile else 'https://www.linkedin.com/in/bhuwan-pandey-2b829a2ba/',
        'github': active_profile.github_url if active_profile else 'https://github.com/Bhuwan-110',
        'education': {
            'degree': active_profile.degree if active_profile else 'Bachelor of Information Technology (BIT)',
            'institution': active_profile.institution if active_profile else 'Himalayan WhiteHouse International College',
            'graduation_year': active_profile.graduation_year if active_profile else '2027 (Expected)',
            'current_status': active_profile.current_semester if active_profile else '7th Semester',
            'focus': 'Software Development, Object-Oriented Programming & AI Fundamentals',
        },
        'intro_paragraphs': active_profile.get_short_bio_paragraphs() if (active_profile and active_profile.short_bio) else [
            (
                "I am an Information Technology student interested in Python development, "
                "backend technologies, web applications, and Artificial Intelligence. "
                "I enjoy learning new technologies, exploring practical solutions, and developing "
                "my technical skills through academic projects and independent learning."
            ),
            (
                "I am currently strengthening my Python programming and Object-Oriented Programming "
                "fundamentals while exploring Django and AI technologies. "
                "My long-term ambition is to become an AI Engineer."
            ),
        ],
        'status': active_profile.availability_status if active_profile else 'Available for IT Internships',
    }

    featured_projects_qs = Project.objects.filter(is_published=True).order_by('order', 'id')[:4]

    context = {
        'page_title': f"{personal_info['name']} | Aspiring Software Developer & AI Enthusiast",
        'personal_info': personal_info,
        'profile': active_profile,
        'technical_interests': [
            {
                'title': 'Python Development',
                'icon': 'bi-filetype-py',
                'summary': (
                    'Strengthening core Python 3 and Object-Oriented Programming fundamentals, '
                    'data structures, modular design, and clean algorithmic problem-solving.'
                ),
                'topics': ['Python 3', 'OOP Concepts', 'Data Structures', 'Clean Code'],
            },
            {
                'title': 'Backend Development',
                'icon': 'bi-hdd-stack-fill',
                'summary': (
                    'Building reliable server-side architectures, database schemas, routing, '
                    'and RESTful services utilizing the Django web framework.'
                ),
                'topics': ['Django', 'SQLite', 'RESTful APIs', 'MVC Architecture'],
            },
            {
                'title': 'Web Technologies',
                'icon': 'bi-window-fullscreen',
                'summary': (
                    'Creating clean, responsive, and accessible user interfaces using semantic HTML5, '
                    'CSS3 design systems, JavaScript, and Bootstrap 5.'
                ),
                'topics': ['HTML5 / CSS3', 'JavaScript', 'Bootstrap 5', 'Responsive Design'],
            },
            {
                'title': 'Artificial Intelligence',
                'icon': 'bi-cpu-fill',
                'summary': (
                    'Exploring machine learning fundamentals, data processing with NumPy and Pandas, '
                    'and pursuing a dedicated ambition toward AI engineering.'
                ),
                'topics': ['Machine Learning', 'Data Analysis', 'NumPy & Pandas', 'AI Ambition'],
            },
        ],
        'featured_projects': featured_projects_qs,
    }
    return render(request, 'core/home.html', context)


def about(request):
    """
    Renders the dedicated About and Education page for Bhuwan Raj Pandey.
    Provides detailed academic trajectory, career objectives, strengths, and areas of exploration.
    Dynamically loads from the active Profile model with fallback to defaults.
    """
    active_profile = Profile.get_active_profile()

    personal_info = {
        'name': active_profile.full_name if active_profile else 'Bhuwan Raj Pandey',
        'title': active_profile.professional_title if active_profile else 'Aspiring Software Developer | Python & AI Enthusiast',
        'location': active_profile.location if active_profile else 'Putalisadak, Kathmandu, Nepal',
        'email': active_profile.email if active_profile else 'officialbhuwan454@gmail.com',
        'linkedin': active_profile.linkedin_url if active_profile else 'https://www.linkedin.com/in/bhuwan-pandey-2b829a2ba/',
        'github': active_profile.github_url if active_profile else 'https://github.com/Bhuwan-110',
        'status': active_profile.availability_status if active_profile else 'Available for IT Internships',
        'about_paragraphs': active_profile.get_about_paragraphs() if (active_profile and active_profile.detailed_bio) else [
            (
                "I am an Information Technology student currently pursuing my Bachelor of "
                "Information Technology (BIT) at Himalayan WhiteHouse International College, Kathmandu."
            ),
            (
                "I have a strong interest in software development, Python programming, backend "
                "technologies, web applications, and Artificial Intelligence. I enjoy exploring "
                "technologies, understanding how systems work, and applying my knowledge through "
                "academic projects and practical learning."
            ),
            (
                "Throughout my academic journey, I have participated in different technology-related "
                "projects and leadership activities. These experiences have helped me develop teamwork, "
                "coordination, planning, documentation, and problem-solving skills."
            ),
            (
                "I am currently strengthening my Python fundamentals and Object-Oriented Programming "
                "knowledge while exploring Django and modern software development practices. "
                "My long-term ambition is to become an AI Engineer."
            ),
        ],
    }

    career_objective = active_profile.career_objective if (active_profile and active_profile.career_objective) else (
        "My immediate goal is to obtain an IT internship where I can apply my programming "
        "knowledge, learn from experienced professionals, and contribute to real-world software "
        "development projects. I am particularly interested in Python development, backend "
        "engineering, and Artificial Intelligence."
    )

    institution = active_profile.institution if active_profile else 'Himalayan WhiteHouse International College'
    degree = active_profile.degree if active_profile else 'Bachelor of Information Technology (BIT)'
    current_status = active_profile.current_semester if active_profile else '7th Semester'
    graduation_year = active_profile.graduation_year if active_profile else '2027 (Expected)'

    context = {
        'page_title': f"About Me & Education | {personal_info['name']}",
        'personal_info': personal_info,
        'profile': active_profile,
        'career_objective': career_objective,
        'education_timeline': [
            {
                'degree': degree,
                'institution': institution,
                'location': 'Putalisadak, Kathmandu, Nepal',
                'current_status': current_status,
                'graduation_year': graduation_year,
                'badge': 'Currently Enrolled',
                'highlights': [
                    'Focus on Software Engineering principles, OOP architecture, and relational database systems.',
                    'Actively designing academic projects in Python, Django web backend, and responsive frontends.',
                    'Participating in college tech activities, teamwork collaborations, and code reviews.',
                ],
            },
        ],
        'personal_strengths': [
            {
                'title': 'Responsible and Disciplined',
                'icon': 'bi-shield-check',
                'description': 'Reliable execution of academic and project milestones with high personal accountability and structured work habits.',
            },
            {
                'title': 'Team Collaboration',
                'icon': 'bi-people-fill',
                'description': 'Effective team contributor experienced in pair programming, peer collaboration, and shared project ownership.',
            },
            {
                'title': 'Willingness to Learn',
                'icon': 'bi-book-half',
                'description': 'Proactive curiosity to research documentation, master modern frameworks, and incorporate professional feedback.',
            },
            {
                'title': 'Problem-Solving',
                'icon': 'bi-puzzle-fill',
                'description': 'Analytical mindset focused on decomposing challenges into clean, logical, and testable algorithmic solutions.',
            },
            {
                'title': 'Planning and Coordination',
                'icon': 'bi-calendar-check-fill',
                'description': 'Organized approach to task scheduling, resource planning, and timeline management in group environments.',
            },
            {
                'title': 'Communication and Documentation',
                'icon': 'bi-file-earmark-text-fill',
                'description': 'Committed to writing clear technical documentation, readable code comments, and delivering effective project walk-throughs.',
            },
        ],
        'career_interests': [
            {
                'title': 'Python Development',
                'icon': 'bi-filetype-py',
                'is_exploring': False,
                'category_label': 'Core Focus',
                'category_class': 'badge bg-primary-subtle text-primary border border-primary-subtle',
                'description': 'Writing clean, idiomatic Python code, applying Object-Oriented principles, and implementing algorithms.',
            },
            {
                'title': 'Backend Development',
                'icon': 'bi-hdd-stack-fill',
                'is_exploring': False,
                'category_label': 'Core Focus',
                'category_class': 'badge bg-primary-subtle text-primary border border-primary-subtle',
                'description': 'Developing backend services using Django, configuring relational databases, and constructing RESTful APIs.',
            },
            {
                'title': 'Web Applications',
                'icon': 'bi-window-fullscreen',
                'is_exploring': False,
                'category_label': 'Core Focus',
                'category_class': 'badge bg-primary-subtle text-primary border border-primary-subtle',
                'description': 'Crafting responsive, accessible web interfaces utilizing semantic HTML5, modern CSS design systems, and JavaScript.',
            },
            {
                'title': 'Artificial Intelligence',
                'icon': 'bi-cpu-fill',
                'is_exploring': True,
                'category_label': 'Actively Exploring & Learning',
                'category_class': 'badge-exploring',
                'description': 'Actively exploring foundational AI theories, computational algorithms, and intelligent systems as an ongoing learning area.',
            },
            {
                'title': 'Machine Learning',
                'icon': 'bi-graph-up-arrow',
                'is_exploring': True,
                'category_label': 'Actively Exploring & Learning',
                'category_class': 'badge-exploring',
                'description': 'Studying data preprocessing, exploratory data analysis using NumPy and Pandas, and foundational predictive models.',
            },
        ],
    }
    return render(request, 'core/about.html', context)


def skills(request):
    """
    Renders the Technical Skills and Learning Journey page.
    Includes skill proficiencies across categories, dedicated AI-assisted development section,
    and structured current vs. future learning journey milestones.
    Filters for visible skills configured in Django Admin.
    """
    all_skills = Skill.objects.filter(is_visible=True).order_by('order', 'id')

    categories_dict = {
        'languages': {
            'title': 'Programming Languages',
            'icon': 'bi-code-slash',
            'description': 'Core programming languages practiced in academic projects and independent development.',
            'skills': all_skills.filter(category='languages'),
        },
        'frontend': {
            'title': 'Frontend Development',
            'icon': 'bi-window-fullscreen',
            'description': 'Web standards and styling libraries used to construct responsive, clean interfaces.',
            'skills': all_skills.filter(category='frontend'),
        },
        'backend': {
            'title': 'Backend Development',
            'icon': 'bi-layers-fill',
            'description': 'Server-side frameworks and architectural patterns for dependable web applications.',
            'skills': all_skills.filter(category='backend'),
        },
        'database': {
            'title': 'Database Management',
            'icon': 'bi-database-fill',
            'description': 'Relational data modeling, schema definition, and query operations.',
            'skills': all_skills.filter(category='database'),
        },
        'tools': {
            'title': 'Development Tools',
            'icon': 'bi-tools',
            'description': 'Version control, collaborative hosting, and integrated coding environments.',
            'skills': all_skills.filter(category='tools'),
        },
    }

    # Dedicated AI-Assisted Development & Vibe Coding category
    ai_assisted_skills = all_skills.filter(category='ai-assisted')

    # Practical applications of AI-Assisted development
    ai_assisted_applications = [
        'AI-assisted software development and workflow orchestration',
        'Prompt engineering for coding tasks and architecture design',
        'AI-assisted code generation and modular implementation',
        'Code explanation, refactoring, and codebase comprehension',
        'Debugging, exception tracing, and error resolution',
        'Full-stack frontend and backend development with AI assistance',
        'Iterative development, refinement, and rapid prototyping',
    ]

    # Areas of Interest
    areas_of_interest = all_skills.filter(category='interests')

    # Learning Journey Goals
    current_learning_goals = LearningGoal.objects.filter(stage='current').order_by('order', 'id')
    future_learning_goals = LearningGoal.objects.filter(stage='future').order_by('order', 'id')

    context = {
        'page_title': 'Technical Skills & Learning Journey | Bhuwan Raj Pandey',
        'categories_dict': categories_dict,
        'ai_assisted_skills': ai_assisted_skills,
        'ai_assisted_applications': ai_assisted_applications,
        'areas_of_interest': areas_of_interest,
        'current_learning_goals': current_learning_goals,
        'future_learning_goals': future_learning_goals,
    }
    return render(request, 'core/skills.html', context)


def experience(request):
    """
    Renders the dedicated Experience & Leadership page.
    Displays professional roles, club executive positions, hackathon head leadership, web program lead, and drone workshop.
    Filters for published experiences configured in Django Admin.
    """
    experiences = Experience.objects.filter(is_published=True).order_by('order', 'id')

    leadership_stats = {
        'total_initiatives': experiences.count(),
        'gurukul_role': 'Online Educator & Management Handler',
        'hackathon_participants': '60 participants (15 teams)',
        'club_tenure': '2025 – 2026',
        'institution': 'Himalayan WhiteHouse International College',
    }

    context = {
        'page_title': 'Experience & Leadership | Bhuwan Raj Pandey',
        'experiences': experiences,
        'leadership_stats': leadership_stats,
    }
    return render(request, 'core/experience.html', context)


def projects(request):
    """
    Renders the Project Portfolio page with interactive category filtering.
    Categories: All, Python / AI, Web Development, IoT, Programming Fundamentals.
    Filters for published projects configured in Django Admin.
    """
    selected_category = request.GET.get('category', 'all').strip()

    all_projects = Project.objects.filter(is_published=True).order_by('order', 'id')

    categories = [
        {'slug': 'all', 'name': 'All', 'count': all_projects.count()},
        {'slug': 'python-ai', 'name': 'Python / AI', 'count': all_projects.filter(category='python-ai').count()},
        {'slug': 'web-development', 'name': 'Web Development', 'count': all_projects.filter(category='web-development').count()},
        {'slug': 'iot', 'name': 'IoT', 'count': all_projects.filter(category='iot').count()},
        {'slug': 'programming-fundamentals', 'name': 'Programming Fundamentals', 'count': all_projects.filter(category='programming-fundamentals').count()},
    ]

    if selected_category and selected_category != 'all':
        filtered_projects = all_projects.filter(category=selected_category)
    else:
        filtered_projects = all_projects

    context = {
        'page_title': 'Projects Portfolio | Bhuwan Raj Pandey',
        'projects': filtered_projects,
        'all_projects': all_projects,
        'categories': categories,
        'selected_category': selected_category,
    }
    return render(request, 'core/projects.html', context)


def project_detail(request, slug):
    """
    Renders the individual project detail page.
    Displays overview, problem statement, objective, tech stack, main features, contribution, and status.
    Filters for published projects configured in Django Admin.
    """
    project = get_object_or_404(Project, slug=slug, is_published=True)

    previous_project = Project.objects.filter(is_published=True, order__lt=project.order).order_by('-order').first()
    next_project = Project.objects.filter(is_published=True, order__gt=project.order).order_by('order').first()

    related_projects = Project.objects.filter(is_published=True).exclude(id=project.id).filter(category=project.category)[:2]
    if not related_projects.exists():
        related_projects = Project.objects.filter(is_published=True).exclude(id=project.id)[:2]

    screenshots = project.screenshots.all().order_by('order', 'id')

    context = {
        'page_title': f"{project.title} | Projects | Bhuwan Raj Pandey",
        'project': project,
        'previous_project': previous_project,
        'next_project': next_project,
        'related_projects': related_projects,
        'screenshots': screenshots,
    }
    return render(request, 'core/project_detail.html', context)


def achievements(request):
    """
    Renders the Achievements, Leadership Recognitions, and Certificates page.
    Features key achievement cards and a certificate gallery with image modal previews and PDF viewing/downloading.
    Filters for published achievements and certificates configured in Django Admin.
    """
    selected_category = request.GET.get('category', 'all').strip()

    all_achievements = Achievement.objects.filter(is_published=True).order_by('order', 'id')
    all_certificates = Certificate.objects.filter(is_published=True).order_by('order', 'id')

    certificate_categories = [
        {'slug': 'all', 'name': 'All Credentials', 'count': all_certificates.count()},
        {'slug': 'leadership', 'name': 'Leadership & Events', 'count': all_certificates.filter(category='leadership').count()},
        {'slug': 'hackathon', 'name': 'Hackathons', 'count': all_certificates.filter(category='hackathon').count()},
        {'slug': 'workshop', 'name': 'Workshops & Training', 'count': all_certificates.filter(category='workshop').count()},
        {'slug': 'technical', 'name': 'Technical & Courses', 'count': all_certificates.filter(category='technical').count()},
        {'slug': 'academic', 'name': 'Academic & Other', 'count': all_certificates.filter(category='academic').count()},
    ]

    if selected_category and selected_category != 'all':
        filtered_certificates = all_certificates.filter(category=selected_category)
    else:
        filtered_certificates = all_certificates

    context = {
        'page_title': 'Achievements, Certificates & Recognition | Bhuwan Raj Pandey',
        'achievements': all_achievements,
        'certificates': filtered_certificates,
        'all_certificates': all_certificates,
        'certificate_categories': certificate_categories,
        'selected_category': selected_category,
    }
    return render(request, 'core/achievements.html', context)


def contact(request):
    """
    Renders the dedicated Contact page and handles recruiter/visitor contact form submissions.
    Validates form data, stores inquiries securely in the database, and provides feedback messages.
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_msg = form.save()
            messages.success(
                request,
                f"Thank you, {contact_msg.name}! Your message has been received securely. "
                "I will review your inquiry and get back to you shortly."
            )
            return redirect('core:contact')
        else:
            messages.error(
                request,
                "There was an issue with your submission. Please check the highlighted fields below."
            )
    else:
        form = ContactForm()

    context = {
        'page_title': 'Contact & Connect | Bhuwan Raj Pandey',
        'form': form,
    }
    return render(request, 'core/contact.html', context)


def download_cv(request):
    """
    Serves the latest active Curriculum Vitae (CV) PDF document dynamically.
    If no active CV exists, redirects gracefully to the contact page with an informative message.
    """
    active_cv = CurriculumVitae.get_active_cv()
    if not active_cv or not active_cv.pdf_file:
        messages.warning(
            request,
            "CV update in progress. Please send a message through the contact form to request the latest copy directly."
        )
        return redirect('core:contact')

    try:
        # Check that the physical file exists in storage
        if not active_cv.pdf_file.storage.exists(active_cv.pdf_file.name):
            messages.warning(
                request,
                "CV update in progress. Please send a message through the contact form to request the latest copy directly."
            )
            return redirect('core:contact')

        filename = "Bhuwan_Raj_Pandey_CV.pdf"
        return FileResponse(
            active_cv.pdf_file.open('rb'),
            as_attachment=True,
            filename=filename,
            content_type='application/pdf'
        )
    except Exception:
        messages.error(
            request,
            "Unable to access the CV file at this moment. Please reach out via email."
        )
        return redirect('core:contact')


@staff_member_required(login_url='admin:login')
def admin_dashboard(request):
    """
    Renders the custom executive CMS Dashboard for authorized staff users.
    Provides live statistics, quick actions, recent messages, and project overviews.
    """
    total_projects = Project.objects.count()
    published_projects = Project.objects.filter(is_published=True).count()

    total_experiences = Experience.objects.count()
    published_experiences = Experience.objects.filter(is_published=True).count()

    total_skills = Skill.objects.count()
    visible_skills = Skill.objects.filter(is_visible=True).count()

    total_achievements = Achievement.objects.count()
    published_achievements = Achievement.objects.filter(is_published=True).count()

    total_certificates = Certificate.objects.count()
    published_certificates = Certificate.objects.filter(is_published=True).count()

    total_messages = ContactMessage.objects.count()
    unread_messages = ContactMessage.objects.filter(is_read=False).count()

    active_cv = CurriculumVitae.get_active_cv()
    active_profile = Profile.get_active_profile()

    recent_messages = ContactMessage.objects.all().order_by('-created_at')[:6]
    recent_projects = Project.objects.all().order_by('-created_at', '-id')[:5]

    context = {
        'page_title': 'CMS Executive Dashboard | Portfolio Administration',
        'stats': {
            'total_projects': total_projects,
            'published_projects': published_projects,
            'total_experiences': total_experiences,
            'published_experiences': published_experiences,
            'total_skills': total_skills,
            'visible_skills': visible_skills,
            'total_achievements': total_achievements,
            'published_achievements': published_achievements,
            'total_certificates': total_certificates,
            'published_certificates': published_certificates,
            'total_messages': total_messages,
            'unread_messages': unread_messages,
        },
        'active_cv': active_cv,
        'active_profile': active_profile,
        'recent_messages': recent_messages,
        'recent_projects': recent_projects,
    }
    return render(request, 'admin/dashboard.html', context)




