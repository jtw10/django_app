from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.test import TestCase
from django.urls import reverse
from ..models import Board, Topic, Post
from ..views import PostUpdateView


class PostUpdateViewTestCase(TestCase):
    def setUp(self):
        self.board = Board.objects.create(name='Jim', description='Bob')
        self.username = 'Jimothy'
        self.password = 'Bobbert'
        user = User.objects.create_user(username=self.username, email='jb@hehe.XD', password=self.password)
        self.topic = Topic.objects.create(subject='Bim Job', board=self.board, starter=user)
        self.post = Post.objects.create(message='Jimmy Where Are You!', topic=self.topic, created_by=user)
        self.url = reverse('edit_post', kwargs={
            'pk': self.board.pk,
            'topic_pk': self.topic.pk,
            'post_pk': self.post.pk
        })


class LoginRequiredPostUpdateViewTests(PostUpdateViewTestCase):
    def test_redirection(self):
        login_url = reverse('login')
        response = self.client.get(self.url)
        self.assertRedirects(response, '{login_url}?next={url}'.format(login_url=login_url, url=self.url))


class UnauthorizedPostUpdateViewTests(PostUpdateViewTestCase):
    def setUp(self):
        super(UnauthorizedPostUpdateViewTests, self).setUp()
        username = 'jombib'
        password = 'jb'
        user = User.objects.create_user(username=username, email='jb@jb.jb', password=password)
        self.client.login(username=username, password=password)
        self.response = self.client.get(self.url)

    def test_status_code(self):
        # topics should only be editted by the owner
        self.assertEquals(self.response.status_code, 404)
