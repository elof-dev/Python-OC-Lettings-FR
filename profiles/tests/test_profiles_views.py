from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from profiles.models import Profile

User = get_user_model()


class ProfileViewsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="bob", password="pw")
        self.profile = Profile.objects.create(user=self.user, favorite_city="Lyon")

    def test_index_status_and_context(self):
        resp = self.client.get(reverse("profiles:index"))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, "profiles/index.html")
        self.assertIn("profiles_list", resp.context)
        self.assertIn(self.profile, resp.context["profiles_list"])

    def test_profile_detail_and_template(self):
        url = reverse("profiles:profile", kwargs={"username": self.user.username})
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, "profiles/profile.html")
        self.assertEqual(resp.context.get("profile"), self.profile)

    def test_profile_detail_404_when_missing(self):
        url = reverse("profiles:profile", kwargs={"username": "doesnotexist"})
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 404)
