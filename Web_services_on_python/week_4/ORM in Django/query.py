from datetime import datetime

from django.db.models import Q, Count, Avg
from pytz import UTC

from db.models import User, Blog, Topic


def create():
    u1 = User.objects.create(first_name='u1', last_name='u1')
    u1.save()
    u2 = User.objects.create(first_name='u2', last_name='u2')
    u2.save()
    u3 = User.objects.create(first_name='u3', last_name='u3')
    u3.save()

    blog1 = Blog.objects.create(title='blog1', author=u1)
    blog1.save()
    blog2 = Blog.objects.create(title='blog2', author=u1)
    blog2.save()

    blog1.subscribers.add(u1, u2)
    blog2.subscribers.add(u2)

    topik1 = Topic.objects.create(title='topik1', blog=blog1, author=u1)
    topik1.save()
    topik2 = Topic.objects.create(title='topik2', blog=blog1, author=u3,
                                  created=datetime(year=2017, month=1, day=1, tzinfo=UTC))
    topik2.save()
    topik1.likes.add(u1, u2, u3)

def edit_all():
    User.objects.all().update(first_name='uu1')


def edit_u1_u2():
    User.objects.filter(Q(first_name='u1') | Q(first_name='u2')).update(first_name='uu1')


def delete_u1():
    User.objects.filter(first_name='u1').delete()


def unsubscribe_u2_from_blogs():
    Blog.subscribers.through.objects.filter(user__first_name='u2').delete()


def get_topic_created_grated():
    return Topic.objects.filter(created__gt=datetime(year=2018, month=1, day=1, tzinfo=UTC))


def get_topic_title_ended():
    return Topic.objects.filter(title__endswith='content')


def get_user_with_limit():
    return User.objects.all().order_by('id')[:-2]               # мб нужно сделать '-id'


def get_topic_count():
    return Blog.objects.annotate(topic_count=Count('topic').order_by('topic_count'))


def get_avg_topic_count():
    pass


def get_blog_that_have_more_than_one_topic():
    pass


def get_topic_by_u1():
    pass


def get_user_that_dont_have_blog():
    pass


def get_topic_that_like_all_users():
    pass


def get_topic_that_dont_have_like():
    pass
