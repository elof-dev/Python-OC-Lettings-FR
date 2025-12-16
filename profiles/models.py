from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """Modèle représentant le profil utilisateur
    Fait appel à un utilisateur via une clé étrangère
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return self.user.username

    class Meta:
        """
        Métadonnées pour le modèle Profile
        db_table: nom de la table dans la base de données
        """

        db_table = "oc_lettings_site_profile"
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"
