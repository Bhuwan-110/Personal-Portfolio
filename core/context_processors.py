from .models import CurriculumVitae, Profile


def global_portfolio_context(request):
    """
    Injects global portfolio context variables into all rendered templates:
    - profile: The active Profile model instance (Bhuwan Raj Pandey)
    - active_cv: The currently active CurriculumVitae instance (or None if no CV is active)
    - contact_info: Dynamic contact coordinates and social links from the active Profile
    """
    try:
        active_profile = Profile.get_active_profile()
    except Exception:
        active_profile = None

    try:
        active_cv = CurriculumVitae.get_active_cv()
    except Exception:
        active_cv = None

    if active_profile:
        contact_info = {
            'name': active_profile.full_name,
            'email': active_profile.email,
            'location': active_profile.location,
            'phone': active_profile.phone,
            'institution': active_profile.institution,
            'degree': active_profile.degree,
            'linkedin': active_profile.linkedin_url,
            'github': active_profile.github_url,
            'availability': active_profile.availability_status,
        }
    else:
        contact_info = {
            'name': 'Bhuwan Raj Pandey',
            'email': 'officialbhuwan454@gmail.com',
            'location': 'Kathmandu, Nepal',
            'phone': '',
            'institution': 'Himalayan WhiteHouse International College',
            'degree': 'Bachelor of Information Technology (BIT)',
            'linkedin': 'https://www.linkedin.com/in/bhuwan-pandey-2b829a2ba/',
            'github': 'https://github.com/Bhuwan-110',
            'availability': 'Open to IT internship opportunities and collaboration.',
        }

    return {
        'profile': active_profile,
        'active_cv': active_cv,
        'contact_info': contact_info,
    }

