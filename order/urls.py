from . import views
from rest_framework_nested import routers
router = routers.DefaultRouter()
router.register('basket', views.BasketViewSet,basename='basket')
# basket_Router=routers.NestedDefaultRouter(router,'basket',lookup='basket_pk')
# basket_Router.register('items',views.OrderItemViewSet,basename='basket-items-detail')
urlpatterns = router.urls
# urlpatterns = router.urls +basket_Router.urls


