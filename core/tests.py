import tempfile
from django.contrib import admin
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, override_settings
from django.urls import reverse
from core.models import (
    Achievement, Certificate, ContactMessage, CurriculumVitae,
    Experience, LearningGoal, Profile, Project, ProjectScreenshot, Skill
)


class PortfolioHomepageTests(TestCase):
    def setUp(self):
        self.response = self.client.get(reverse('core:home'))

    def test_homepage_status_and_templates(self):
        """Verify homepage returns 200 OK and renders home.html extending base.html."""
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'core/home.html')
        self.assertTemplateUsed(self.response, 'core/base.html')

    def test_hero_section_and_personal_details(self):
        """Verify personal name, title, location, and social links are rendered."""
        self.assertContains(self.response, 'Bhuwan Raj Pandey')
        self.assertContains(self.response, 'Aspiring Software Developer | Python &amp; AI Enthusiast')
        self.assertContains(self.response, 'Kathmandu, Nepal')
        self.assertContains(self.response, 'officialbhuwan454@gmail.com')
        self.assertContains(self.response, 'https://github.com/Bhuwan-110')
        self.assertContains(self.response, 'https://www.linkedin.com/in/bhuwan-pandey-2b829a2ba/')

    def test_profile_photo_rendered(self):
        """Verify uploaded profile picture is rendered."""
        self.assertContains(self.response, 'profile-avatar-wrapper')
        self.assertContains(self.response, 'profile-picture.png')

    def test_navbar_navigation_links(self):
        """Verify navbar links directly to About, Experience, and Projects pages."""
        self.assertContains(self.response, reverse('core:about'))
        self.assertContains(self.response, reverse('core:experience'))
        self.assertContains(self.response, reverse('core:projects'))


class PortfolioAboutPageTests(TestCase):
    def setUp(self):
        self.response = self.client.get(reverse('core:about'))

    def test_about_page_status_and_templates(self):
        """Verify about page returns 200 OK and renders about.html extending base.html."""
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'core/about.html')
        self.assertTemplateUsed(self.response, 'core/base.html')

    def test_about_me_section_content(self):
        """Verify the exact biographical paragraphs and profile details."""
        self.assertContains(self.response, 'Bhuwan Raj Pandey')
        self.assertContains(self.response, 'Bachelor of Information Technology (BIT)')
        self.assertContains(self.response, 'Himalayan WhiteHouse International College')
        self.assertContains(self.response, 'leadership activities')
        self.assertContains(self.response, 'teamwork, coordination, planning, documentation, and problem-solving skills')
        self.assertContains(self.response, 'AI Engineer')
        self.assertContains(self.response, 'profile-picture.png')

    def test_education_section_details(self):
        """Verify education timeline contains accurate college, semester, and location info."""
        self.assertContains(self.response, 'Bachelor of Information Technology (BIT)')
        self.assertContains(self.response, 'Himalayan WhiteHouse International College')
        self.assertContains(self.response, 'Putalisadak, Kathmandu, Nepal')
        self.assertContains(self.response, '7th Semester')
        self.assertContains(self.response, '2027')


class PortfolioExperienceTests(TestCase):
    def setUp(self):
        self.response = self.client.get(reverse('core:experience'))

    def test_experience_page_status_and_templates(self):
        """Verify experience page returns 200 OK and renders experience.html extending base.html."""
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'core/experience.html')
        self.assertTemplateUsed(self.response, 'core/base.html')

    def test_gurukul_experience(self):
        """Verify GURUKUL – शिक्षा professional experience, roles, and responsibilities."""
        self.assertContains(self.response, 'GURUKUL – शिक्षा')
        self.assertContains(self.response, 'Online Educator &amp; entire management handler')
        self.assertContains(self.response, 'Loksewa and Security Forces Examination Preparation')
        self.assertContains(self.response, 'Nepal Army, APF, and Nepal Police examinations')
        self.assertContains(self.response, 'Online Teaching')
        self.assertContains(self.response, 'Educational Content Creation')
        self.assertContains(self.response, 'Student Engagement')
        self.assertContains(self.response, 'Mentorship')

    def test_it_club_experience(self):
        """Verify Whitehouse Innovators IT Club positions and responsibilities."""
        self.assertContains(self.response, 'Whitehouse Innovators – IT Club')
        self.assertContains(self.response, 'General Secretary (2025) &amp; Vice President (2026)')
        self.assertContains(self.response, 'Student coordination across IT cohorts')
        self.assertContains(self.response, 'Event planning and organization')
        self.assertContains(self.response, 'Documentation and communication')

    def test_sankalpa_hackathon_experience(self):
        """Verify Sankalpa Hackathon details, role, and exact statistics."""
        self.assertContains(self.response, 'Sankalpa Hackathon')
        self.assertContains(self.response, 'Event Head')
        self.assertContains(self.response, '3-Day Hackathon')
        self.assertContains(self.response, '15 Teams')
        self.assertContains(self.response, '4 Participants per Team')
        self.assertContains(self.response, '60 Participants in Total')

    def test_web_dev_and_drone_workshops(self):
        """Verify Web Development Program and Drone Workshop leadership entries."""
        self.assertContains(self.response, 'Web Development Program')
        self.assertContains(self.response, 'Main Lead')
        self.assertContains(self.response, 'One-Day Program')
        self.assertContains(self.response, 'Drone Workshop')
        self.assertContains(self.response, 'exposure to drone technology and practical learning')


