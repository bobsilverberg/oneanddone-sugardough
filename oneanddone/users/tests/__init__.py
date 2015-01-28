from django.contrib.auth.models import User

from factory import DjangoModelFactory, Sequence, SubFactory

from oneanddone.users import models


class UserFactory(DjangoModelFactory):
    FACTORY_FOR = User

    username = Sequence(lambda n: 'test{0}'.format(n))
    email = Sequence(lambda n: 'test{0}@example.com'.format(n))


class UserProfileFactory(DjangoModelFactory):
    FACTORY_FOR = models.UserProfile

    user = SubFactory(UserFactory)
    name = Sequence(lambda n: 'test{0}'.format(n))
    username = Sequence(lambda n: 'testuser%d' % n)
