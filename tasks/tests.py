from django.test import TestCase
from django.urls import reverse

from users.models import AppUser
from statuses.models import Status
from labels.models import Label
from .models import Task

class TestCreateUpdateDeleteTask(TestCase):
    def setUp(self):
        self.data1 = {
        'first_name': 'First_name1',
        'last_name': 'Last_name1',
        'username': 'test_username1',
        'password': 'password1',
    }
        self.data2 = {
        'first_name': 'First_name2',
        'last_name': 'Last_name2',
        'username': 'test_username2',
        'password': 'password2',
    }
        self.user = AppUser.objects.create_user(**self.data1)
        AppUser.objects.create_user(**self.data2)
        Label.objects.create(name='Test_label1')
        Label.objects.create(name='Test_label2')
        Status.objects.create(name='Test_status1')
        Status.objects.create(name='Test_status2')
        self.client.force_login(self.user)
    
    def test_create_task(self):
        response = self.client.post(reverse('task_create'), data={
            'name': 'Test_task',
            'description': 'test_description',
            'status': Status.objects.get(name='Test_status1'),
            'executor': AppUser.objects.get(usernameusername='test_username1'),
            'labels': Label.objects.get(name='Test_label1'),
        })
        self.assertEqual(response.status_code, 302)
    
    
    def test_update_task_form(self):
        task_data={
            'name': 'Test_task',
            'description': 'test_description',
            'status': Status.objects.get(name='Test_status1'),
            'executor': AppUser.objects.get(username='test_username1'),
            'labels': Label.objects.get(name='Test_label1'),
        }
        Task.objects.create(**task_data)
        id = Task.objects.get(name='Test_task').pk
        response = self.client.post(reverse('task_update', args=[id]), data={
            'name': 'Updated_test_task',
            'description': 'test_description',
            'status': Status.objects.get(name='Test_status2'),
            'executor': AppUser.objects.get(username='test_username2'),
            'labels': Label.objects.get(name='Test_label2'),
            
        })
        self.assertEqual(response.status_code, 302)
    
    def test_delete_task_user(self):
        task_data={
            'name': 'Test_task',
            'description': 'test_description',
            'status': Status.objects.get(name='Test_status1'),
            'executor': AppUser.objects.get(username='test_username1'),
            'labels': Label.objects.get(name='Test_label1'),
        }
        Task.objects.create(**task_data)
        id = Status.objects.get(name='Test_task').pk
        response = self.client.post(reverse('task_delete', args=[id]))
        self.assertEqual(response.status_code, 302)
