import os
from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse


class Profile(models.Model):
    """
    Model representing Bhuwan Raj Pandey's personal and professional profile.
    Editable dynamically through Django Admin.
    """
    full_name = models.CharField(max_length=150, default='Bhuwan Raj Pandey')
    professional_title = models.CharField(
        max_length=200, 
        default='Aspiring Software Developer | Python & AI Enthusiast'
    )
    short_bio = models.TextField(
        help_text="Short introductory summary for hero section and card previews"
    )
    detailed_bio = models.TextField(
        help_text="Detailed biographical introduction for the About page (paragraphs separated by blank lines)"
    )
    profile_photo = models.ImageField(
        upload_to='profile/', 
        blank=True, 
        null=True,
        help_text="Upload your personal profile portrait (JPG, PNG, WebP)"
    )
    email = models.EmailField(default='officialbhuwan454@gmail.com')
    location = models.CharField(max_length=150, default='Kathmandu, Nepal')
    phone = models.CharField(max_length=50, blank=True, help_text="Optional contact number for public display")
    linkedin_url = models.URLField(default='https://www.linkedin.com/in/bhuwan-pandey-2b829a2ba/')
    github_url = models.URLField(default='https://github.com/Bhuwan-110')
    career_objective = models.TextField(
        blank=True,
        help_text="Career goal statement for recruiters and internship programs"
    )
    availability_status = models.CharField(
        max_length=100, 
        default='Available for IT Internships',
        help_text="e.g. Available for IT Internships, Open to Collaboration"
    )
    institution = models.CharField(
        max_length=200, 
        default='Himalayan WhiteHouse International College'
    )
    degree = models.CharField(
        max_length=200, 
        default='Bachelor of Information Technology (BIT)'
    )
    current_semester = models.CharField(max_length=100, default='7th Semester')
    graduation_year = models.CharField(max_length=100, default='2027 (Expected)')
    is_active = models.BooleanField(
        default=True,
        help_text="Only one profile can be active at a time. Saving an active profile deactivates others."
    )
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Personal Profile'
        verbose_name_plural = 'Personal Profile'

    def __str__(self):
        status = " [ACTIVE]" if self.is_active else ""
        return f"{self.full_name} - {self.professional_title}{status}"

    def save(self, *args, **kwargs):
        if self.is_active:
            Profile.objects.exclude(pk=self.pk).update(is_active=False)
        super().save(*args, **kwargs)

    @classmethod
    def get_active_profile(cls):
        """Returns the active profile or None."""
        return cls.objects.filter(is_active=True).first()

    def get_about_paragraphs(self):
        """Returns non-empty paragraphs from detailed_bio."""
        if not self.detailed_bio:
            return []
        return [p.strip() for p in self.detailed_bio.split('\n') if p.strip()]

    def get_short_bio_paragraphs(self):
        """Returns non-empty paragraphs from short_bio."""
        if not self.short_bio:
            return []
        return [p.strip() for p in self.short_bio.split('\n') if p.strip()]


