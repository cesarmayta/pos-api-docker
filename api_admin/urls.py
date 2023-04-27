from rest_framework.routers import DefaultRouter
from django.urls import path,include

from . import views

router  = DefaultRouter()

router.register(r'mesa',views.MesaViewSet,basename='mesas')
router.register(r'categoria',views.CategoriaViewSet,basename='categorias')
router.register(r'plato',views.PlatoViewSet,basename='platos')



urlpatterns = [
    path('',include(router.urls)),
    path('plato/uploadimg',views.UploadPlatoImagenView.as_view())
]