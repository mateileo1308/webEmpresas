from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from .models import Page
from django.shortcuts import render, get_object_or_404, get_list_or_404

# Create your views here.
class pagesListView(ListView):
    model = Page

class pageDetailView(DetailView):
    model = Page

class pageCreateView(CreateView):
    model = Page
    fields = ["title", "content", "order"]

"""
    title = models.CharField(verbose_name="Título", max_length=200)
    content = RichTextField(verbose_name="Contenido")
    order = models.SmallIntegerField(verbose_name="Orden", default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
    pages = get_list_or_404(Page)
    return render(request, 'pages/pages.html', {'pages':pages})

def page(request, page_id, page_slug):
    page = get_object_or_404(Page, id=page_id)
    return render(request, 'pages/page.html', {'page':page})

"""