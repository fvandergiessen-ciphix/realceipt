from django.urls import path
from django.urls.conf import include
from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register('receipts', views.ReceiptViewSet)
router.register('newreceipt', views.NewReceiptViewSet, basename='new-receipt')

receipt_router = routers.NestedDefaultRouter(router, 'receipts', lookup='receipts')
receipt_router.register('item', views.ReceiptItemViewSet, basename='receipt-items')

urlpatterns = router.urls + receipt_router.urls + [path('homepage/', views.hello)] 