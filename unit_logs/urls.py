"""Defines a  URL pattern for unit_logs"""

from django.urls import path

from . import views

app_name = 'unit_logs'
urlpatterns = [
    # Home page
    path('', views.units, name='index'),
    # Page that shows all units
    path('units/', views.units, name='units'),
    # Detail page for a single unit
    path('units/<int:unit_id>/', views.unit, name='unit'),
    # Pages that show the units
    path('winx/', views.winx, name='winx'),
    path('enable/', views.enable, name='enable'),
    path('arkle/', views.arkle, name='arkle'),
    path('denman/', views.denman, name='denman'),
    path('kauto/', views.kauto, name='kauto'),
    path('frankel/', views.frankel, name='frankel'),
    # Page for adding a new unit
    path('new_unit/', views.new_unit, name='new_unit'),
    # Page for viewing unit
    path('unit/<int:unit_pk>', views.show_unit, name='show_unit'),
    # Page for deleting unit
    path('unit/<int:unit_pk>/delete', views.delete_unit, name='delete_unit'),
    
]