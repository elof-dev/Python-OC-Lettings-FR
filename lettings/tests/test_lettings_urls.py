from django.test import SimpleTestCase
from django.urls import reverse, resolve, NoReverseMatch
from lettings import views


class LettingsUrlsTests(SimpleTestCase):
    def test_lettings_index_resolves_to_index_view(self):
        url = reverse("lettings:index")
        self.assertEqual(resolve(url).func, views.index)

    def test_letting_detail_resolves_to_letting_view(self):
        url = reverse("lettings:letting", kwargs={"letting_id": 1})
        self.assertEqual(resolve(url).func, views.letting)

    def test_letting_reverse_requires_letting_id(self):
        with self.assertRaises(NoReverseMatch):
            reverse("lettings:letting")  # doit lever car kwargs manquant