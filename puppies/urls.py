from django.urls import path

from .views import PuppiesList, PuppyDetail, PuppyCreate, PuppyDelete, PuppyUpdate

urlpatterns = [
    path('puppies/', PuppiesList.as_view(), name='puppies_list'),
    path('puppy/<int:pk>/', PuppyDetail.as_view(), name='puppy_detail'),
    path('puppy/new/', PuppyCreate.as_view(), name='new_puppy'),
    path('puppy/delete/<int:pk>/', PuppyDelete.as_view(), name='delete_puppy'),
    path('puppy/update/<int:pk>/', PuppyUpdate.as_view(), name='update_puppy'),
]
