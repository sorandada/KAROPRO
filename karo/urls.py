from django.urls import path, include
from .views import KaroList, KaroDetail, KaroCreate, KaroDelete, KaroUpdate, fulldelete



urlpatterns = [
    path("list/", KaroList, name="list"),
    path("detail/<int:pk>", KaroDetail.as_view(), name="detail"),
    path("create/", KaroCreate.as_view(), name="create"),
    path("delete/<int:pk>", KaroDelete.as_view(), name="delete"),
    path("update/<int:pk>", KaroUpdate.as_view(), name="update"),

    path("fulldelete/", fulldelete, name="fulldelete"),
    
]