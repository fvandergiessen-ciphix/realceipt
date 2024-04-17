from django.urls import path
from django.urls.conf import include
from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register('receipts', views.ReceiptViewSet)

receipt_router = routers.NestedDefaultRouter(router, 'receipts', lookup='receipts')
receipt_router.register('receipts', views.ReceiptViewSet, basename='receipts')
receipt_router.register('files', views.ReceiptFileViewSet, basename='receipts-files')

urlpatterns = router.urls + receipt_router.urls