from django.urls import path
from . import views


urlpatterns = [
   path('create', views.add_rso, name='add_rso'),
   path('', views.list_rsos, name = 'list_rsos'),
   # path('details', views.rso_info, name='rso_info')
   path('<int:rso_id>', views.rso_info, name='rso_info')
]