import pytest


@pytest.mark.django_db
def test__group__return_valid_str(group_object):
    assert str(group_object) == group_object.title


@pytest.mark.django_db
def test__tag__return_valid_str(tag_object):
    assert str(tag_object) == tag_object.name


@pytest.mark.django_db
def test__post__return_valid_str(post_object):
    assert str(post_object) == (post_object.text[:15] + '...' if len(post_object.text) > 15 else post_object.text)


@pytest.mark.django_db
def test__comment__return_valid_str(comment_object):
    assert str(comment_object) == comment_object.text[:15]


