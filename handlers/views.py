from django.shortcuts import render


def custom_404_view(request, exception):
    """
    Gestionnaire de la page d'erreur 404 personnalisée
    La fonction prend la requête et l'exception en paramètres et
    rends le template 404.html avec le statut 404.
    """
    return render(request, "404.html", status=404)

def custom_500_view(request):
    """
    Gestionnaire de la page d'erreur 500 personnalisée
    La fonction prend la requête en paramètre et
    rends le template 500.html avec le statut 500.
    """
    return render(request, "500.html", status=500)
