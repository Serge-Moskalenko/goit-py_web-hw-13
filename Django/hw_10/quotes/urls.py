from django.urls import path
from . import views

app_name = "quotes"

urlpatterns = [
    path("", views.main, name="root"),
    path("<int:page>", views.main, name="root_paginate"),
    path('add-author/', views.add_author, name='add_author'),
    path('add-quote/', views.add_quote, name='add_quote'),
    path('author/<str:author_id>/', views.author_detail, name='author_detail'),
    path('tag/<str:tag>/', views.quotes_by_tag, name='quotes_by_tag'),
    path('search-by-tag/', views.search_by_tag, name='search_by_tag'),

]
