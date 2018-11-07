import os

from django.views.generic import View
from django.conf import settings
from django.shortcuts import render

manga_directory = 'reader/manga/'
manga_path = os.path.join(settings.STATIC_ROOT, manga_directory)


def get_directory_as_nested_dict(path: str):
    nest = {}
    for element in os.listdir(path):
        absolute_path = os.path.join(path, element)
        static_relative_path = absolute_path[len(settings.STATIC_ROOT):]
        if not os.path.isdir(absolute_path):
            nest[static_relative_path] = None
        else:
            nest[static_relative_path] = get_directory_as_nested_dict(absolute_path)
    return nest


class MainView(View):
    template_name = "reader/index.html"

    def get(self, request, *args, **kwargs):
        return render(request, template_name=self.template_name, context={"dirs": get_directory_as_nested_dict(manga_path)})
