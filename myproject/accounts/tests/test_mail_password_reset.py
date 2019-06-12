from django.core import mail
from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase


class PasswordResetMailTests(TestCase):
    def setUp(self):
        User.objects.create_user(username='jimmiebobbie', email='jimbob@gmail.com', password='heheXD')
        self.response = self.client.post(reverse('password_reset'), {'email': 'jimothybobbert@gmail.com'})
        self.email = mail.outbox[0]

    def test_email_subject(self):
        self.assertEqual('[UwU] Your password needs be reset', self.email.subject)

    def test_email_body(self):
        context = self.response.context
        token = context.get('token')
        uid = context.get('uid')
        password_Reset_token_url = reverse('password_reset_confirm', kwargs={
            'uidb64': uid,
            'token': token
        })
        self.assertIn(password_Reset_token_url, self.email.body)
        self.assertIn('jimmiebobbie', self.email.body)
        self.assertIn('jimothybobbert@greathuman.com', self.email.body)

    def test_email_to(self):
        self.assertEqual(['jimothybobbert@greathuman.com'], self.email.to)
