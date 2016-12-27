from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index ),
    url(r'^school_list_process$', views.school_list_process),
    # url(r'^school_profile_process$', views.school_profile_process),
    # url(r'^school_profile$', views.school_profile),
    # url(r'^school_list$', views.school_list),

    # url(r'^school_list/(?P<school_name>\w)/$', views.school_list),
    # url(r'^school_profile_process/(?P<school_name>\w)$', views.school_profile_process),
    # url(r'^school_profile/(?P<school_name>\w)/$', views.school_profile),
    # url(r'^ninjas/(?P<color>\w{0,10})/$', views.colors)
]
