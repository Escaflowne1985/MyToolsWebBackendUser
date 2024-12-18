# -*- coding: UTF-8 -*-

from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import *

router = DefaultRouter()

# router.register('Payment', PaymentViewSet, 'Payment')


urlpatterns = [
    path('stop_task/', stop_task, name='stop_task'),
]
urlpatterns += router.urls
