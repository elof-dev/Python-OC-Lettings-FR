from django.test import SimpleTestCase
from django.urls import reverse, resolve, NoReverseMatch, Resolver404
from profiles import views

class ProfileUrlsTest(SimpleTestCase):
    def test_index_resolves_to_index_view(self):
        url = reverse("profiles:index")
        self.assertEqual(resolve(url).func, views.index)

    def test_profile_resolves_to_profile_view(self):
        url = reverse("profiles:profile", kwargs={"username": "alice"})
        self.assertEqual(resolve(url).func, views.profile)

    def test_reverse_missing_username_raises(self):
        with self.assertRaises(NoReverseMatch):
            reverse("profiles:profile")

    def test_resolve_unknown_path_raises_resolver404(self):
        with self.assertRaises(Resolver404):
            resolve("/une-url-qui-n-existe-pas/")