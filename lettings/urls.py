from django.urls import path
from . import views

app_name = "lettings"

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:letting_id>/", views.letting, name="letting"),
]

handler500 = 'handlers.views.custom_500_view'
handler404 = 'handlers.views.custom_404_view'