class Experience(models.Model):
    """
    Model representing professional, leadership, club, and event organizing experiences.
    """
    CATEGORY_CHOICES = [
        ('professional', 'Professional Experience'),
        ('teaching', 'Teaching Experience'),
        ('leadership', 'Leadership Experience'),
        ('event', 'Event Management'),
        ('workshop', 'Workshops & Programs'),
        ('volunteering', 'Volunteering'),
    ]

    title = models.CharField(max_length=200, help_text="Event or organization title")
    role = models.CharField(max_length=200, help_text="Role or leadership position held")
    institution = models.CharField(max_length=200, default='Himalayan WhiteHouse International College')
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='leadership')
    period = models.CharField(max_length=100, help_text="e.g. 2025 – 2026 or 3-Day Hackathon")
    duration_stats = models.CharField(max_length=250, blank=True, help_text="Verified stats or specialization")
    start_date = models.DateField(blank=True, null=True, help_text="Start date (optional)")
    end_date = models.DateField(blank=True, null=True, help_text="End date (leave blank if currently active)")
    is_current = models.BooleanField(default=False, help_text="Currently holding this role")
    organization_logo = models.ImageField(upload_to='experiences/logos/', blank=True, null=True, help_text="Organization logo")
    description = models.TextField(help_text="Overview of the experience and context")
    responsibilities = models.TextField(blank=True, help_text="Responsibilities or key highlights separated by newlines")
    skills = models.CharField(max_length=350, blank=True, default='', help_text="Comma-separated skills demonstrated")
    icon = models.CharField(max_length=50, default='bi-briefcase-fill')
    is_featured = models.BooleanField(default=True, help_text="Highlight on homepage or featured lists")
    is_published = models.BooleanField(default=True, help_text="Display on public experience page")
    order = models.PositiveIntegerField(default=0, help_text="Ordering index")

    class Meta:
        ordering = ['order', 'id']
        verbose_name = 'Experience & Leadership'
        verbose_name_plural = 'Experiences & Leadership'

    def __str__(self):
        return f"{self.title} ({self.role})"

    def get_responsibilities_list(self):
        """Returns non-empty responsibility items as a list."""
        if not self.responsibilities:
            return []
        return [r.strip() for r in self.responsibilities.split('\n') if r.strip()]

    def get_skills_list(self):
        """Returns non-empty skills as a stripped list."""
        if not self.skills:
            return []
        return [s.strip() for s in self.skills.split(',') if s.strip()]


class Project(models.Model):
    """
    Model representing portfolio projects across Python/AI, Web, IoT, and Programming Fundamentals.
    """
    CATEGORY_CHOICES = [
        ('python-ai', 'Python / AI'),
        ('web-development', 'Web Development'),
        ('iot', 'IoT'),
        ('programming-fundamentals', 'Programming Fundamentals'),
    ]

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, help_text="Unique URL identifier")
    subtitle = models.CharField(max_length=250, blank=True, help_text="Nepali full title or secondary subtitle")
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    status = models.CharField(max_length=100, default='Academic project', help_text="e.g. Prototype, College project, Academic project")
    short_description = models.TextField(help_text="Concise description for cards and previews")
    overview = models.TextField(help_text="Detailed project overview for the individual detail page")
    problem_statement = models.TextField(blank=True, help_text="The core problem the project addresses")
    objective = models.TextField(blank=True, help_text="The primary objectives of the project")
    technologies = models.CharField(max_length=300, help_text="Comma-separated technologies list (e.g. Python, Django, NLP)")
    features_or_concepts = models.TextField(blank=True, help_text="Main features, concepts, or modules separated by newlines")
    my_contribution = models.TextField(blank=True, help_text="Specific personal engineering contribution")
    github_url = models.URLField(blank=True, null=True, help_text="GitHub repository URL if publicly available")
    live_url = models.URLField(blank=True, null=True, help_text="Live demo or hosted application URL")
    image = models.ImageField(upload_to='projects/', blank=True, null=True, help_text="Main project cover image or architectural diagram")
    featured = models.BooleanField(default=False, help_text="Highlight on the homepage")
    is_published = models.BooleanField(default=True, help_text="Publish project on public portfolio")
    order = models.PositiveIntegerField(default=0, help_text="Ordering index")
    created_at = models.DateTimeField(auto_now_add=True, null=True, help_text="Creation timestamp")
    updated_at = models.DateTimeField(auto_now=True, help_text="Last updated timestamp")

    class Meta:
        ordering = ['order', 'id']
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('core:project_detail', kwargs={'slug': self.slug})

    def get_technologies_list(self):
        """Returns individual technologies as a stripped list."""
        if not self.technologies:
            return []
        return [t.strip() for t in self.technologies.split(',') if t.strip()]

    def get_features_list(self):
        """Returns feature lines as a stripped list."""
        if not self.features_or_concepts:
            return []
        return [f.strip() for f in self.features_or_concepts.split('\n') if f.strip()]


