from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from ..models import Board, Topic, Post
from ..views import reply_topic
from ..forms import PostForm


class ReplyTopicTestCase(TestCase):
    def setUp(self):
        self.board = Board.objects.create(name='Jimbob', description='Jimbob Discussion.')
        self.username = 'jimbob'
        self.password = 'jb'
        user = User.objects.create_user(username=self.username, email='jim@bob.com', password=self.password)
        self.topic = Topic.objects.create_user(subject='Unit Test', board=self.board, starter=user)
        Post.objects.create(message='Hi Jimothy', topic=self.topic, created_by=user)
        self.url = reverse('reply_topic', kwargs={'pk': self.board.pk, 'topic_pk': self.topic.pk})
