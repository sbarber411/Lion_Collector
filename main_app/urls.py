from django.urls import path

from . import views


urlpatterns = [
	path('', views.home, name='home'), 
	path('about/', views.about, name='about'),
	path('lions/', views.lions_index, name='index'),
	path('lions/<int:lion_id>/', views.lions_detail, name='detail'),
    path('lions/create/', views.LionCreate.as_view(), name='lions_create'),
    path('lions/<int:pk>/update/', views.LionUpdate.as_view(), name='lions_update'),
    path('lions/<int:pk>/delete/', views.LionDelete.as_view(), name='lions_delete'),
    path('lions/<int:lion_id>/add_feeding/', views.add_feeding, name='add_feeding'),
    path('lions/<int:lion_id>/assoc_toy/<int:toy_id>/', views.assoc_toy, name='assoc_toy'),
    path('toys/', views.ToyList.as_view(), name='toys_index'),
    path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toys_detail'),
    path('toys/create/', views.ToyCreate.as_view(), name='toys_create'),
    path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toys_update'),
    path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toys_delete'),
]