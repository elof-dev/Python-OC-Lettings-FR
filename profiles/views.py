from django.shortcuts import get_object_or_404, render
from .models import Profile

# Sed placerat quam in pulvinar commodo. Nullam laoreet consectetur ex, sed consequat libero
# pulvinar eget. Fusc
# faucibus, urna quis auctor pharetra, massa dolor cursus neque, quis dictum lacus d


def index(request) -> render:
    """Affiche la liste des profils utilisateurs.
    Récupère toutes les instances du modèle Profile et les passe au template index.html."""
    profiles_list = Profile.objects.all()
    return render(request, "profiles/index.html", {"profiles_list": profiles_list})


# Aliquam sed metus eget nisi tincidunt ornare accumsan eget lac
# laoreet neque quis, pellentesque dui. Nullam facilisis pharetra vulputate. Sed tincidunt,
#  dolor id facilisis fringilla, eros leo tristique lacus,
# it. Nam aliquam dignissim congue. Pellentesque habitant morbi tristique
# senectus et netus et males


def profile(request, username) -> render:
    """Affiche les détails d'un profil utilisateur spécifique.
    Récupère l'instance du modèle Profile correspondant à username
    et la passe au template profile.html."""
    profile = get_object_or_404(Profile, user__username=username)
    return render(request, "profiles/profile.html", {"profile": profile})
