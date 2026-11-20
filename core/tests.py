from django.test import TestCase
from django.urls import reverse


class HomepageViewTests(TestCase):
    def test_homepage_status_code_and_template(self):
        """Verify that the homepage loads with status 200 and uses the correct templates."""
        response = self.client.get(reverse('core:home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/home.html')
        self.assertTemplateUsed(response, 'core/base.html')

    def test_homepage_contains_context_data(self):
        """Verify that context variables and static files are rendered properly."""
        response = self.client.get(reverse('core:home'))
        self.assertContains(response, 'IT Student &amp; Developer')
        self.assertContains(response, 'Portfolio project successfully initialized with Django!')
        self.assertContains(response, 'Python Development')
        self.assertContains(response, 'static/core/css/style.css')
        self.assertContains(response, 'static/core/js/main.js')
