from django.test import TestCase, Client
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

#from task_manager.helpers import test_english, remove_rollbar
from users.models import AppUser


class SignUpPageTests(TestCase):
    def setUp(self) -> None:
        self.first_name = 'Test_first_name'
        self.second_name = 'Test_second_name'
        self.username = 'testuser'
        self.password = 'password'

    def test_signup_page_url(self):
        response = self.client.get("/users/signup/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='users/registration.html')

    def test_signup_page_view_name(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='users/registration.html')

    def test_signup_form(self):
        response = self.client.post(reverse('signup'), data={
            'first_name': self.first_name,
            'second_name': self.second_name,
            'username': self.username,
            'password1': self.password,
            'password2': self.password
        })
        self.assertEqual(response.status_code, 302)

    


