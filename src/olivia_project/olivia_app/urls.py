from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name = "index"),
    path("contacto/<int:contacto_id>/",
         views.detalle_cont, name = "detalle_cont"),
    path("<int:usuario_id>/", views.index, name = "index"),
    path("<int:usuario_id>/contacto/<int:contacto_id>/",
         views.detalle_cont, name = "detalle_cont"),
    path("<int:usuario_id>/contacto/nuevo/",
         views.detalle_cont, name = "detalle_cont")
]
