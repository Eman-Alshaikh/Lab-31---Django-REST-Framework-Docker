from django.urls import path
from  sweets.api.viewset import (
    SweetsListApiView,
    SweetsDetailApiView,

)
urlpatterns=[


    path('api/v1/sweets-list',SweetsListApiView.as_view(),name='sweets_list'),
        path('api/v1/<int:pk>',SweetsListApiView.as_view(),name='sweet_detail'),

]