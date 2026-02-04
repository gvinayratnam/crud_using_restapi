from django.urls import path
from . import views

urlpatterns = [
    path('/',views.Booklist),
    path('post/',views.post_Booklist),
    path('put/<int:id>/',views.update_Booklist),
    path('del/<int:id>/',views.dele_book),
]
