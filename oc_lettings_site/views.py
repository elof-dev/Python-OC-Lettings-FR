from django.shortcuts import render

def index(request):
    """Affiche la page d'accueil du site OC Lettings."""
    return render(request, "index.html")