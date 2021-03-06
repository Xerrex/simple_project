from django.test import TestCase
from django.urls import reverse, resolve

from ..views import signup
from ..forms import SignUpForm


class SignUpTests(TestCase):
    """Tests for the sign up view/url.
    """

    def setUp(self):
        url = reverse('signup')
        self.response = self.client.get(url)

    def test_signup_status_code(self):
        """Test signup view status code.
        """
        self.assertEquals(self.response.status_code, 200)

    def test_signup_url_resolves_signup_view(self):
        """Test signup url resolves to the signup view.
        """
        view = resolve('/signup/')
        self.assertEquals(view.func, signup)

    def test_csrf(self):
        """Test that the signup view contains CSRF token.
        """
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_contains_form(self):
        """Test that signup view contains form
        """
        form = self.response.context.get('form')
        self.assertIsInstance(form, SignUpForm)

    def test_form_inputs(self):
        """Test form contains inputs.

        The view must contain five inputs: csrf, username, email,
        password1, password2.
        """

        self.assertContains(self.response, '<input', 5)
        self.assertContains(self.response, 'type="text"', 1)
        self.assertContains(self.response, 'type="email"', 1)
        self.assertContains(self.response, 'type="password"', 2)