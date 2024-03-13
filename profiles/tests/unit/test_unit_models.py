import pytest
from django.contrib.auth.models import User
from profiles.models import Profile


@pytest.mark.django_db
class TestProfileModel:
    """
    A class to test the Profile model in the profiles application.

    This class contains methods to test the creation, string representation, and field attributes
    of the Profile model instances.

    Methods:
        test_profile_creation: Tests the creation of a Profile instance.
        test_string_representation: Tests the string representation of a Profile instance.
        test_favorite_city_field: Tests the favorite_city field of a Profile instance.
    """

    @pytest.fixture
    def test_user(self, db):
        """
        Creates a user instance for use in tests.
        """
        return User.objects.create_user(username='testuser', password='12345')

    def test_profile_creation(self, test_user):
        """
        Tests the creation of a Profile instance linked to a User instance.
        """
        profile = Profile.objects.create(user=test_user, favorite_city='TestCity')
        assert isinstance(profile, Profile)
        assert profile.user == test_user

    def test_string_representation(self, test_user):
        """
        Tests the string representation of a Profile instance.
        """
        profile = Profile.objects.create(user=test_user, favorite_city='TestCity')
        assert str(profile) == 'testuser'

    def test_favorite_city_field(self, test_user):
        """
        Tests the favorite_city field of a Profile instance.
        """
        profile = Profile.objects.create(user=test_user, favorite_city='TestCity')
        assert profile.favorite_city == 'TestCity'
