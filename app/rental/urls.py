from django.urls import path
from django.urls.conf import include

from rest_framework.routers import DefaultRouter

from rental import views

router = DefaultRouter()
router.register('features', views.OptionViewSet)
router.register('districts', views.DistrictViewSet)
router.register('houses', views.HouseViewSet)

app_name = 'rental'

urlpatterns = [
    path('', include(router.urls))
]