class ProjectScreenshot(models.Model):
    """
    Additional screenshots or system diagrams for a portfolio project.
    """
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='screenshots')
    image = models.ImageField(upload_to='projects/screenshots/', help_text="Upload screenshot or architectural diagram")
    caption = models.CharField(max_length=200, blank=True, help_text="Optional caption or description")
    order = models.PositiveIntegerField(default=0, help_text="Display ordering index")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', 'id']
        verbose_name = 'Project Screenshot'
        verbose_name_plural = 'Project Screenshots'

    def __str__(self):
        return f"Screenshot for {self.project.title} ({self.caption or f'Image #{self.id}'})"


class Skill(models.Model):
    """
    Model representing technical skills across languages, frontend, backend, database,
    traditional tools, AI-assisted development tools, and exploration interests.
    """
    CATEGORY_CHOICES = [
        ('languages', 'Programming Languages'),
        ('frontend', 'Frontend Development'),
        ('backend', 'Backend Development'),
        ('database', 'Database'),
        ('tools', 'Development Tools'),
        ('ai-assisted', 'AI-Assisted Development & Vibe Coding'),
        ('interests', 'Areas of Interest'),
    ]

    name = models.CharField(max_length=150)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    proficiency = models.CharField(
        max_length=100, 
        blank=True, 
        help_text="Provisional proficiency level (e.g. Intermediate / Developing, Basic, etc.)"
    )
    description = models.CharField(max_length=255, blank=True, help_text="Short description or key application")
    icon = models.CharField(max_length=50, blank=True, help_text="Bootstrap icon class (e.g. bi-filetype-py)")
    custom_logo = models.CharField(
        max_length=150, 
        blank=True, 
        help_text="Path to static logo (e.g. core/images/icons/google-antigravity.svg)"
    )
    is_currently_learning = models.BooleanField(default=False, help_text="Mark as currently active in learning workflow")
    is_future_interest = models.BooleanField(default=False, help_text="Mark as future learning interest")
    is_visible = models.BooleanField(default=True, help_text="Display on public skills page")
    order = models.PositiveIntegerField(default=0, help_text="Ordering index")

    class Meta:
        ordering = ['order', 'id']
        verbose_name = 'Technical Skill'
        verbose_name_plural = 'Technical Skills'

    def __str__(self):
        return f"{self.name} [{self.get_category_display()}] - {self.proficiency}"


class LearningGoal(models.Model):
    """
    Model representing milestones in the student learning journey.
    """
    STAGE_CHOICES = [
        ('current', 'Current Learning Focus'),
        ('future', 'Future Learning Interest'),
    ]

    title = models.CharField(max_length=200)
    stage = models.CharField(max_length=20, choices=STAGE_CHOICES, default='current')
    description = models.TextField(blank=True, help_text="Details of what is being learned or explored")
    badge_label = models.CharField(max_length=100, blank=True, help_text="e.g. Active Daily Focus, Exploration Area")
    icon = models.CharField(max_length=50, default='bi-compass', help_text="Bootstrap icon class")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'id']
        verbose_name = 'Learning Journey Goal'
        verbose_name_plural = 'Learning Journey Goals'

    def __str__(self):
        return f"[{self.get_stage_display()}] {self.title}"