class PortfolioProjectsTests(TestCase):
    def setUp(self):
        self.response = self.client.get(reverse('core:projects'))

    def test_projects_page_status_and_templates(self):
        """Verify projects page returns 200 OK and renders projects.html extending base.html."""
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'core/projects.html')
        self.assertTemplateUsed(self.response, 'core/base.html')

    def test_all_six_projects_displayed(self):
        """Verify all 6 required projects are displayed in the portfolio."""
        self.assertContains(self.response, 'AI-Based Resume Screening System')
        self.assertContains(self.response, 'GUNASO-MP')
        self.assertContains(self.response, 'गुनासो अनुगमन, व्यवस्थापन तथा समाधान प्रणाली')
        self.assertContains(self.response, 'Speed Detection and Traffic Challan Automation System')
        self.assertContains(self.response, 'Attendance Management System')
        self.assertContains(self.response, 'Bank Management System (C)')
        self.assertContains(self.response, 'Bank Management System (C++)')

    def test_category_filtering(self):
        """Verify server-side and client-side category filtering endpoints."""
        # Test Python / AI filter
        r_ai = self.client.get(reverse('core:projects') + '?category=python-ai')
        self.assertEqual(r_ai.status_code, 200)
        self.assertContains(r_ai, 'AI-Based Resume Screening System')
        self.assertNotContains(r_ai, 'GUNASO-MP')

        # Test Web Development filter
        r_web = self.client.get(reverse('core:projects') + '?category=web-development')
        self.assertEqual(r_web.status_code, 200)
        self.assertContains(r_web, 'GUNASO-MP')
        self.assertNotContains(r_web, 'Attendance Management System')

        # Test IoT filter
        r_iot = self.client.get(reverse('core:projects') + '?category=iot')
        self.assertEqual(r_iot.status_code, 200)
        self.assertContains(r_iot, 'Speed Detection and Traffic Challan Automation System')
        self.assertNotContains(r_iot, 'AI-Based Resume Screening System')

        # Test Programming Fundamentals filter
        r_prog = self.client.get(reverse('core:projects') + '?category=programming-fundamentals')
        self.assertEqual(r_prog.status_code, 200)
        self.assertContains(r_prog, 'Bank Management System (C)')
        self.assertContains(r_prog, 'Bank Management System (C++)')
        self.assertContains(r_prog, 'Attendance Management System')

    def test_project_detail_pages(self):
        """Verify detail page routing and content for each project."""
        for project in Project.objects.all():
            detail_url = reverse('core:project_detail', kwargs={'slug': project.slug})
            res = self.client.get(detail_url)
            self.assertEqual(res.status_code, 200)
            self.assertTemplateUsed(res, 'core/project_detail.html')
            self.assertContains(res, project.title)
            self.assertContains(res, 'Project Overview')
            self.assertContains(res, 'Project Objective')
            self.assertContains(res, 'My Personal Contribution')
            self.assertContains(res, project.status)


