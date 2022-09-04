from django.urls import include, path
from rest_framework import routers
from . import views

# router = routers.DefaultRouter()
# router.register(r'cards', views.CardViewSet.as_view())
# router.register(r'states', views.StateViewSet.as_view())

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
        path('cards/', views.CardViewSet.as_view({'get': 'list'})),
        path('states/', views.StateViewSet.as_view()),
        path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
