import pytest
from lettings.models import Address, Letting


@pytest.mark.django_db
class TestAddressModel:
    """
    A class to test the Address model.

    Methods:
        test_string_representation: Tests that the string representation of an address is correct.
        test_address_fields: Tests that the fields of an address can be validated without errors.
    """

    def test_string_representation(self):
        """
        Tests that the string representation of an address is correct.
        """
        address = Address(
            number=123,
            street='Main Street',
            city='Anytown',
            state='Anystate',
            zip_code=12345,
            country_iso_code='USA'
        )
        assert str(address) == '123 Main Street'

    def test_address_fields(self):
        """
        Tests that the fields of an address can be validated without errors.
        """
        address = Address(
            number=123,
            street='Main Street',
            city='Anytown',
            state='NY',
            zip_code=12345,
            country_iso_code='USA'
        )
        address.full_clean()


class TestLettingModel:
    """
    A class to test the Letting model.

    Methods:
        test_string_representation: Tests that the string representation of a letting is correct.
    """
    @pytest.fixture
    def test_address(self, db):
        """
        Creates an address for testing.
        """
        return Address.objects.create(
            number=123,
            street='Main Street',
            city='Anytown',
            state='Anystate',
            zip_code=12345,
            country_iso_code='USA'
        )

    def test_string_representation(self, test_address):
        """
        Tests that the string representation of a letting is correct.
        """
        letting = Letting(title='Nice place', address=test_address)
        assert str(letting) == 'Nice place'
