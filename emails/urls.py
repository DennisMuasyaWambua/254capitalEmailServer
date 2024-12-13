from django.urls import path
from .views import ContactFormView, LoanApplicationView

urlpatterns = [
    path('contact/', ContactFormView.as_view()),
    path('loan-applications/', LoanApplicationView.as_view()),
]