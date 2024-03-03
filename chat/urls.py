from django.urls import path
from .views import process_data, JsonUploadAPIView

urlpatterns = [
    path('predict/', process_data, name='predict'),
    path('json_upload/', JsonUploadAPIView.as_view(), name='intents_upload'),
]

