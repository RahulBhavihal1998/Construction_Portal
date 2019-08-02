from django.conf.urls import url
from src.views.userview import UserView
from src.views.loginview import LoginView

urlpatterns = [
    url(r'^user/', UserView.as_view()),
    url(r'^login/', LoginView.as_view())

]
