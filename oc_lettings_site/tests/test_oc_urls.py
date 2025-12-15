from django.test import SimpleTestCase
from django.urls import reverse, resolve
from oc_lettings_site import views as site_views
from lettings import views as lettings_views
from profiles import views as profiles_views

class UrlsTests(SimpleTestCase):
    """
    Tests des résolutions d'URL pour le site OC Lettings.
    """
    def test_index_resolves_to_index_view(self):
        # récupère index view
        url = reverse("index")
        # vérifie que l'URL résout à la vue correcte
        self.assertEqual(resolve(url).func, site_views.index)

    def test_lettings_index_resolves_to_lettings_index_view(self):
        # récupère lettings index view
        url = reverse("lettings:index")
        # vérifie que l'URL résout à la vue correcte
        self.assertEqual(resolve(url).func, lettings_views.index)

    def test_profiles_index_resolves_to_profiles_index_view(self):
        # récupère profiles index view
        url = reverse("profiles:index")
        # vérifie que l'URL résout à la vue correcte
        self.assertEqual(resolve(url).func, profiles_views.index)