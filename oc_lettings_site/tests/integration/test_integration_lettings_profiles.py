import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from lettings.models import Address, Letting
from profiles.models import Profile


@pytest.mark.django_db
class TestCombinedIntegration:
    """
    Test class for combined integration between lettings and profiles.
    """

    @pytest.fixture
    def setup_data(self, db):
        """
        Creates instances for Address, Letting, User and Profile for use in the integration tests.
        """
        user = User.objects.create_user(username='testuser', password='12345')
        profile = Profile.objects.create(user=user, favorite_city='TestCity')
        address = Address.objects.create(
            number=123,
            street='Main Street',
            city='Anytown',
            state='NY',
            zip_code=12345,
            country_iso_code='USA'
        )
        letting = Letting.objects.create(title='Nice place', address=address)
        return user, profile, address, letting

    def test_combined_page_integration(self, client, setup_data):
        """
        Ensures that the combined functionality on a page,
        like showing user profile details on a letting detail page, works correctly.
        """
        user, profile, address, letting = setup_data
        letting_url = reverse('lettings:letting', kwargs={'letting_id': letting.id})
        profile_url = reverse('profiles:profile', kwargs={'username': user.username})

        response_letting = client.get(letting_url)
        response_profile = client.get(profile_url)

        # Checking if letting and profile data are correct and available on respective pages
        assert response_letting.status_code == 200
        assert 'Nice place' in response_letting.content.decode()
        assert 'Main Street' in response_letting.content.decode()

        assert response_profile.status_code == 200
        assert 'TestCity' in response_profile.content.decode()
        assert 'testuser' in response_profile.content.decode()
