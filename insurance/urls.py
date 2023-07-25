from rest_framework.routers import SimpleRouter

from insurance.views import ClientViewSet, InsuranceViewSet


urlpatterns = []

router = SimpleRouter()
router.register('client', ClientViewSet)
router.register('insurance', InsuranceViewSet)

urlpatterns += router.urls
