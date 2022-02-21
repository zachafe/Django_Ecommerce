from django.urls import path

from app.reports.views import ReportSaleView

urlpatterns = [
    # reports
    path('sale/', ReportSaleView.as_view(), name='sale_report'),
]