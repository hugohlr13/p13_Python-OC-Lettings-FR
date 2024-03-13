import pytest
from django.urls import reverse
from lettings.models import Address, Letting


@pytest.mark.django_db
class TestLettingsViews:
    """
    A class to test views associated with the Letting model.

    This class contains methods to test the index view and individual letting view.

    Methods:
        test_index_view: Tests the lettings index view for correct HTTP status and content.
        test_letting_view: Tests the individual letting view for correct HTTP status and content.
    """
    @pytest.fixture
    def test_address(self, db):
        """
        Creates an address instance for use in tests.
        """
        return Address.objects.create(
            number=123,
            street='Main Street',
            city='Anytown',
            state='Anystate',
            zip_code=12345,
            country_iso_code='USA'
        )

    @pytest.fixture
    def test_letting(self, db, test_address):
        """
        Creates a letting instance for use in tests, linked to the address instance.
        """
        return Letting.objects.create(title='Nice place', address=test_address)

    def test_index_view(self, client):
        """
        Tests the lettings index view for correct HTTP status and content.
        """
        response = client.get(reverse('lettings:index'))
        assert response.status_code == 200
        assert 'Nice place' not in response.content.decode()

    def test_letting_view(self, client, test_letting):
        """
        Tests the individual letting view for correct HTTP status and content.
        """
        url = reverse('lettings:letting', args=[test_letting.id])
        response = client.get(url)
        assert response.status_code == 200
        assert 'Nice place' in response.content.decode()
        assert 'Main Street' in response.content.decode()
