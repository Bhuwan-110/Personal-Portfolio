from django.db import migrations


def seed_skills_and_goals(apps, schema_editor):
    Skill = apps.get_model('core', 'Skill')
    LearningGoal = apps.get_model('core', 'LearningGoal')

    skills_data = [
        # 1. Programming Languages
        {
            'name': 'Python',
            'category': 'languages',
            'proficiency': 'Intermediate / Developing',
            'description': 'Core Python 3 syntax, data structures, OOP principles, and clean algorithmic problem solving.',
            'icon': 'bi-filetype-py',
            'custom_logo': '',
            'is_currently_learning': True,
            'is_future_interest': False,
            'order': 10,
        },
        {
            'name': 'C',
            'category': 'languages',
            'proficiency': 'Basic',
            'description': 'Structured programming, pointers, memory concepts, and low-level disk file handling.',
            'icon': 'bi-code-square',
            'custom_logo': '',
            'is_currently_learning': False,
            'is_future_interest': False,
            'order': 11,
        },
        {
            'name': 'C++',
            'category': 'languages',
            'proficiency': 'Basic',
            'description': 'Object-Oriented Programming, classes, data encapsulation, and stream-based persistence using <fstream>.',
            'icon': 'bi-filetype-raw',
            'custom_logo': '',
            'is_currently_learning': False,
            'is_future_interest': False,
            'order': 12,
        },

        # 2. Frontend Development
        {
            'name': 'HTML',
            'category': 'frontend',
            'proficiency': 'Basic to Intermediate',
            'description': 'Semantic markup, accessible page structure, SEO tags, and responsive form controls.',
            'icon': 'bi-filetype-html',
            'custom_logo': '',
            'is_currently_learning': False,
            'is_future_interest': False,
            'order': 20,
        },
        {
            'name': 'CSS',
            'category': 'frontend',
            'proficiency': 'Basic to Intermediate',
            'description': 'Modern responsive layouts, Flexbox, CSS Grid, design variables, and light/dark theme implementation.',
            'icon': 'bi-filetype-css',
            'custom_logo': '',
            'is_currently_learning': False,
            'is_future_interest': False,
            'order': 21,
        },
        {
            'name': 'JavaScript',
            'category': 'frontend',
            'proficiency': 'Basic',
            'description': 'DOM manipulation, event listeners, dynamic user interactions, and asynchronous AJAX workflows.',
            'icon': 'bi-filetype-js',
            'custom_logo': '',
            'is_currently_learning': False,
            'is_future_interest': False,
            'order': 22,
        },
        {
            'name': 'Bootstrap',
            'category': 'frontend',
            'proficiency': 'Intermediate',
            'description': 'Responsive 12-column grid system, UI components, utility classes, and Bootstrap 5 theming.',
            'icon': 'bi-bootstrap-fill',
            'custom_logo': '',
            'is_currently_learning': False,
            'is_future_interest': False,
            'order': 23,
        },

        # 3. Backend Development
        {
            'name': 'Django',
            'category': 'backend',
            'proficiency': 'Beginner',
            'description': 'Model-View-Template (MVT) architecture, ORM database querying, URL routing, and built-in Admin management.',
            'icon': 'bi-layers-fill',
            'custom_logo': '',
            'is_currently_learning': True,
            'is_future_interest': False,
            'order': 30,
        },

        # 4. Database
        {
            'name': 'MySQL',
            'category': 'database',
            'proficiency': 'Basic',
            'description': 'Relational database schema modeling, primary/foreign key relations, and structured SQL operations.',
            'icon': 'bi-database-fill',
            'custom_logo': '',
            'is_currently_learning': True,
            'is_future_interest': False,
            'order': 40,
        },
        {
            'name': 'SQLite',
            'category': 'database',
            'proficiency': 'Basic to Intermediate',
            'description': 'Lightweight, serverless relational database integrated with Django development and academic applications.',
            'icon': 'bi-database',
            'custom_logo': '',
            'is_currently_learning': False,
            'is_future_interest': False,
            'order': 41,
        },

        # 5. Development Tools
        {
            'name': 'Git',
            'category': 'tools',
            'proficiency': 'Basic',
            'description': 'Distributed version control, repository tracking, staging, branching, and commit hygiene.',
            'icon': 'bi-git',
            'custom_logo': '',
            'is_currently_learning': False,
            'is_future_interest': False,
            'order': 50,
        },
        {
            'name': 'GitHub',
            'category': 'tools',
            'proficiency': 'Basic',
            'description': 'Remote repository hosting, project documentation, issue tracking, and collaborative portfolio publishing.',
            'icon': 'bi-github',
            'custom_logo': '',
            'is_currently_learning': False,
            'is_future_interest': False,
            'order': 51,
        },
        {
            'name': 'Visual Studio Code',
            'category': 'tools',
            'proficiency': 'Intermediate',
            'description': 'Daily coding environment, debugging, integrated terminal, Python linters, and workspace productivity tools.',
            'icon': 'bi-code-slash',
            'custom_logo': '',
            'is_currently_learning': False,
            'is_future_interest': False,
            'order': 52,
        },

        # 6. AI-Assisted Development & Vibe Coding (Separate Category)
        {
            'name': 'Google Antigravity',
            'category': 'ai-assisted',
            'proficiency': 'Active Practical Workflow',
            'description': 'AI-assisted development, workspace agent orchestration, iterative code refinement, and automated diagnostics.',
            'icon': 'bi-stars',
            'custom_logo': 'core/images/icons/google-antigravity.svg',
            'is_currently_learning': True,
            'is_future_interest': False,
            'order': 60,
        },
        {
            'name': 'Claude AI',
            'category': 'ai-assisted',
            'proficiency': 'Active Practical Workflow',
            'description': 'Prompt engineering for coding tasks, code explanation, architectural reasoning, and error resolution.',
            'icon': 'bi-robot',
            'custom_logo': 'core/images/icons/claude-ai.svg',
            'is_currently_learning': True,
            'is_future_interest': False,
            'order': 61,
        },

        # 7. Areas of Interest
        {
            'name': 'Artificial Intelligence',
            'category': 'interests',
            'proficiency': 'Exploration Area',
            'description': 'Foundational principles, intelligent algorithms, and dedicated long-term aspiration toward an AI engineering career.',
            'icon': 'bi-cpu-fill',
            'custom_logo': '',
            'is_currently_learning': False,
            'is_future_interest': True,
            'order': 70,
        },
        {
            'name': 'Machine Learning',
            'category': 'interests',
            'proficiency': 'Exploration Area',
            'description': 'Exploratory data analysis, statistical metrics, NumPy, Pandas, and foundational predictive algorithms.',
            'icon': 'bi-graph-up-arrow',
            'custom_logo': '',
            'is_currently_learning': False,
            'is_future_interest': True,
            'order': 71,
        },
        {
            'name': 'Natural Language Processing',
            'category': 'interests',
            'proficiency': 'Exploration Area',
            'description': 'Text processing, keyword extraction, and resume candidate matching workflows.',
            'icon': 'bi-chat-square-text-fill',
            'custom_logo': '',
            'is_currently_learning': False,
            'is_future_interest': True,
            'order': 72,
        },
        {
            'name': 'Backend Engineering',
            'category': 'interests',
            'proficiency': 'Active Study & Focus',
            'description': 'Designing performant server-side architectures, database schemas, and robust API endpoints.',
            'icon': 'bi-hdd-network-fill',
            'custom_logo': '',
            'is_currently_learning': True,
            'is_future_interest': False,
            'order': 73,
        },
    ]

    for s_data in skills_data:
        Skill.objects.update_or_create(name=s_data['name'], defaults=s_data)

    goals_data = [
        # Current Focus
        {
            'title': 'Python Fundamentals',
            'stage': 'current',
            'description': 'Strengthening mastery of core Python 3 syntax, control flow, functions, and standard library modules.',
            'badge_label': 'Daily Active Focus',
            'icon': 'bi-filetype-py',
            'order': 1,
        },
        {
            'title': 'Object-Oriented Programming in Python',
            'stage': 'current',
            'description': 'Applying clean OOP paradigms including classes, encapsulation, inheritance, polymorphism, and modular architectures.',
            'badge_label': 'Daily Active Focus',
            'icon': 'bi-braces-asterisk',
            'order': 2,
        },
        {
            'title': 'Django and Backend Development',
            'stage': 'current',
            'description': 'Building production-grade web applications, ORM queries, URL dispatching, and secure template architectures.',
            'badge_label': 'Core Framework',
            'icon': 'bi-layers',
            'order': 3,
        },
        {
            'title': 'SQL and Database Management',
            'stage': 'current',
            'description': 'Designing relational database schemas in MySQL and SQLite with optimal relations, constraints, and data integrity.',
            'badge_label': 'Database Foundations',
            'icon': 'bi-database-check',
            'order': 4,
        },
        {
            'title': 'APIs and Software Integration',
            'stage': 'current',
            'description': 'Structuring RESTful API endpoints, handling JSON requests/responses, and connecting client-side interfaces.',
            'badge_label': 'Web Architecture',
            'icon': 'bi-hdd-network',
            'order': 5,
        },
        {
            'title': 'AI-Assisted Development & Vibe Coding',
            'stage': 'current',
            'description': 'Integrating Google Antigravity and Claude AI into the practical workflow for prompt engineering, iterative coding, and debugging.',
            'badge_label': 'Modern Workflow',
            'icon': 'bi-stars',
            'order': 6,
        },

        # Future Learning Interests
        {
            'title': 'Artificial Intelligence',
            'stage': 'future',
            'description': 'Deep study of foundational AI theories, agentic workflows, search algorithms, and computational intelligence.',
            'badge_label': 'Long-Term Ambition',
            'icon': 'bi-cpu',
            'order': 7,
        },
        {
            'title': 'Machine Learning',
            'stage': 'future',
            'description': 'Studying supervised and unsupervised learning algorithms, model training pipelines, and evaluation metrics.',
            'badge_label': 'Academic Study Area',
            'icon': 'bi-graph-up',
            'order': 8,
        },
        {
            'title': 'Natural Language Processing (NLP)',
            'stage': 'future',
            'description': 'Investigating semantic text processing, tokenization, embeddings, and modern language model integration.',
            'badge_label': 'Specialized Interest',
            'icon': 'bi-chat-left-dots',
            'order': 9,
        },
        {
            'title': 'AI Application Development',
            'stage': 'future',
            'description': 'Architecting full-stack software applications that embed machine learning and assistive AI capabilities into practical user tools.',
            'badge_label': 'Applied Engineering',
            'icon': 'bi-robot',
            'order': 10,
        },
    ]

    for g_data in goals_data:
        LearningGoal.objects.update_or_create(title=g_data['title'], defaults=g_data)


def remove_skills_and_goals(apps, schema_editor):
    Skill = apps.get_model('core', 'Skill')
    LearningGoal = apps.get_model('core', 'LearningGoal')
    Skill.objects.all().delete()
    LearningGoal.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_learninggoal_skill'),
    ]

    operations = [
        migrations.RunPython(seed_skills_and_goals, remove_skills_and_goals),
    ]
