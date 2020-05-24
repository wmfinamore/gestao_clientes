from django.urls import path
from .views import Persons_list, Persons_new, Persons_update, Persons_delete
from .views import PersonList, PersonDetail, PersonCreate


urlpatterns = [
    path('list/', Persons_list, name="person_list"),
    path('new/', Persons_new, name="person_new"),
    path('update/<int:id>', Persons_update, name="person_update"),
    path('delete/<int:id>', Persons_delete, name="person_delete"),
    path('person_list/', PersonList.as_view(), name="person_list_cbv"),
    path('person_detail/<int:pk>', PersonDetail.as_view(), name='person_detail_cbv'),
    path('person_create/', PersonCreate.as_view(), name='person_create_cbv'),
]
