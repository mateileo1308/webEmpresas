from django.urls import path
from .views import ProfilesListView, ProfileDetailView

urlpatterns = [
    path('', ProfilesListView.as_view(), name="Profiles"),
    path('<username>/', ProfileDetailView.as_view(), name='detail'),
]

"""
    path('<int:pk>/<slug:page_slug>/', pageDetailView.as_view(), name='page'),
    path('create/', pageCreateView.as_view(), name='create'),
    path('update/<int:pk>/', pageUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', pageDeleteView.as_view(), name='delete'),
"""