class Achievement(models.Model):
    """
    Model representing major extracurricular, leadership, and technical achievements.
    """
    CATEGORY_CHOICES = [
        ('hackathon', 'Hackathons & Competitions'),
        ('leadership', 'Club & Executive Leadership'),
        ('workshop', 'Workshops & Programs'),
        ('academic', 'Academic & Extracurricular'),
    ]

    title = models.CharField(max_length=200, help_text="e.g. Sankalpa Hackathon, Whitehouse Innovators – IT Club")
    role = models.CharField(max_length=200, blank=True, help_text="e.g. Event Head, Main Lead, Vice President")
    organization = models.CharField(max_length=200, default='Himalayan WhiteHouse International College')
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='leadership')
    period = models.CharField(max_length=100, help_text="e.g. 3-Day Hackathon, 2025 – 2026, One Day")
    metrics_summary = models.CharField(max_length=250, blank=True, help_text="e.g. 15 Teams | 60 Participants")
    description = models.TextField(help_text="Overview of the achievement and recognized outcome")
    key_highlights = models.TextField(blank=True, help_text="Highlights or takeaways separated by newlines")
    icon = models.CharField(max_length=50, default='bi-trophy-fill', help_text="Bootstrap icon class")
    event_photo = models.ImageField(upload_to='achievements/photos/', blank=True, null=True, help_text="Event photograph")
    is_published = models.BooleanField(default=True, help_text="Display on public achievements page")
    order = models.PositiveIntegerField(default=0, help_text="Ordering index")
    featured = models.BooleanField(default=True, help_text="Show in prominent achievements grid")

    class Meta:
        ordering = ['order', 'id']
        verbose_name = 'Achievement'
        verbose_name_plural = 'Achievements'

    def __str__(self):
        return f"{self.title} ({self.role})" if self.role else self.title

    def get_highlights_list(self):
        """Returns key highlights as a stripped list."""
        if not self.key_highlights:
            return []
        return [h.strip() for h in self.key_highlights.split('\n') if h.strip()]

    def has_certificate(self):
        """Checks if any verified certificate is attached to this achievement."""
        return self.certificates.filter(certificate_file__isnull=False).exclude(certificate_file='').exists()


class Certificate(models.Model):
    """
    Model representing verified certificates, credentials, and course completions.
    Supports image (JPG, PNG, WebP) and PDF document uploads via Django Admin.
    """
    CATEGORY_CHOICES = [
        ('leadership', 'Leadership & Event Organizing'),
        ('hackathon', 'Hackathon & Competitions'),
        ('workshop', 'Workshops & Programs'),
        ('technical', 'Technical & Development'),
        ('academic', 'Academic & Extracurricular'),
    ]

    title = models.CharField(max_length=200, help_text="Certificate title (e.g. Certificate of Executive Leadership)")
    issuing_organization = models.CharField(max_length=200, help_text="e.g. Himalayan WhiteHouse International College, Whitehouse Innovators")
    issue_date = models.DateField(blank=True, null=True, help_text="Exact issue date if known")
    issue_date_display = models.CharField(max_length=100, blank=True, help_text="Display date text (e.g. '2025 – 2026', '2025')")
    description = models.TextField(blank=True, help_text="Short description of the certificate or recognized contribution")
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='leadership')
    certificate_file = models.FileField(
        upload_to='certificates/',
        blank=True,
        null=True,
        help_text="Upload certificate image (JPG, PNG, WebP) or PDF document"
    )
    achievement = models.ForeignKey(
        Achievement,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='certificates',
        help_text="Optionally link this certificate to a specific achievement"
    )
    credential_id = models.CharField(max_length=150, blank=True, help_text="Credential ID or registration number if available")
    credential_url = models.URLField(blank=True, null=True, help_text="External verification URL if available")
    is_temporary_placeholder = models.BooleanField(
        default=False, 
        help_text="Mark if this is a temporary preview placeholder file pending final official scan upload"
    )
    is_published = models.BooleanField(default=True, help_text="Display on public certificates gallery")
    order = models.PositiveIntegerField(default=0, help_text="Ordering index")
    is_featured = models.BooleanField(default=True, help_text="Show prominently in certificate gallery")

    class Meta:
        ordering = ['order', 'id']
        verbose_name = 'Certificate'
        verbose_name_plural = 'Certificates'

    def __str__(self):
        return f"{self.title} - {self.issuing_organization}"

    @property
    def has_file(self):
        return bool(self.certificate_file)

    @property
    def is_pdf(self):
        if not self.certificate_file:
            return False
        return self.certificate_file.name.lower().endswith('.pdf')

    @property
    def is_image(self):
        if not self.certificate_file:
            return False
        ext = self.certificate_file.name.lower().split('.')[-1]
        return ext in ['jpg', 'jpeg', 'png', 'webp', 'gif']

    @property
    def file_extension(self):
        if not self.certificate_file:
            return ''
        return self.certificate_file.name.lower().split('.')[-1].upper()

    def get_date_display(self):
        if self.issue_date_display:
            return self.issue_date_display
        if self.issue_date:
            return self.issue_date.strftime('%B %Y')
        return 'Date on Record'


