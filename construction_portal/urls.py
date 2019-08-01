from django.conf.urls import url
from src.views.userview import UserView

urlpatterns = [
    url(r'^user/', UserView.as_view()),

]
