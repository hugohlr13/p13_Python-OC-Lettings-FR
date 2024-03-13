import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from profiles.models import Profile


@pytest.mark.django_db
class TestProfilesViews:
    """
    A class to test the views associated with the profiles application.

    This class contains methods to test the rendering and context data of the index and profile
    detail views provided by the profiles application.

    Methods:
        test_index_view: Tests the index view which lists all profiles.
        test_profile_view: Tests the profile detail view for a specific user's profile.
    """

    @pytest.fixture
    def test_user(self, db):
        """
        Creates a user instance for use in tests.
        """
        return User.objects.create_user(username='testuser', password='12345')

    @pytest.fixture
    def test_profile(self, db, test_user):
        """
        Creates a profile instance for use in tests.
        """
        return Profile.objects.create(user=test_user, favorite_city='TestCity')

    def test_index_view(self, client):
        """
        Tests the index view to ensure it returns a 200 status code and the correct template.
        """
        response = client.get(reverse('profiles:index'))
        assert response.status_code == 200
        assert 'profiles/index.html' in [t.name for t in response.templates]
        assert 'profiles_list' in response.context

    def test_profile_view(self, client, test_profile):
        """
        Tests the profile detail view to ensure it returns a 200 status code,
        uses the correct template, and the context contains the correct profile instance.
        """
        url = reverse('profiles:profile', kwargs={'username': test_profile.user.username})
        response = client.get(url)
        assert response.status_code == 200
        assert 'profiles/profile.html' in [t.name for t in response.templates]
        assert 'profile' in response.context
        assert response.context['profile'] == test_profile
