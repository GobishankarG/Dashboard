from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("login", views.login, name='login'),
    path("register", views.register, name='register'),
    path("table", views.table, name='table'),
    path("buttons", views.buttons, name="buttons"),
    path("dropdowns", views.dropdowns, name="dropdowns"),
    path("typography", views.typography, name="typography"),
    path("basic_elements", views.basic_elements, name="basic_elements"),
    path("chartjs", views.chartjs, name="chartjs"),
    path("mdi", views.mdi, name="mdi"),
    path("error_404", views.error_404, name="error_404"),
    path("error_500", views.error_500, name="error_500"),
    path("form", views.form, name="form"),
    path("view_data", views.view_data, name="view_data"),
    path("save_data", views.save_data, name="save_data"),
    path("update_page/<int:id>", views.update_page, name="update_page"),
    path("delete/<int:id>", views.delete, name="delete"),
    path('delete_multiple/', views.delete_multiple_items, name='delete_multiple_items')
]