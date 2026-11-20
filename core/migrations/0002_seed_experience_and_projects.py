from django.db import migrations


def seed_experiences_and_projects(apps, schema_editor):
    Experience = apps.get_model('core', 'Experience')
    Project = apps.get_model('core', 'Project')

    # 1. Experiences & Leadership
    experiences = [
        {
            'title': 'Whitehouse Innovators – IT Club',
            'role': 'General Secretary (2025) & Vice President (2026)',
            'institution': 'Himalayan WhiteHouse International College',
            'category': 'leadership',
            'period': '2025 – 2026',
            'duration_stats': 'Executive Leadership Tenure',
            'description': (
                'Served in key executive leadership roles within the Whitehouse Innovators IT Club, '
                'fostering collaborative student technology engagement, coordinating departmental programs, '
                'and driving technical learning opportunities.'
            ),
            'responsibilities': (
                'Student coordination across IT cohorts\n'
                'Event planning and organization\n'
                'Documentation and communication\n'
                'Supporting technology-related activities\n'
                'Team coordination and leadership'
            ),
            'icon': 'bi-people-fill',
            'order': 1,
        },
        {
            'title': 'Sankalpa Hackathon',
            'role': 'Event Head',
            'institution': 'Himalayan WhiteHouse International College',
            'category': 'event',
            'period': '3-Day Hackathon',
            'duration_stats': '15 Teams • 4 Participants per Team • 60 Participants in Total',
            'description': (
                'Contributed to leading and organizing a three-day hackathon focused on technology and '
                'digital problem-solving for 60 participating students across 15 collaborative teams.'
            ),
            'responsibilities': (
                'Led overall event execution, participant coordination, and schedule management\n'
                'Coordinated 15 student teams (60 total participants) across 3 intensive days of problem-solving\n'
                'Facilitated problem statement briefings, progress milestones, and technical inquiries\n'
                'Managed documentation, judging coordination, and team logistics throughout the hackathon'
            ),
            'icon': 'bi-trophy-fill',
            'order': 2,
        },
        {
            'title': 'Web Development Program',
            'role': 'Main Lead',
            'institution': 'Himalayan WhiteHouse International College',
            'category': 'workshop',
            'period': 'One-Day Program',
            'duration_stats': 'Practical Web Architecture Workshop',
            'description': (
                'Led the organization and coordination of a one-day web development program for students, '
                'providing hands-on learning in modern web technologies.'
            ),
            'responsibilities': (
                'Led the organization, scheduling, and logistical coordination of the program\n'
                'Coordinated student registrations, lab environment setup, and resources\n'
                'Guided peers through practical web development exercises and foundational workflows\n'
                'Conducted session communications and participant documentation'
            ),
            'icon': 'bi-code-slash',
            'order': 3,
        },
        {
            'title': 'Drone Workshop',
            'role': 'Organizer & Coordinator',
            'institution': 'Himalayan WhiteHouse International College',
            'category': 'workshop',
            'period': 'Hands-on Workshop',
            'duration_stats': 'Emerging Hardware & Aviation Tech Exposure',
            'description': (
                'Organized a drone workshop to provide students with exposure to drone technology and '
                'practical learning.'
            ),
            'responsibilities': (
                'Planned and organized the demonstration space and workshop schedule\n'
                'Facilitated student exposure to drone components, flight principles, and practical tech\n'
                'Coordinated participant safety protocols, session timeline, and interactive discussions\n'
                'Gathered student feedback and documented workshop outcomes'
            ),
            'icon': 'bi-broadcast-pin',
            'order': 4,
        },
    ]

    for exp_data in experiences:
        Experience.objects.update_or_create(title=exp_data['title'], defaults=exp_data)

    # 2. Projects
    projects = [
        {
            'title': 'AI-Based Resume Screening System',
            'slug': 'ai-based-resume-screening-system',
            'subtitle': 'Candidate Profile Evaluation & Matching Prototype',
            'category': 'python-ai',
            'status': 'Prototype',
            'short_description': (
                'A system designed to assist recruiters in evaluating resumes against job requirements '
                'by identifying relevant skills, matching candidate profiles, and supporting resume screening.'
            ),
            'overview': (
                'The AI-Based Resume Screening System is a prototype developed to assist human recruiters in evaluating '
                'unstandardized resumes against structured job openings. By parsing documents, extracting key technical competencies, '
                'and computing skill alignment, the system acts as a supportive decision aid. Importantly, it is engineered as a '
                'human-in-the-loop tool and does not make automatic hiring decisions.'
            ),
            'problem_statement': (
                'Recruiting teams routinely receive dozens or hundreds of unstructured resumes for individual technical positions. '
                'Manually reviewing each document for core requirements can lead to fatigue, oversight of relevant applicant credentials, '
                'and prolonged turnaround times.'
            ),
            'objective': (
                'To build a supportive backend prototype that parses incoming resumes, detects candidate competencies, computes relevance scores '
                'against posted job requirements, and presents an organized evaluation overview to assist recruiter decision-making.'
            ),
            'technologies': 'Python, Django, Machine Learning, NLP',
            'features_or_concepts': (
                'Resume text extraction and document parsing\n'
                'Job requirement matching and semantic alignment\n'
                'Skill identification and domain categorization\n'
                'Candidate comparison dashboard overview\n'
                'Human-in-the-loop decision support (strictly assistive, no automated decisions)'
            ),
            'my_contribution': (
                'Architected the Django backend structure, designed the text processing and skill-matching pipeline '
                'in Python, and implemented the candidate profile comparison view.'
            ),
            'github_url': None,
            'featured': True,
            'order': 1,
        },
        {
            'title': 'GUNASO-MP',
            'slug': 'gunaso-mp-grievance-management-system',
            'subtitle': 'गुनासो अनुगमन, व्यवस्थापन तथा समाधान प्रणाली',
            'category': 'web-development',
            'status': 'College project',
            'short_description': (
                'A web-based grievance management system designed to support the submission, monitoring, '
                'management, and resolution tracking of public grievances directed towards elected representatives.'
            ),
            'overview': (
                'GUNASO-MP (गुनासो अनुगमन, व्यवस्थापन तथा समाधान प्रणाली) is a college web development project engineered '
                'to facilitate transparent communication between citizens and elected representatives. The system enables constituents '
                'to log public grievances, track progress through unique tracking identifiers, and enables representative offices to '
                'review, assign, and update grievance statuses systematically.'
            ),
            'problem_statement': (
                'Citizens often lack a direct, transparent, and verifiable channel to communicate community grievances, infrastructure issues, '
                'and localized concerns to their elected representatives, leading to delays and lack of accountability.'
            ),
            'objective': (
                'To create a structured, web-based grievance tracking platform featuring asynchronous citizen submission forms, tracking mechanisms, '
                'and a representative administrative dashboard for systematic grievance triage and resolution.'
            ),
            'technologies': 'PHP, MySQL, HTML, CSS, JavaScript, AJAX',
            'features_or_concepts': (
                'Online citizen grievance submission portal\n'
                'Unique tracking code generation for grievance monitoring\n'
                'Administrative panel for elected representatives and case officers\n'
                'Asynchronous form validation and state updates via AJAX\n'
                'Relational MySQL schema managing grievances, categories, and resolution logs'
            ),
            'my_contribution': (
                'Designed the relational database tables in MySQL, developed the backend PHP handlers for grievance lifecycle routing, '
                'and implemented responsive citizen submission forms with AJAX integration.'
            ),
            'github_url': None,
            'featured': True,
            'order': 2,
        },
        {
            'title': 'Speed Detection and Traffic Challan Automation System',
            'slug': 'speed-detection-traffic-challan-automation',
            'subtitle': 'Sensor-Based Vehicle Speed Detection & Challan Trigger Prototype',
            'category': 'iot',
            'status': 'College project',
            'short_description': (
                'An academic IoT project exploring vehicle speed detection and traffic challan automation '
                'using Arduino and sensors.'
            ),
            'overview': (
                'An exploratory hardware and Internet of Things (IoT) project that measures the velocity of passing objects using '
                'spaced sensor thresholds connected to an Arduino microcontroller. When calculated speed exceeds configured safety limits, '
                'the system triggers a simulated traffic violation and automated challan record.'
            ),
            'problem_statement': (
                'Manual monitoring of vehicle speeds on roads requires constant personnel presence and introduces human timing errors. '
                'Automated sensor-based detection demonstrates how electronic timing can reliably measure velocity and flag violations.'
            ),
            'objective': (
                'To explore the integration of microcontroller programming and sensor timing to calculate vehicle speed across designated intervals '
                'and trigger an automated challan notification workflow.'
            ),
            'technologies': 'Arduino, Sensors',
            'features_or_concepts': (
                'Sensor-based interval timing for vehicle speed calculation\n'
                'Microcontroller program logic authored on Arduino\n'
                'Configurable speed threshold detection\n'
                'Simulated automated traffic challan alert output upon speed violation'
            ),
            'my_contribution': (
                'Programmed the Arduino microcontroller logic, calculated interval timing algorithms based on sensor triggers, '
                'and documented experimental velocity measurements.'
            ),
            'github_url': None,
            'featured': True,
            'order': 3,
        },
        {
            'title': 'Attendance Management System',
            'slug': 'attendance-management-system',
            'subtitle': 'Student Attendance Tracking & Record System',
            'category': 'programming-fundamentals',
            'status': 'Academic project',
            'short_description': (
                'An academic software project focused on student attendance management.'
            ),
            'overview': (
                'An academic software project developed in Java to streamline classroom attendance logging, roll call management, '
                'and student attendance summary calculations. Built to replace manual paper sheets with structured software records.'
            ),
            'problem_statement': (
                'Paper-based attendance sheets are prone to physical damage, calculation errors across terms, and lack quick summary capabilities.'
            ),
            'objective': (
                'To build a structured desktop application applying Java Object-Oriented Programming (OOP) paradigms for logging, '
                'reviewing, and calculating student attendance.'
            ),
            'technologies': 'Java',
            'features_or_concepts': (
                'Student record management by roll number and course\n'
                'Attendance marking workflows (Present / Absent status)\n'
                'Attendance summary calculations across class sessions\n'
                'Application of Java Object-Oriented Programming (OOP) principles'
            ),
            'my_contribution': (
                'Designed the Java class structure using OOP concepts (encapsulation, abstraction), authored attendance tracking methods, '
                'and validated system accuracy.'
            ),
            'github_url': None,
            'featured': True,
            'order': 4,
        },
        {
            'title': 'Bank Management System (C)',
            'slug': 'bank-management-system-c',
            'subtitle': 'Console Banking System with File Handling Persistence',
            'category': 'programming-fundamentals',
            'status': 'Academic project',
            'short_description': (
                'A programming project exploring basic bank management operations and persistent data storage using C file handling.'
            ),
            'overview': (
                'A foundational programming project authored in C that implements fundamental banking operations through an interactive '
                'console interface. Demonstrates low-level data persistence, structured records, and binary/text file I/O operations.'
            ),
            'problem_statement': (
                'Understanding persistent data management without a relational database engine requires direct manipulation of file streams, '
                'memory buffers, and structured byte records in procedural programming.'
            ),
            'objective': (
                'To demonstrate proficiency in C programming, pointers, custom structures, and disk-level file handling by creating '
                'a persistent console banking management system.'
            ),
            'technologies': 'C',
            'features_or_concepts': (
                'Customer account registration and record structuring\n'
                'Deposit, withdrawal, and balance inquiry transactions\n'
                'Persistent data storage utilizing C File Handling (fopen, fread, fwrite, fclose)\n'
                'Console-based menu navigation and basic input verification'
            ),
            'my_contribution': (
                'Defined C structures for account entities, wrote file I/O operations to read/write accounts to disk, '
                'and built the interactive console command menu.'
            ),
            'github_url': None,
            'featured': False,
            'order': 5,
        },
        {
            'title': 'Bank Management System (C++)',
            'slug': 'bank-management-system-cpp',
            'subtitle': 'Object-Oriented Banking System with Stream-Based File Handling',
            'category': 'programming-fundamentals',
            'status': 'Academic project',
            'short_description': (
                'A C++ programming project focused on applying OOP concepts and file handling to a bank management application.'
            ),
            'overview': (
                'An object-oriented bank management system written in C++ that demonstrates how procedural banking logic can be '
                'refactored into reusable, encapsulated classes with stream-based file persistence using `<fstream>`.'
            ),
            'problem_statement': (
                'Transitioning from procedural to object-oriented programming requires structuring data and behavior together inside '
                'encapsulated classes while maintaining data persistence across application sessions.'
            ),
            'objective': (
                'To apply Object-Oriented Programming (OOP) principles in C++ (classes, objects, encapsulation, data hiding) alongside '
                'file streaming to build a clean banking management application.'
            ),
            'technologies': 'C++',
            'features_or_concepts': (
                'Class-based object architecture encapsulating account data and member functions\n'
                'Account balance updates with transaction safety validation\n'
                'Persistent stream handling utilizing C++ <fstream> (ifstream and ofstream)\n'
                'Menu-driven user interface with modular method calls'
            ),
            'my_contribution': (
                'Engineered the core Account class with private member variables and public operational methods, '
                'and implemented disk streaming for saving and loading account data.'
            ),
            'github_url': None,
            'featured': False,
            'order': 6,
        },
    ]

    for proj_data in projects:
        Project.objects.update_or_create(slug=proj_data['slug'], defaults=proj_data)


def remove_experiences_and_projects(apps, schema_editor):
    Experience = apps.get_model('core', 'Experience')
    Project = apps.get_model('core', 'Project')
    Experience.objects.all().delete()
    Project.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(seed_experiences_and_projects, remove_experiences_and_projects),
    ]
