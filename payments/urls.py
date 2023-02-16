from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('cancel/', CancelView.as_view(), name='cancel'),
    path('create-payment-intent/<pk>/', StripeIntentView.as_view(), name='create-payment-intent'),
    path('success/', SuccessView.as_view(), name='success'),
    path('create-checkout-session/<pk>/', CreateCheckoutSessionView.as_view(), name='create-checkout-session'),
    path('', HomePageView.as_view(), name='home-page'),
    path('item/<pk>', ProductLandingPageView.as_view(), name='landing'),
]
