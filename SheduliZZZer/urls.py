from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from .views import GetData, UpdateEvents, UpdateExperts, UpdateImages, UpdateDefaultEvents

app_name = 'SheduliZZZer'

urlpatterns = [
    path('get_data/', GetData.as_view()),
    path('update_events/', UpdateEvents.as_view()),
    path('update_experts/', UpdateExperts.as_view()),
    path('update_images/', UpdateImages.as_view()),
    path('update_default_events/', UpdateDefaultEvents.as_view()),
]

urlpatterns += staticfiles_urlpatterns()