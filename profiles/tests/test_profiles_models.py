from django.test import TestCase
from django.contrib.auth import get_user_model
from profiles.models import Profile

User = get_user_model()


class ProfileModelTest(TestCase):
    def test_profile_str_and_meta(self):
        user = User.objects.create_user(username="alice", password="pw")
        profile = Profile.objects.create(user=user, favorite_city="Paris")
        self.assertEqual(str(profile), "alice")
        self.assertEqual(profile._meta.db_table, "oc_lettings_site_profile")
