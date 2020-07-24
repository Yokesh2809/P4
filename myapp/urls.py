from django.urls import path
from myapp import views

app_name="myapp"#is used to creatq a namespace
urlpatterns = [
    #path("secondary suffix",address of function, name of mapping)
    path('',views.index,name='index'),
    path('home',views.home,name="home"),
    path('fact/<n>',views.fact,name="fact"),
]
