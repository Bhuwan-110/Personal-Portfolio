from django.contrib import admin
from django.utils.html import format_html
from .models import (
    Achievement, Certificate, ContactMessage, CurriculumVitae,
    Experience, LearningGoal, Profile, Project, ProjectScreenshot, Skill
)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'professional_title', 'email', 'location', 'availability_status', 'is_active', 'photo_preview', 'updated_at')
    list_editable = ('is_active',)
    search_fields = ('full_name', 'professional_title', 'email', 'location', 'short_bio')
    readonly_fields = ('photo_preview_large', 'updated_at')
    fieldsets = (
        ('Personal Identity & Active Status', {
            'fields': ('full_name', 'professional_title', 'is_active', 'availability_status')
        }),
        ('Portrait & Photograph', {
            'fields': ('profile_photo', 'photo_preview_large'),
            'description': 'Upload your profile photo (PNG, JPG, WebP). If left blank, the website automatically uses the default professional photo.'
        }),
        ('Biographies & Introductions', {
            'fields': ('short_bio', 'detailed_bio', 'career_objective'),
            'description': 'Paragraphs in detailed bio can be separated with blank lines.'
        }),
        ('Academic Details', {
            'fields': ('institution', 'degree', 'current_semester', 'graduation_year')
        }),
        ('Contact & Public Social Coordinates', {
            'fields': ('email', 'location', 'phone', 'linkedin_url', 'github_url')
        }),
    )

    def photo_preview(self, obj):
        if obj.profile_photo:
            return format_html('<img src="{}" style="width: 34px; height: 34px; border-radius: 50%; object-fit: cover; border: 1px solid #cbd5e1;" />', obj.profile_photo.url)
        return 'Default'
    photo_preview.short_description = 'Photo'

    def photo_preview_large(self, obj):
        if obj.profile_photo:
            return format_html('<img src="{}" style="max-height: 180px; border-radius: 8px; border: 1px solid #cbd5e1; box-shadow: 0 2px 4px rgba(0,0,0,0.08);" /><br><small style="color: #64748b;">Current uploaded profile portrait</small>', obj.profile_photo.url)
        return 'No custom photo uploaded yet. Using default placeholder image.'
    photo_preview_large.short_description = 'Photo Preview'


