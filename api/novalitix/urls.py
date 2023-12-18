from django.urls import path
from .views import PredictionHouseAPIView, PredictionReviewAPIView

urlpatterns = [
    path('predict-house/', PredictionHouseAPIView.as_view(), name='predicthouse'),
    path('predict-review/', PredictionReviewAPIView.as_view(), name='predictreview'),
]

