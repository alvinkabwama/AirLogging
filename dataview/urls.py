from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^datarecieve/',views.datarecieve),
    url(r'^datasend/',views.datasend),
    url(r'^datashow/',views.datashow),
]


