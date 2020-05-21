from django.urls import path
from .views import Persons_list, Persons_new, Persons_update, Persons_delete
from .views import PersonList


urlpatterns = [
    path('list/', Persons_list, name="person_list"),
    path('person_list/', PersonList.as_view(), name="person_list"),
    path('new/', Persons_new, name="person_new"),
    path('update/<int:id>', Persons_update, name="person_update"),
    path('delete/<int:id>', Persons_delete, name="person_delete"),
]
