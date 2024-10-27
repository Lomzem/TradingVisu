from django.urls import path
from . import views

urlpatterns = [
    path("", views.upload, name="upload"),
    path("upload_csv/", views.upload_csv, name="upload_csv"),
    # path("visualization/", views.visualization, name="visualization"),
]
