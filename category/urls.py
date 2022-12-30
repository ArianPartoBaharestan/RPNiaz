from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('category', views.CategoryView)
router.register('brand', views.BrandView)
urlpatterns = router.urls

