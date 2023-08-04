from rest_framework.routers import SimpleRouter

from insurance.views import ClientViewSet, InsuranceViewSet


urlpatterns = []

router = SimpleRouter()
router.register('clients', ClientViewSet)
router.register('insurances', InsuranceViewSet)

urlpatterns += router.urls
