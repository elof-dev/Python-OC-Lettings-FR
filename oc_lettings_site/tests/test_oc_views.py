from django.test import TestCase
from django.urls import reverse

class IndexViewTest(TestCase):
    def test_index_status_code_and_template(self):
        """
        Teste que la page d'accueil renvoie un code 200 et utilise le template correct.
        """
        # récupère la réponse de la vue index
        resp = self.client.get(reverse("index"))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, "index.html")

    def test_index_contains_expected_content_and_links(self):
        """
        Teste que la page d'accueil contient le contenu attendu et les liens vers les applications.
        """
        resp = self.client.get(reverse("index"))
        # contenu principal attendu
        self.assertContains(resp, "Welcome to Holiday Homes")
        # liens vers les apps
        self.assertContains(resp, reverse("profiles:index"))
        self.assertContains(resp, reverse("lettings:index"))