class PortfolioSkillsTests(TestCase):
    def setUp(self):
        self.response = self.client.get(reverse('core:skills'))

    def test_skills_page_status_and_templates(self):
        """Verify skills page returns 200 OK and renders skills.html extending base.html."""
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'core/skills.html')
        self.assertTemplateUsed(self.response, 'core/base.html')

    def test_programming_languages_category(self):
        """Verify Programming Languages category and entries."""
        self.assertContains(self.response, '1. Programming Languages')
        self.assertContains(self.response, 'Python')
        self.assertContains(self.response, 'Intermediate / Developing')
        self.assertContains(self.response, 'C')
        self.assertContains(self.response, 'C++')

    def test_frontend_development_category(self):
        """Verify Frontend Development category and entries."""
        self.assertContains(self.response, '2. Frontend Development')
        self.assertContains(self.response, 'HTML')
        self.assertContains(self.response, 'CSS')
        self.assertContains(self.response, 'JavaScript')
        self.assertContains(self.response, 'Bootstrap')

    def test_backend_and_database_categories(self):
        """Verify Backend Development and Database Management categories."""
        self.assertContains(self.response, '3. Backend Development')
        self.assertContains(self.response, 'Django')
        self.assertContains(self.response, '4. Database Management')
        self.assertContains(self.response, 'MySQL')
        self.assertContains(self.response, 'SQLite')

    def test_traditional_development_tools(self):
        """Verify Traditional Development Tools category and entries."""
        self.assertContains(self.response, '5. Traditional Development Tools')
        self.assertContains(self.response, 'Git')
        self.assertContains(self.response, 'GitHub')
        self.assertContains(self.response, 'Visual Studio Code')

    def test_ai_assisted_development_section(self):
        """Verify dedicated AI-Assisted Development & Vibe Coding category and custom logos."""
        self.assertContains(self.response, 'AI-Assisted Development &amp; Vibe Coding')
        self.assertContains(self.response, 'Google Antigravity')
        self.assertContains(self.response, 'Claude AI')
        self.assertContains(self.response, 'google-antigravity.svg')
        self.assertContains(self.response, 'claude-ai.svg')
        self.assertContains(self.response, 'Prompt engineering for coding tasks and architecture design')
        self.assertContains(self.response, 'Code explanation, refactoring, and codebase comprehension')
        self.assertContains(self.response, 'Engineering Clarification:')
        self.assertContains(self.response, 'claim expertise in training or creating proprietary foundation AI models')

    def test_learning_journey_focus_and_future(self):
        """Verify Learning Journey distinguishes current practice from future exploration."""
        self.assertContains(self.response, 'My Learning Journey')
        self.assertContains(self.response, 'Current Learning Focus')
        self.assertContains(self.response, 'Future Learning Interests')
        self.assertContains(self.response, 'Python Fundamentals')
        self.assertContains(self.response, 'Object-Oriented Programming in Python')
        self.assertContains(self.response, 'Django and Backend Development')
        self.assertContains(self.response, 'SQL and Database Management')
        self.assertContains(self.response, 'Natural Language Processing (NLP)')
        self.assertContains(self.response, 'AI Application Development')

    def test_areas_of_interest(self):
        """Verify Areas of Interest overview cards."""
        self.assertContains(self.response, 'Specialization &amp; Areas of Interest')
        self.assertContains(self.response, 'Artificial Intelligence')
        self.assertContains(self.response, 'Machine Learning')
        self.assertContains(self.response, 'Natural Language Processing')
        self.assertContains(self.response, 'Backend Engineering')

    def test_navigation_link_in_navbar(self):
        """Verify navbar and footer link to the skills page."""
        self.assertContains(self.response, reverse('core:skills'))
        home_res = self.client.get(reverse('core:home'))
        self.assertContains(home_res, reverse('core:skills'))


