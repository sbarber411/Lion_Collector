from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  # route for cats index
  path('lions/', views.lions_index, name='index'),
  path('lions/<int:lion_id>/', views.lions_detail, name='details'),
]