def validate_cv_file(file):
    """
    Validates that the uploaded CV file is a genuine PDF and within the 10MB size limit.
    """
    ext = os.path.splitext(file.name)[1].lower()
    if ext != '.pdf':
        raise ValidationError("Only PDF files (.pdf) are allowed for CV uploads.")

    max_size = 10 * 1024 * 1024  # 10 MB
    if file.size > max_size:
        raise ValidationError(f"File size exceeds 10MB limit (Current size: {file.size / (1024 * 1024):.1f}MB).")

    # Verify PDF magic signature (%PDF-)
    try:
        file.seek(0)
        header = file.read(5)
        file.seek(0)
        if header != b'%PDF-':
            raise ValidationError("The uploaded file does not appear to be a valid PDF document.")
    except Exception:
        pass


class CurriculumVitae(models.Model):
    """
    Model representing uploaded CV / Resume PDF documents.
    Ensures only one active CV exists at any time.
    """
    title = models.CharField(
        max_length=200, 
        default='Bhuwan Raj Pandey - Professional CV',
        help_text="Descriptive title (e.g. Bhuwan Raj Pandey - Python & AI CV 2026)"
    )
    pdf_file = models.FileField(
        upload_to='cv/',
        validators=[validate_cv_file],
        help_text="Upload CV in PDF format (maximum size: 10MB)"
    )
    uploaded_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(
        default=True,
        help_text="Mark as the currently active CV. Activating this automatically deactivates all other CVs."
    )
    notes = models.CharField(max_length=255, blank=True, help_text="Optional version notes for admin reference")

    class Meta:
        ordering = ['-is_active', '-uploaded_at']
        verbose_name = 'Curriculum Vitae (CV)'
        verbose_name_plural = 'Curriculum Vitae (CVs)'

    def __str__(self):
        status = " [ACTIVE]" if self.is_active else ""
        return f"{self.title}{status}"

    def save(self, *args, **kwargs):
        """
        When this CV is saved as active, automatically deactivate all other CVs
        to enforce the business rule that only one active CV exists.
        """
        if self.is_active:
            CurriculumVitae.objects.exclude(pk=self.pk).update(is_active=False)
        super().save(*args, **kwargs)

    @classmethod
    def get_active_cv(cls):
        """Returns the currently active CV, or None."""
        return cls.objects.filter(is_active=True).first()

    @property
    def file_size_display(self):
        if not self.pdf_file:
            return 'No file'
        try:
            size = self.pdf_file.size
            if size < 1024 * 1024:
                return f"{size / 1024:.1f} KB"
            return f"{size / (1024 * 1024):.2f} MB"
        except Exception:
            return 'Unknown'


class ContactMessage(models.Model):
    """
    Model representing messages submitted via the website contact form.
    """
    name = models.CharField(max_length=150, help_text="Full Name")
    email = models.EmailField(help_text="Email Address")
    subject = models.CharField(max_length=200, help_text="Subject")
    message = models.TextField(help_text="Message Content")
    created_at = models.DateTimeField(auto_now_add=True, help_text="Submission Timestamp")
    is_read = models.BooleanField(default=False, help_text="Mark as read")
    replied = models.BooleanField(default=False, help_text="Mark as replied")
    notes = models.TextField(blank=True, help_text="Admin internal notes")

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Contact Message'
        verbose_name_plural = 'Contact Messages'

    def __str__(self):
        read_badge = "✓ Read" if self.is_read else "★ New"
        return f"[{read_badge}] {self.name} - {self.subject}"


