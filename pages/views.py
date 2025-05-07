from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Page
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect, render, get_object_or_404, get_list_or_404
from .forms import PageForm


class StaffRequiredMixin(object):
    """
    Este Mixin requiere que el usuario sea parte del staff
    """
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return redirect(reverse_lazy('admin:login'))
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)

# Create your views here.
class pagesListView(ListView):
    model = Page
    #user_ = request.user
    #print(f"en la vista principal {user_}")

class pageDetailView(DetailView):
    model = Page

class pageCreateView(StaffRequiredMixin, CreateView):
    model = Page
    form_class = PageForm
    success_url = reverse_lazy('pages:pages')

class pageUpdateView(StaffRequiredMixin, UpdateView):
    model = Page
    form_class = PageForm
    template_name_suffix = "_update_form"

    def get_success_url(self):
        return reverse_lazy('pages:update', args = [self.object.id]) + '?ok'

class pageDeleteView(StaffRequiredMixin, DeleteView):
    model = Page
    success_url = reverse_lazy('pages:pages')



