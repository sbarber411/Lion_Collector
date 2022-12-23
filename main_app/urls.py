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
]