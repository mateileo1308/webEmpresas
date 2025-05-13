from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from registration.models import Profile


# Create your views here.
class ProfileListView(ListView):
    model = Profile
    template_name = 'profiles/profile_list.html'
    paginate_by = 1

    def get_template_names(self):
        template_names = super().get_template_names()
        print(f"Plantillas que Django intentará cargar: {template_names}")
        # Puedes forzar una plantilla específica aquí:
        # self.template_name = 'tu_app/tu_plantilla_personalizada.html'
        return template_names

class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'profiles/profile_detail.html'

    def get_object(self):
        return get_object_or_404(Profile, user__username=self.kwargs['username'])
