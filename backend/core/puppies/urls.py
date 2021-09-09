from django.urls import path

from .views import PuppiesList, PuppyDetail

urlpatterns = [
    path('puppies/', PuppiesList.as_view(), name='puppies_list'),
    path('puppy/<int:pk>/', PuppyDetail.as_view(), name='puppy_detail'),
]
