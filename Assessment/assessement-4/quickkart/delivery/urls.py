from rest_framework.routers import DefaultRouter
from .views import DeliveryOrderViewSet, DeliveryAgentViewSet

router = DefaultRouter()
router.register('orders', DeliveryOrderViewSet)
router.register('agents', DeliveryAgentViewSet)

urlpatterns = router.urls
