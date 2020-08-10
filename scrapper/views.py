from django.shortcuts import render

from .scrap_util import scrap_manjaro_stable_updates, scrap_realpython, scrap_stackoverflow_python


def index(request):
    contents_real_python = scrap_realpython()
    contents_manjaro_stable = scrap_manjaro_stable_updates()
    contents_stackoverflow = scrap_stackoverflow_python()
    context = {
        "contents_real_python": contents_real_python,
        "contents_manjaro_updates": contents_manjaro_stable,
        "contents_stackoverflow":contents_stackoverflow,
    }
    return render(request, "index.html", context)

