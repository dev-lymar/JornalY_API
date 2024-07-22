import pytest
from django.contrib.auth import get_user_model

from posts.models import Comment, Follow, Group, Post, Tag

User = get_user_model()


@pytest.fixture
def user():
    return User.objects.create(username='testuser', password='testpass')


@pytest.fixture
def another_user():
    return User.objects.create(username='anotheruser', password='testpass')


@pytest.fixture
def group_object():
    return Group.objects.create(
        title='Test Group',
        slug='test-group',
        description='This is a test group'
    )


@pytest.fixture
def tag_object():
    return Tag.objects.create(name='Test Tag')


@pytest.fixture
def post_object(user, group_object):
    return Post.objects.create(
        text='This is a test post',
        author=user,
        group=group_object
    )


@pytest.fixture
def comment_object(user, post_object):
    return Comment.objects.create(
        post=post_object,
        author=user,
        text='This is a test comment'
    )


@pytest.fixture
def follow_object(user, another_user):
    return Follow.objects.create(user=user, author=another_user)