from django.shortcuts import render

from .scrap_util import scrap_manjaro_stable_updates, scrap_realpython


def index(request):
    contents_real_python = scrap_realpython()
    contents_manjaro_stable = scrap_manjaro_stable_updates()
    context = {
        "contents_real_python": contents_real_python,
        "contents_manjaro_updates": contents_manjaro_stable,
    }
    return render(request, "index.html", context)