class PortfolioAchievementsTests(TestCase):
    def setUp(self):
        self.response = self.client.get(reverse('core:achievements'))

    def test_achievements_page_status_and_templates(self):
        """Verify achievements page returns 200 OK and renders achievements.html extending base.html."""
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'core/achievements.html')
        self.assertTemplateUsed(self.response, 'core/base.html')

    def test_part_a_milestone_achievements_content(self):
        """Verify all 4 required achievements from Part A are displayed with accurate details."""
        # 1. Sankalpa Hackathon
        self.assertContains(self.response, 'Sankalpa Hackathon')
        self.assertContains(self.response, 'Event Head')
        self.assertContains(self.response, '3-Day Hackathon')
        self.assertContains(self.response, '15 Teams | 60 Participants')
        self.assertContains(self.response, 'three-day hackathon focused on technology and digital problem-solving')

        # 2. Web Development Program
        self.assertContains(self.response, 'Web Development Program')
        self.assertContains(self.response, 'Main Lead')
        self.assertContains(self.response, 'One-Day Program')
        self.assertContains(self.response, 'one-day web development program for students')

        # 3. Drone Workshop
        self.assertContains(self.response, 'Drone Workshop')
        self.assertContains(self.response, 'exposure to drone technology')

        # 4. Whitehouse Innovators – IT Club
        self.assertContains(self.response, 'Whitehouse Innovators – IT Club')
        self.assertContains(self.response, 'General Secretary (2025) &amp; Vice President (2026)')
        self.assertContains(self.response, '2025 – 2026')

    def test_certificate_gallery_and_categories(self):
        """Verify certificates and credential categories."""
        self.assertContains(self.response, 'Certificate &amp; Credential Gallery')
        self.assertContains(self.response, 'Certificate of Executive Leadership')
        self.assertContains(self.response, 'Certificate of Appreciation – Event Head')
        self.assertContains(self.response, 'Web Development Program Organizing Lead')
        self.assertContains(self.response, 'Drone Workshop Organizing Committee Recognition')
        self.assertContains(self.response, 'Leadership &amp; Events')
        self.assertContains(self.response, 'Hackathons')
        self.assertContains(self.response, 'Workshops &amp; Training')

    def test_certificate_image_lightbox_and_temporary_placeholder(self):
        """Verify image certificate triggers the lightbox modal and displays temporary disclaimer."""
        self.assertContains(self.response, 'data-cert-modal="true"')
        self.assertContains(self.response, 'certificate_placeholder.png')
        self.assertContains(self.response, 'Enlarge Certificate')
        self.assertContains(self.response, 'Temporary preview placeholder file')

    def test_certificate_pdf_view_and_download(self):
        """Verify PDF certificate provides safe view in new tab and download link."""
        self.assertContains(self.response, 'sample_certificate.pdf')
        self.assertContains(self.response, 'View PDF in New Tab')
        self.assertContains(self.response, 'Download PDF')
        self.assertContains(self.response, 'target="_blank"')
        self.assertContains(self.response, 'rel="noopener noreferrer"')

    def test_achievement_without_file_fallback(self):
        """Verify achievements without an uploaded certificate file render gracefully without fake previews."""
        self.assertContains(self.response, 'Official Institutional Record')
        self.assertContains(self.response, 'Document on Request')

    def test_category_filtering(self):
        """Verify category filtering for certificate gallery context and rendering."""
        r_lead = self.client.get(reverse('core:achievements') + '?category=leadership')
        self.assertEqual(r_lead.status_code, 200)
        self.assertEqual(len(r_lead.context['certificates']), 1)
        self.assertEqual(r_lead.context['certificates'][0].title, 'Certificate of Executive Leadership')

        r_hack = self.client.get(reverse('core:achievements') + '?category=hackathon')
        self.assertEqual(r_hack.status_code, 200)
        self.assertEqual(len(r_hack.context['certificates']), 1)
        self.assertEqual(r_hack.context['certificates'][0].title, 'Certificate of Appreciation – Event Head')

    def test_navbar_and_footer_navigation(self):
        """Verify achievements link is present in navbar and footer."""
        self.assertContains(self.response, reverse('core:achievements'))
        home_res = self.client.get(reverse('core:home'))
        self.assertContains(home_res, reverse('core:achievements'))

    def test_admin_registration(self):
        """Verify Achievement and Certificate are registered in Django Admin."""
        self.assertIn(Achievement, admin.site._registry)
        self.assertIn(Certificate, admin.site._registry)

    @override_settings(MEDIA_ROOT=tempfile.gettempdir())
    def test_certificate_upload_and_properties(self):
        """Test uploading both image and PDF files to Certificate and verifying model properties."""
        # Test image upload
        image_content = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01\x08\x06\x00\x00\x00\x1f\x15c4\x00\x00\x00\nIDATx\x9cc\x00\x01\x00\x00\x05\x00\x01\r\n-\xb4\x00\x00\x00\x00IEND\xaeB`\x82'
        uploaded_image = SimpleUploadedFile('test_cert.png', image_content, content_type='image/png')
        cert_img = Certificate.objects.create(
            title='Test Python Certification',
            issuing_organization='Himalayan WhiteHouse',
            category='technical',
            certificate_file=uploaded_image,
        )
        self.assertTrue(cert_img.has_file)
        self.assertTrue(cert_img.is_image)
        self.assertFalse(cert_img.is_pdf)
        self.assertEqual(cert_img.file_extension, 'PNG')

        # Test PDF upload
        pdf_content = b'%PDF-1.4\n1 0 obj\n<<>>\nendobj\ntrailer\n<<>>\n%%EOF'
        uploaded_pdf = SimpleUploadedFile('test_cert.pdf', pdf_content, content_type='application/pdf')
        cert_pdf = Certificate.objects.create(
            title='Test Hackathon Certificate',
            issuing_organization='Sankalpa',
            category='hackathon',
            certificate_file=uploaded_pdf,
        )
        self.assertTrue(cert_pdf.has_file)
        self.assertFalse(cert_pdf.is_image)
        self.assertTrue(cert_pdf.is_pdf)
        self.assertEqual(cert_pdf.file_extension, 'PDF')


class PortfolioContactAndCVTests(TestCase):
    def setUp(self):
        self.contact_url = reverse('core:contact')
        self.download_cv_url = reverse('core:download_cv')

    def test_contact_page_status_and_templates(self):
        """Verify contact page returns 200 OK and renders contact.html extending base.html."""
        res = self.client.get(self.contact_url)
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'core/contact.html')
        self.assertTemplateUsed(res, 'core/base.html')

    def test_contact_information_and_social_links(self):
        """Verify personal contact coordinates, email, location, GitHub and LinkedIn links."""
        res = self.client.get(self.contact_url)
        self.assertContains(res, 'Bhuwan Raj Pandey')
        self.assertContains(res, 'officialbhuwan454@gmail.com')
        self.assertContains(res, 'Kathmandu, Nepal')
        self.assertContains(res, 'https://www.linkedin.com/in/bhuwan-pandey-2b829a2ba/')
        self.assertContains(res, 'https://github.com/Bhuwan-110')
        self.assertContains(res, 'target="_blank"')
        self.assertContains(res, 'rel="noopener noreferrer"')

    def test_contact_form_valid_submission(self):
        """Verify a valid contact form submission stores message in DB and redirects with success flash."""
        payload = {
            'name': 'Sarah Connor',
            'email': 'sarah@example.com',
            'subject': 'Python Backend Internship Offer',
            'message': 'We reviewed your portfolio and would like to discuss a summer internship opportunity.',
        }
        res = self.client.post(self.contact_url, payload, follow=True)
        self.assertEqual(res.status_code, 200)
        self.assertContains(res, 'received securely')
        self.assertTrue(ContactMessage.objects.filter(email='sarah@example.com').exists())
        saved_msg = ContactMessage.objects.get(email='sarah@example.com')
        self.assertEqual(saved_msg.name, 'Sarah Connor')
        self.assertEqual(saved_msg.subject, 'Python Backend Internship Offer')
        self.assertFalse(saved_msg.is_read)

    def test_contact_form_invalid_submissions(self):
        """Verify invalid contact form inputs are rejected and error feedback is presented."""
        # 1. Invalid email
        payload_bad_email = {
            'name': 'Test User',
            'email': 'not-a-valid-email',
            'subject': 'Hello',
            'message': 'Valid length message text here.',
        }
        res1 = self.client.post(self.contact_url, payload_bad_email)
        self.assertEqual(res1.status_code, 200)
        self.assertContains(res1, 'Enter a valid email address')

        # 2. Too short message
        payload_short_msg = {
            'name': 'Test User',
            'email': 'valid@example.com',
            'subject': 'Hello',
            'message': 'Hi',
        }
        res2 = self.client.post(self.contact_url, payload_short_msg)
        self.assertEqual(res2.status_code, 200)
        self.assertContains(res2, 'at least 10 characters')

    def test_contact_form_spam_honeypot(self):
        """Verify automated spam bots triggering the hidden honeypot are rejected."""
        payload_spam = {
            'name': 'Spam Bot',
            'email': 'bot@spammer.com',
            'subject': 'Buy crypto now',
            'message': 'Visit our shady website right now for free tokens.',
            'website_url': 'http://automated-spam-attack.com',
        }
        res = self.client.post(self.contact_url, payload_spam)
        self.assertEqual(res.status_code, 200)
        self.assertContains(res, 'Spam submission detected')
        self.assertFalse(ContactMessage.objects.filter(email='bot@spammer.com').exists())

    def test_dynamic_cv_download_when_active(self):
        """Verify downloading the active CV returns PDF content with standard filename."""
        res = self.client.get(self.download_cv_url)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res['Content-Type'], 'application/pdf')
        self.assertIn('attachment;', res['Content-Disposition'])
        self.assertIn('filename="Bhuwan_Raj_Pandey_CV.pdf"', res['Content-Disposition'])

    def test_dynamic_cv_download_when_no_active_cv(self):
        """Verify graceful redirection when no CV is marked as active."""
        CurriculumVitae.objects.update(is_active=False)
        res = self.client.get(self.download_cv_url, follow=True)
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'core/contact.html')
        self.assertContains(res, 'CV update in progress')

    def test_dynamic_cv_download_when_file_missing_on_storage(self):
        """Verify graceful redirection when the active CV record points to a missing file on storage."""
        active_cv = CurriculumVitae.get_active_cv()
        active_cv.pdf_file.name = 'cv/missing_file_on_disk.pdf'
        active_cv.save()
        res = self.client.get(self.download_cv_url, follow=True)
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'core/contact.html')
        self.assertContains(res, 'CV update in progress')

    def test_cv_download_links_present_in_all_views(self):
        """Verify Homepage, Navbar, and Contact page all provide the Download CV link."""
        home_res = self.client.get(reverse('core:home'))
        self.assertContains(home_res, self.download_cv_url)

        about_res = self.client.get(reverse('core:about'))
        self.assertContains(about_res, self.download_cv_url)  # From navbar

        contact_res = self.client.get(self.contact_url)
        self.assertContains(contact_res, self.download_cv_url)

    @override_settings(MEDIA_ROOT=tempfile.gettempdir())
    def test_cv_single_active_constraint(self):
        """Verify saving a new active CV automatically deactivates all previous active CVs."""
        # Ensure active CV exists
        cv1 = CurriculumVitae.objects.create(
            title='CV Version 1',
            pdf_file=SimpleUploadedFile('cv1.pdf', b'%PDF-1.4\ntest1', content_type='application/pdf'),
            is_active=True
        )
        self.assertTrue(CurriculumVitae.objects.get(pk=cv1.pk).is_active)

        # Upload Version 2 as active
        cv2 = CurriculumVitae.objects.create(
            title='CV Version 2',
            pdf_file=SimpleUploadedFile('cv2.pdf', b'%PDF-1.4\ntest2', content_type='application/pdf'),
            is_active=True
        )
        # Check cv1 is now inactive and cv2 is active
        self.assertFalse(CurriculumVitae.objects.get(pk=cv1.pk).is_active)
        self.assertTrue(CurriculumVitae.objects.get(pk=cv2.pk).is_active)
        self.assertEqual(CurriculumVitae.get_active_cv().pk, cv2.pk)

    def test_admin_registration(self):
        """Verify ContactMessage and CurriculumVitae are registered in Django Admin."""
        self.assertIn(ContactMessage, admin.site._registry)
        self.assertIn(CurriculumVitae, admin.site._registry)

    def test_navbar_and_footer_link_to_contact(self):
        """Verify navbar and footer link to the dedicated contact page."""
        home_res = self.client.get(reverse('core:home'))
        self.assertContains(home_res, reverse('core:contact'))
        contact_res = self.client.get(self.contact_url)
        self.assertContains(contact_res, reverse('core:contact'))


class PortfolioAdminAndCMSTests(TestCase):
    def setUp(self):
        self.staff_user = User.objects.create_user(
            username='staffuser',
            email='staff@bhuwan.dev',
            password='secretpassword123',
            is_staff=True
        )
        self.regular_user = User.objects.create_user(
            username='regularuser',
            email='regular@bhuwan.dev',
            password='secretpassword123',
            is_staff=False
        )
        self.dashboard_url = reverse('core:admin_dashboard')
        self.admin_index_url = reverse('admin:index')

    def test_dashboard_access_control(self):
        """Verify anonymous and non-staff users cannot access /dashboard/ and staff can."""
        # Anonymous
        anon_res = self.client.get(self.dashboard_url)
        self.assertEqual(anon_res.status_code, 302)
        self.assertIn('/admin/login/', anon_res['Location'])

        # Regular user
        self.client.login(username='regularuser', password='secretpassword123')
        reg_res = self.client.get(self.dashboard_url)
        self.assertEqual(reg_res.status_code, 302)
        self.assertIn('/admin/login/', reg_res['Location'])
        self.client.logout()

        # Staff user
        self.client.login(username='staffuser', password='secretpassword123')
        staff_res = self.client.get(self.dashboard_url)
        self.assertEqual(staff_res.status_code, 200)
        self.assertTemplateUsed(staff_res, 'admin/dashboard.html')
        self.assertContains(staff_res, 'Portfolio CMS Executive Dashboard')
        self.assertContains(staff_res, 'Projects')
        self.assertContains(staff_res, 'Contact Inquiries')

    def test_custom_admin_index_and_branding(self):
        """Verify staff visiting /admin/ sees the custom branding and live CMS banner."""
        self.client.login(username='staffuser', password='secretpassword123')
        res = self.client.get(self.admin_index_url)
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'admin/index.html')
        self.assertContains(res, 'BHUWAN.DEV')
        self.assertContains(res, 'Executive Dashboard')
        self.assertContains(res, 'Live CMS')

    def test_admin_registrations_step9(self):
        """Verify Profile and all core models are registered in Django admin."""
        self.assertIn(Profile, admin.site._registry)
        self.assertIn(Project, admin.site._registry)
        self.assertIn(Experience, admin.site._registry)
        self.assertIn(Skill, admin.site._registry)
        self.assertIn(Achievement, admin.site._registry)
        self.assertIn(Certificate, admin.site._registry)

    def test_profile_single_active_constraint(self):
        """Verify creating or activating a second profile deactivates previous active profiles."""
        p1 = Profile.objects.create(
            full_name='Bhuwan Primary',
            professional_title='Developer 1',
            email='p1@bhuwan.dev',
            location='Kathmandu',
            is_active=True
        )
        self.assertTrue(Profile.objects.get(pk=p1.pk).is_active)
        self.assertEqual(Profile.get_active_profile().pk, p1.pk)

        p2 = Profile.objects.create(
            full_name='Bhuwan Secondary',
            professional_title='Developer 2',
            email='p2@bhuwan.dev',
            location='Lalitpur',
            is_active=True
        )
        self.assertFalse(Profile.objects.get(pk=p1.pk).is_active)
        self.assertTrue(Profile.objects.get(pk=p2.pk).is_active)
        self.assertEqual(Profile.get_active_profile().pk, p2.pk)

    def test_dynamic_profile_reflection_on_public_pages(self):
        """Verify modifying active Profile dynamically changes the content on Home and About pages."""
        profile = Profile.objects.filter(is_active=True).first()
        if not profile:
            profile = Profile.objects.create(
                full_name='Original Name',
                professional_title='Original Title',
                email='orig@bhuwan.dev',
                location='Original City',
                career_objective='Original Ambition to be an AI Engineer.',
                is_active=True
            )
        profile.full_name = 'Bhuwan Dynamic Pandey'
        profile.professional_title = 'Senior Python & AI Architect'
        profile.location = 'Pokhara, Nepal'
        profile.career_objective = 'Pioneering production AI systems for modern computing.'
        profile.save()

        # Homepage
        home_res = self.client.get(reverse('core:home'))
        self.assertEqual(home_res.status_code, 200)
        self.assertContains(home_res, 'Bhuwan Dynamic Pandey')
        self.assertContains(home_res, 'Senior Python &amp; AI Architect')
        self.assertContains(home_res, 'Pokhara, Nepal')
        self.assertContains(home_res, 'Pioneering production AI systems for modern computing.')

        # About page
        about_res = self.client.get(reverse('core:about'))
        self.assertEqual(about_res.status_code, 200)
        self.assertContains(about_res, 'Bhuwan Dynamic Pandey')
        self.assertContains(about_res, 'Senior Python &amp; AI Architect')
        self.assertContains(about_res, 'Pokhara, Nepal')
        self.assertContains(about_res, 'Pioneering production AI systems for modern computing.')

    def test_project_is_published_filtering(self):
        """Verify unpublished projects are excluded from project list and detail returns 404."""
        pub_proj = Project.objects.create(
            title='Published Project Alpha',
            slug='published-project-alpha',
            category='web_development',
            status='Completed',
            short_description='Visible project',
            overview='Visible overview',
            is_published=True,
            order=1
        )
        unpub_proj = Project.objects.create(
            title='Draft Secret Project Beta',
            slug='draft-secret-project-beta',
            category='machine_learning',
            status='In Progress',
            short_description='Hidden draft project',
            overview='Hidden overview',
            is_published=False,
            order=2
        )

        # Projects list view
        res = self.client.get(reverse('core:projects'))
        self.assertEqual(res.status_code, 200)
        self.assertContains(res, 'Published Project Alpha')
        self.assertNotContains(res, 'Draft Secret Project Beta')

        # Detail view for published
        detail_pub = self.client.get(reverse('core:project_detail', kwargs={'slug': pub_proj.slug}))
        self.assertEqual(detail_pub.status_code, 200)
        self.assertContains(detail_pub, 'Published Project Alpha')

        # Detail view for unpublished returns 404
        detail_unpub = self.client.get(reverse('core:project_detail', kwargs={'slug': unpub_proj.slug}))
        self.assertEqual(detail_unpub.status_code, 404)

    def test_experience_is_published_filtering(self):
        """Verify unpublished experiences are hidden from experience page."""
        unpub_exp = Experience.objects.create(
            title='Secret Covert Role',
            role='Operative',
            institution='Classified Org',
            category='professional',
            period='2024',
            description='This should not be seen on public site.',
            is_published=False
        )
        res = self.client.get(reverse('core:experience'))
        self.assertEqual(res.status_code, 200)
        self.assertNotContains(res, 'Secret Covert Role')

    def test_skill_is_visible_filtering(self):
        """Verify invisible skills are hidden from skills page."""
        hidden_skill = Skill.objects.create(
            name='Obscure Assembly Lang',
            category='languages',
            proficiency='Basic Familiarity',
            is_visible=False
        )
        res = self.client.get(reverse('core:skills'))
        self.assertEqual(res.status_code, 200)
        self.assertNotContains(res, 'Obscure Assembly Lang')

    def test_achievement_and_certificate_is_published_filtering(self):
        """Verify unpublished achievements and certificates are hidden."""
        unpub_achieve = Achievement.objects.create(
            title='Unpublished Private Award',
            role='Honoree',
            organization='Confidential Context',
            category='academic',
            period='2025',
            description='Not ready to publish.',
            is_published=False
        )
        unpub_cert = Certificate.objects.create(
            title='Draft Certification Title',
            issuing_organization='Draft Institute',
            issue_date='2025-01-01',
            is_published=False
        )
        res = self.client.get(reverse('core:achievements'))
        self.assertEqual(res.status_code, 200)
        self.assertNotContains(res, 'Unpublished Private Award')
        self.assertNotContains(res, 'Draft Certification Title')

    @override_settings(MEDIA_ROOT=tempfile.gettempdir())
    def test_project_screenshot_inline_support(self):
        """Verify multiple screenshots can be attached to a project and render on detail page."""
        proj = Project.objects.create(
            title='Multi Screenshot Project',
            slug='multi-screenshot-proj',
            category='web_development',
            status='Active',
            short_description='Testing screenshots',
            overview='Project with gallery screenshots',
            is_published=True
        )
        ProjectScreenshot.objects.create(
            project=proj,
            image=SimpleUploadedFile('shot1.png', b'\x89PNG\r\n\x1a\n\x00\x00', content_type='image/png'),
            caption='Admin Dashboard Screenshot 1',
            order=1
        )
        ProjectScreenshot.objects.create(
            project=proj,
            image=SimpleUploadedFile('shot2.png', b'\x89PNG\r\n\x1a\n\x00\x00', content_type='image/png'),
            caption='Analytics Graph Screenshot 2',
            order=2
        )
        self.assertEqual(proj.screenshots.count(), 2)

        res = self.client.get(reverse('core:project_detail', kwargs={'slug': proj.slug}))
        self.assertEqual(res.status_code, 200)
        self.assertContains(res, 'Project Screenshots &amp; Visuals')
        self.assertContains(res, 'Admin Dashboard Screenshot 1')
        self.assertContains(res, 'Analytics Graph Screenshot 2')



