from django.urls import path
from . import views

urlpatterns = [
    path('', views.index , name='landing page'),
    path('analyze',views.analyzepage,name='analyzepage'),
    path('calculations', views.calculation , name='calculation')
]