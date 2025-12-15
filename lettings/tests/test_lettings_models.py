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
        a = Address.objects.create(
            number=5, street="Rue Exemple", city="Lyon", state="FR", zip_code=69001, country_iso_code="FRA"
        )
        self.assertEqual(str(a), "5 Rue Exemple")

    def test_letting_str_and_relation(self):
        a = self.make_valid_address()
        a.full_clean()
        a.save()
        l = Letting.objects.create(title="Belle maison", address=a)
        self.assertEqual(str(l), "Belle maison")
        # relation OneToOne fonctionne
        self.assertEqual(l.address, a)

    def test_valid_address_full_clean_passes(self):
        a = self.make_valid_address()
        # ne doit pas lever
        a.full_clean()

    def test_state_min_length_validator_raises(self):
        a = self.make_valid_address()
        a.state = "F"  # trop court (minLength 2)
        with self.assertRaises(ValidationError):
            a.full_clean()

    def test_country_iso_code_min_length_validator_raises(self):
        a = self.make_valid_address()
        a.country_iso_code = "FR"  # trop court (minLength 3)
        with self.assertRaises(ValidationError):
            a.full_clean()

    def test_number_max_value_validator_raises(self):
        a = self.make_valid_address()
        a.number = 10000  # supérieur au MaxValueValidator(9999)
        with self.assertRaises(ValidationError):
            a.full_clean()

    def test_zip_code_max_value_validator_raises(self):
        a = self.make_valid_address()
        a.zip_code = 100000  # supérieur au MaxValueValidator(99999)
        with self.assertRaises(ValidationError):
            a.full_clean()