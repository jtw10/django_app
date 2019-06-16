from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse, resolve
from ..models import Board, Topic, Post
from ..views import reply_topic
from ..forms import PostForm


class ReplyTopicTestCase(TestCase):
    def setUp(self):
        self.board = Board.objects.create(name='Jimbob', description='Jimbob Discussion.')
        self.username = 'jimbob'
        self.password = 'jb'
        user = User.objects.create_user(username=self.username, email='jim@bob.com', password=self.password)
        self.topic = Topic.objects.create(subject='Unit Test', board=self.board, starter=user)
        Post.objects.create(message='Hi Jimothy', topic=self.topic, created_by=user)
        self.url = reverse('reply_topic', kwargs={'pk': self.board.pk, 'topic_pk': self.topic.pk})


class LoginRequiredReplyTopicTests(ReplyTopicTestCase):
    def test_redirection(self):
        login_url = reverse('login')
        response = self.client.get(self.url)
        self.assertRedirects(response, '{login_url}?next={url}'.format(login_url=login_url, url=self.url))


class ReplyTopicTests(ReplyTopicTestCase):
    def setUp(self):
        super(ReplyTopicTests, self).setUp()
        self.client.login(username=self.username, password=self.password)
        self.response = self.client.get(self.url)

    def test_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_view_function(self):
        view = resolve('/boards/1/topics/1/reply/')
        self.assertEquals(view.func, reply_topic)

    def test_csrf(self):
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_contains_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form, PostForm)

    def test_form_inputs(self):
        # view should have 2 input areas for csrf and textarea
        self.assertContains(self.response, '<input', 1)
        self.assertContains(self.response, '<textarea', 1)


class SuccessfulReplyTopicTests(ReplyTopicTestCase):
    def setUp(self):
        super(SuccessfulReplyTopicTests, self).setUp()
        self.client.login(username=self.username, password=self.password)
        self.response = self.client.post(self.url, {'message': 'Jim Bob'})

    def test_redirection(self):
        topic_posts_url = reverse('topic_posts', kwargs={'pk': self.board.pk, 'topic_pk': self.topic.pk})
        self.assertRedirects(self.response, topic_posts_url)

    def test_reply_created(self):
        # 2 total posts. one in ReplyTopicTestCase and one in this class
        self.assertEquals(Post.objects.count(), 2)


class InvalidReplyTopicTests(ReplyTopicTestCase):
    def setUp(self):
        # empty dictionary submission to 'reply_topic' view
        super(InvalidReplyTopicTests, self).setUp()
        self.client.login(username=self.username, password=self.password)
        self.response = self.client.post(self.url, {})

    def test_status_code(self):
        # invalid submissions should return same page
        self.assertEquals(self.response.status_code, 200)

    def test_form_errors(self):
        form = self.response.context.get('form')
        self.assertTrue(form.errors)
