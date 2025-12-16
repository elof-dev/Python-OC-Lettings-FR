from django.test import TestCase, override_settings
from django.urls import reverse


class FunctionalSiteTests(TestCase):
    def test_index_links_and_navigation(self):
        """Vérifie que l'index contient les liens vers profiles et lettings
        et que ces pages répondent 200."""
        resp = self.client.get(reverse("index"))
        self.assertEqual(resp.status_code, 200)
        # liens présents
        profiles_url = reverse("profiles:index")
        lettings_url = reverse("lettings:index")
        self.assertContains(resp, profiles_url)
        self.assertContains(resp, lettings_url)

        # navigation vers profiles index
        resp_profiles = self.client.get(profiles_url)
        self.assertEqual(resp_profiles.status_code, 200)

        # navigation vers lettings index
        resp_lettings = self.client.get(lettings_url)
        self.assertEqual(resp_lettings.status_code, 200)

    @override_settings(DEBUG=False, ALLOWED_HOSTS=["testserver"])
    def test_404_uses_custom_template(self):
        """En DEBUG=False, une URL inconnue doit renvoyer le template 404.html."""
        resp = self.client.get("/url-qui-n-existe-pas/")
        self.assertEqual(resp.status_code, 404)
        # vérifie que le template 404.html est utilisé
        self.assertTemplateUsed(resp, "404.html")
        # vérifie un contenu attendu du template 404
        self.assertContains(resp, "Page introuvable", status_code=404)
