from django.shortcuts import render


def home(request):
    """
    Renders the portfolio homepage.
    Passes initial profile and skills context to verify template rendering.
    """
    context = {
        'page_title': 'Home | Professional IT Portfolio',
        'student_name': 'IT Student & Developer',
        'tagline': 'Aspiring Python Developer | Backend Engineer | AI Enthusiast',
        'focus_areas': [
            'Python Development',
            'Django Backend Architecture',
            'Web Technologies (HTML5, CSS3, JavaScript, Bootstrap 5)',
            'Artificial Intelligence & Machine Learning',
        ],
        'status_message': 'Portfolio project successfully initialized with Django!',
    }
    return render(request, 'core/home.html', context)
