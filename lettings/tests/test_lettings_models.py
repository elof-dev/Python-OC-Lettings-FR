from django.test import TestCase
from django.core.exceptions import ValidationError
from lettings.models import Address, Letting


class LettingsModelsTest(TestCase):
    def make_valid_address(self):
        return Address(
            number=12,
            street="Rue de Test",
            city="Paris",
            state="FR",
            zip_code=75001,
            country_iso_code="FRA",
        )

    def test_address_str(self):
        address = Address.objects.create(
            number=5,
            street="Rue Exemple",
            city="Lyon",
            state="FR",
            zip_code=69001,
            country_iso_code="FRA",
        )
        self.assertEqual(str(address), "5 Rue Exemple")

    def test_letting_str_and_relation(self):
        address = self.make_valid_address()
        address.full_clean()
        address.save()
        letting = Letting.objects.create(title="Belle maison", address=address)
        self.assertEqual(str(letting), "Belle maison")
        # relation OneToOne fonctionne
        self.assertEqual(letting.address, address)

    def test_valid_address_full_clean_passes(self):
        address = self.make_valid_address()
        # ne doit pas lever
        address.full_clean()

    def test_state_min_length_validator_raises(self):
        address = self.make_valid_address()
        address.state = "F"  # trop court (minLength 2)
        with self.assertRaises(ValidationError):
            address.full_clean()

    def test_country_iso_code_min_length_validator_raises(self):
        address = self.make_valid_address()
        address.country_iso_code = "FR"  # trop court (minLength 3)
        with self.assertRaises(ValidationError):
            address.full_clean()

    def test_number_max_value_validator_raises(self):
        address = self.make_valid_address()
        address.number = 10000  # supérieur au MaxValueValidator(9999)
        with self.assertRaises(ValidationError):
            address.full_clean()

    def test_zip_code_max_value_validator_raises(self):
        address = self.make_valid_address()
        address.zip_code = 100000  # supérieur au MaxValueValidator(99999)
        with self.assertRaises(ValidationError):
            address.full_clean()
