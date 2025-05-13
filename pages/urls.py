from django.urls import path
from .views import pagesListView, pageDetailView, pageCreateView, pageUpdateView, pageDeleteView
from . import views

pages_patterns = ([
    path('', pagesListView.as_view(), name='pages'),
    path('<int:pk>/<slug:page_slug>/', pageDetailView.as_view(), name='page'),
    path('create/', pageCreateView.as_view(), name='create'),
    path('update/<int:pk>/', pageUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', pageDeleteView.as_view(), name='delete'),
], 'pages')
