from django.urls import path
from .views import DashboardSummary

urlpatterns = [
    path('dashboard/summary/', DashboardSummary.as_view()),
]