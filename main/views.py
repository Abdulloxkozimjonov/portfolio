from django.shortcuts import render
from . import models


def index_view(request):
    banner = models.Banner.objects.last()
    context = {
        'banner': banner,
        'info': models.Info.objects.last(),
        'about': models.About.objects.all().order_by('-id')[:3],
        'people_say': models.People_say.objects.all().order_by('-id')[:4],
        'fac': models.Fac.objects.all().order_by('-id')[:4],
    }
    return render(request, 'index.html', context)


def contact_view(request):
    full_name = request.POST["full_name"]
    email = request.POST["email"]
    message = request.POST["message"]
    create = models.Contact.objects.create(
        full_name = full_name,
        email = email,
        message = message,
    )