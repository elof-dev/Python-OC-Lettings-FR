from django.test import TestCase
from django.urls import reverse
from lettings.models import Letting, Address


class LettingsViewsTest(TestCase):
    def make_address(self, **kwargs):
        data = {
            "number": kwargs.get("number", 1),
            "street": kwargs.get("street", "Rue de Test"),
            "city": kwargs.get("city", "Paris"),
            "state": kwargs.get("state", "FR"),
            "zip_code": kwargs.get("zip_code", 75001),
            "country_iso_code": kwargs.get("country_iso_code", "FRA"),
        }
        return Address.objects.create(**data)

    def test_index_status_code_and_template(self):
        resp = self.client.get(reverse("lettings:index"))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, "lettings/index.html")

    def test_index_contains_lettings_list(self):
        addr = self.make_address()
        letting = Letting.objects.create(title="Maison Test", address=addr)
        resp = self.client.get(reverse("lettings:index"))
        self.assertIn("lettings_list", resp.context)
        self.assertEqual(list(resp.context["lettings_list"]), [letting])

    def test_letting_detail_status_and_context(self):
        addr = self.make_address(number=2, street="Rue Exemple", city="Lyon", zip_code=69001)
        letting = Letting.objects.create(title="Bel Appartement", address=addr)
        url = reverse("lettings:letting", kwargs={"letting_id": letting.id})
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, "lettings/letting.html")
        self.assertEqual(resp.context.get("title"), letting.title)
        self.assertEqual(resp.context.get("address"), letting.address)