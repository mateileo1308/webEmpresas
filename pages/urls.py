from django.urls import path
from .views import pagesListView, pageDetailView, pageCreateView
from . import views

urlpatterns = [
    path('', pagesListView.as_view(), name='pages'),
    path('<int:pk>/<slug:page_slug>/', pageDetailView.as_view(), name='page'),
    path('create/', pageCreateView.as_view(), name='pageCreation'),
]


