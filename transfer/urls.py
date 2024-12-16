from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('accounts',views.Accountviewset)

urlpatterns = [
    path('',include(router.urls)),
    path('home', views.transfer_funds_page, name='transfer_funds_page')
    
]




