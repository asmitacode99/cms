from django.conf import settings
from rest_framework.routers import DefaultRouter
from rest_framework.routers import SimpleRouter
from cms.users.api.v1.views import UserViewSet


router = DefaultRouter() if settings.DEBUG else SimpleRouter()
  
router.register("user", UserViewSet)

app_name = "api"
urlpatterns = router.urls
