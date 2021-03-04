from rest_framework import routers
from Products.views import ProductViewSet
from rest_framework import renderers

router = routers.DefaultRouter()
router.register('products',ProductViewSet)
