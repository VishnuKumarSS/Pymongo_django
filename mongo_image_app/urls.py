from django.urls import path

from .views import image_upload_view

app_name = 'mongo_image_app'

urlpatterns = [
    path('upload/', image_upload_view)
]