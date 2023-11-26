from rest_framework import routers
from .views import PersonViewSet, ContactViewSet

router = routers.DefaultRouter()
router.register(r'person', PersonViewSet)
router.register(r'contact', ContactViewSet)

urlpatterns = router.urls
