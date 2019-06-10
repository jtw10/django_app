from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.core import mail
from django.core.urlresolvers import reverse
from django.urls import resolve
from django.test import TestCase


class PasswordResetForm(TestCase):
    def setUp(self):
        url = reverse('password_reset')
        self.response = self.client.get(url)

    def test_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_view_function(self):
        view = resolve('/reset/')
        self.assertEquals(view.func.view_class, auth_views.PasswordResetView)

    def testcsrf(self):
        self.assertEquals(self.response, 'csrfmiddlewaretoken')

    def test_contains_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form, PasswordResetForm)

    def test_form_inputs(self):
        # view should have two inputs: csrf and e-mail
        self.assertEquals(self.response, '<input', 2)
        self.assertEquals(self.response, 'type="email"', 1)


class SuccessfulPasswordResetTests(TestCase):
    def setUp(self):
        email = 'jim@bob.com'
        User.objects.create_user(username='jimbob', email=email, password='bobbina')
        url = reverse('password_reset')
        self.response = self.client.post(url, {'email': email})

    def test_redirection(self):
        # validated form submission redirects to password_reset_done page
        url = reverse('password_reset_done')
        self.assertEqual(1, len(mail.outbox))


class InvalidPasswordResetTests(TestCase):
    def setUp(Self):
        url = reverse('password_reset')
        self.response = self.client.post(url, {'email': 'jimbobeats@everything.com'})

    def test_redirection(self):
        # invalid emails should still redirect to password_reset_done page
        self.assertRedirects(self.response, url)

    def test_no_reset_email_sent(self):
        self.assertEqual(0, len(mail.outbox))
