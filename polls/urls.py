from .views import football, basketball, box, detail
from django.urls import path

urlpatterns = [
    path('football/', football),
    path('basketball/',basketball),
    path('box/', box),
    path('detail/<int:sport_id>', detail)
]