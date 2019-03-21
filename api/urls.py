
from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('team', views.MemberViews)

urlpatterns = [
    path('', include(router.urls)),
]
