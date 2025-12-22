from django.contrib import admin
from django.urls import include, path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("lettings/", include(("lettings.urls", "lettings"), namespace="lettings")),
    path("profiles/", include(("profiles.urls", "profiles"), namespace="profiles")),
    path("admin/", admin.site.urls),
]

# Gestionnaires d'erreurs personnalisés
handler500 = "handlers.views.custom_500_view"
handler404 = "handlers.views.custom_404_view"
