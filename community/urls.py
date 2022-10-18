from django.urls import path
from community import views

app_name = 'community'

urlpatterns = [

    path('', views.index, name='index'),
    path('<int:article_id>/',views.article_detail, name="article_detail"),
    path('creative_article/',views.creative_article, name='creative_article'),
    

]
