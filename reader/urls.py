from django.conf.urls import url
from reader.views import MainView

urlpatterns = [
    url('$^', MainView.as_view(), name='index'),
]
