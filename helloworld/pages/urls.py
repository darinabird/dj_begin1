from django.urls import path
from .views import homePageView

# URLpattern has three parts:
#   - a Python regular expression for the empty string ''
#   - specify the view which is called homePageView
#   - add an optional URL name of 'home'

urlpatterns = [
    path('', homePageView, name='home')
]
