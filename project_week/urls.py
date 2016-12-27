
from django.conf.urls import url, include

urlpatterns = [
    url(r'^', include ("apps.project_app.urls")),
]
