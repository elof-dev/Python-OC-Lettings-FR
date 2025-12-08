from django.shortcuts import get_object_or_404, render
from .models import Letting

def index(request):
    lettings_list = Letting.objects.all()
    return render(request, "lettings/index.html", {"lettings_list": lettings_list})

def letting(request, letting_id):
    letting = get_object_or_404(Letting, id=letting_id)
    return render(
        request,
        "lettings/letting.html",
        {"title": letting.title, "address": letting.address},
    )