class ProjectScreenshotInline(admin.TabularInline):
    model = ProjectScreenshot
    extra = 1
    fields = ('image', 'caption', 'order', 'preview')
    readonly_fields = ('preview',)

    def preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height: 45px; border-radius: 4px;" />', obj.image.url)
        return 'No image'


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('title', 'role', 'institution', 'category', 'period', 'is_published', 'order')
    list_filter = ('category', 'is_published', 'is_current')
    search_fields = ('title', 'role', 'institution', 'description', 'skills')
    list_editable = ('is_published', 'order')
    ordering = ('order', 'id')
    fieldsets = (
        ('Event / Club / Organization Information', {
            'fields': ('title', 'role', 'institution', 'category', 'icon', 'organization_logo', 'is_featured', 'is_published', 'order')
        }),
        ('Duration, Dates & Verified Stats', {
            'fields': ('period', 'duration_stats', 'start_date', 'end_date', 'is_current')
        }),
        ('Details, Responsibilities & Skills', {
            'fields': ('description', 'responsibilities', 'skills')
        }),
    )


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'status', 'featured', 'is_published', 'order', 'cover_preview')
    list_filter = ('category', 'status', 'featured', 'is_published')
    search_fields = ('title', 'short_description', 'technologies', 'overview')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ProjectScreenshotInline]
    list_editable = ('featured', 'is_published', 'order')
    ordering = ('order', 'id')
    readonly_fields = ('cover_preview_large', 'created_at', 'updated_at')
    fieldsets = (
        ('Basic Information & Publishing', {
            'fields': ('title', 'slug', 'subtitle', 'category', 'status', 'featured', 'is_published', 'order')
        }),
        ('Descriptions & Overview', {
            'fields': ('short_description', 'overview', 'problem_statement', 'objective')
        }),
        ('Technical Details', {
            'fields': ('technologies', 'features_or_concepts', 'my_contribution')
        }),
        ('Links & Visual Media', {
            'fields': ('github_url', 'live_url', 'image', 'cover_preview_large'),
            'description': 'Leave github_url or live_url blank if not publicly available. The frontend handles missing links gracefully without inventing URLs.'
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def cover_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height: 32px; border-radius: 4px;" />', obj.image.url)
        return 'No cover'
    cover_preview.short_description = 'Cover'

    def cover_preview_large(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height: 180px; border-radius: 6px;" />', obj.image.url)
        return 'No cover image uploaded'
    cover_preview_large.short_description = 'Cover Preview'


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'proficiency', 'is_currently_learning', 'is_future_interest', 'is_visible', 'order')
    list_filter = ('category', 'is_currently_learning', 'is_future_interest', 'is_visible')
    search_fields = ('name', 'proficiency', 'description')
    list_editable = ('proficiency', 'is_currently_learning', 'is_visible', 'order')
    ordering = ('order', 'id')
    fieldsets = (
        ('Skill Details', {
            'fields': ('name', 'category', 'proficiency', 'description', 'is_visible', 'order')
        }),
        ('Visuals & Icons', {
            'fields': ('icon', 'custom_logo'),
            'description': 'Provide a Bootstrap icon class (e.g. bi-filetype-py) or custom SVG path (e.g. core/images/icons/google-antigravity.svg)'
        }),
        ('Learning Journey Association', {
            'fields': ('is_currently_learning', 'is_future_interest')
        }),
    )


@admin.register(LearningGoal)
class LearningGoalAdmin(admin.ModelAdmin):
    list_display = ('title', 'stage', 'badge_label', 'order')
    list_filter = ('stage',)
    search_fields = ('title', 'description', 'badge_label')
    list_editable = ('stage', 'order')
    ordering = ('order', 'id')


class CertificateInline(admin.TabularInline):
    model = Certificate
    extra = 0
    fields = ('title', 'issuing_organization', 'issue_date_display', 'category', 'certificate_file', 'is_temporary_placeholder', 'is_published', 'order')


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ('title', 'role', 'organization', 'category', 'period', 'is_published', 'order', 'featured')
    list_filter = ('category', 'organization', 'is_published', 'featured')
    search_fields = ('title', 'role', 'organization', 'description', 'key_highlights')
    list_editable = ('is_published', 'order', 'featured')
    inlines = [CertificateInline]
    ordering = ('order', 'id')
    fieldsets = (
        ('Achievement Overview', {
            'fields': ('title', 'role', 'organization', 'category', 'period', 'metrics_summary', 'icon', 'event_photo', 'is_published', 'order', 'featured')
        }),
        ('Detailed Description & Highlights', {
            'fields': ('description', 'key_highlights'),
            'description': 'Enter bullet points separated by newlines.'
        }),
    )


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('title', 'issuing_organization', 'category', 'get_date_display', 'file_type_badge', 'file_status', 'is_published', 'order', 'is_featured')
    list_filter = ('category', 'issuing_organization', 'is_published', 'is_featured', 'is_temporary_placeholder')
    search_fields = ('title', 'issuing_organization', 'description', 'credential_id')
    list_editable = ('is_published', 'order', 'is_featured')
    ordering = ('order', 'id')
    readonly_fields = ('file_preview_display',)
    fieldsets = (
        ('Certificate Metadata', {
            'fields': ('title', 'issuing_organization', 'category', 'achievement', 'is_published', 'order', 'is_featured')
        }),
        ('Dates & External Verification', {
            'fields': ('issue_date', 'issue_date_display', 'credential_id', 'credential_url')
        }),
        ('Certificate Document File & Preview', {
            'fields': ('certificate_file', 'is_temporary_placeholder', 'file_preview_display'),
            'description': 'Upload an image (JPG, PNG, WebP) or PDF file. Images can be viewed in the portfolio lightbox, and PDFs can be viewed or downloaded.'
        }),
        ('Context & Description', {
            'fields': ('description',)
        }),
    )

    def file_type_badge(self, obj):
        if obj.is_pdf:
            return 'PDF'
        elif obj.is_image:
            return obj.file_extension
        return 'No File'
    file_type_badge.short_description = 'Format'

    def file_status(self, obj):
        if obj.has_file:
            if obj.is_temporary_placeholder:
                return 'Temporary Placeholder'
            return 'Uploaded Document'
        return 'No File Attached'
    file_status.short_description = 'Status'

    def file_preview_display(self, obj):
        if not obj.has_file:
            return 'No file uploaded yet. Upload a certificate image or PDF above.'
        if obj.is_image:
            return format_html(
                '<div style="margin-top: 5px;"><img src="{}" style="max-height: 180px; border-radius: 6px; border: 1px solid #cbd5e1; box-shadow: 0 2px 4px rgba(0,0,0,0.05);" /><br><small style="color: #64748b;">Current image preview</small></div>',
                obj.certificate_file.url
            )
        elif obj.is_pdf:
            return format_html(
                '<div style="margin-top: 5px;"><a href="{}" target="_blank" rel="noopener noreferrer" class="button" style="padding: 6px 12px; background: #1d4ed8; color: #fff; text-decoration: none; border-radius: 4px; display: inline-block;">View PDF Document &rarr;</a><br><small style="color: #64748b;">Opens PDF in new tab</small></div>',
                obj.certificate_file.url
            )
        return format_html('<a href="{}" target="_blank">Download File</a>', obj.certificate_file.url)
    file_preview_display.short_description = 'Current Document Preview'


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at', 'is_read', 'replied')
    list_filter = ('is_read', 'replied', 'created_at')
    search_fields = ('name', 'email', 'subject', 'message', 'notes')
    list_editable = ('is_read', 'replied')
    ordering = ('-created_at',)
    readonly_fields = ('name', 'email', 'subject', 'message', 'created_at')
    actions = ['mark_as_read', 'mark_as_unread']
    fieldsets = (
        ('Sender Information', {
            'fields': ('name', 'email', 'created_at')
        }),
        ('Message Content', {
            'fields': ('subject', 'message')
        }),
        ('Admin Status & Follow-Up Notes', {
            'fields': ('is_read', 'replied', 'notes'),
            'description': 'Keep track of correspondence and internship inquiries.'
        }),
    )

    @admin.action(description="Mark selected messages as read")
    def mark_as_read(self, request, queryset):
        count = queryset.update(is_read=True)
        self.message_user(request, f"{count} message(s) marked as read.")

    @admin.action(description="Mark selected messages as unread")
    def mark_as_unread(self, request, queryset):
        count = queryset.update(is_read=False)
        self.message_user(request, f"{count} message(s) marked as unread.")


@admin.register(CurriculumVitae)
class CurriculumVitaeAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'file_size_display', 'uploaded_at', 'download_action')
    list_filter = ('is_active', 'uploaded_at')
    search_fields = ('title', 'notes')
    list_editable = ('is_active',)
    ordering = ('-is_active', '-uploaded_at')
    readonly_fields = ('uploaded_at', 'file_preview')
    actions = ['set_as_active']
    fieldsets = (
        ('CV Metadata & Active Status', {
            'fields': ('title', 'is_active', 'notes'),
            'description': 'Only one CV can be active at a time. Activating this version automatically deactivates all other uploaded CVs.'
        }),
        ('PDF Document Upload & Preview', {
            'fields': ('pdf_file', 'file_preview', 'uploaded_at'),
            'description': 'Upload a valid PDF document (maximum 10MB). The active CV will be served dynamically via website download buttons.'
        }),
    )

    def download_action(self, obj):
        if obj.pdf_file:
            return format_html(
                '<a href="{}" target="_blank" class="button" style="padding: 4px 8px; font-size: 0.8rem; background: #1d4ed8; color: #fff; text-decoration: none; border-radius: 4px;">View PDF</a>',
                obj.pdf_file.url
            )
        return 'No file'
    download_action.short_description = 'Document'

    def file_preview(self, obj):
        if obj.pdf_file:
            return format_html(
                '<div style="margin-top: 5px;"><a href="{}" target="_blank" rel="noopener noreferrer" style="font-weight: 600; color: #1d4ed8;">Open {} in new tab &rarr;</a> (Size: {})</div>',
                obj.pdf_file.url,
                obj.pdf_file.name,
                obj.file_size_display
            )
        return 'No PDF file currently uploaded.'
    file_preview.short_description = 'Current PDF File'

    @admin.action(description="Activate selected CV (deactivates others)")
    def set_as_active(self, request, queryset):
        if queryset.count() > 1:
            self.message_user(request, "Please select only one CV to activate at a time.", level='error')
            return
        selected = queryset.first()
        if selected:
            selected.is_active = True
            selected.save()
            self.message_user(request, f"'{selected.title}' is now the single active CV served on the portfolio.")

