from django.urls import path
from community import views

app_name = 'community'

urlpatterns = [

    path('', views.index, name='index'),
    path('<int:article_id>/', views.article_detail, name="article_detail"),
    path('<int:article_id>/update_article/', views.update_article, name="update_article"),
    path('<int:article_id>/delete_article/', views.delete_article, name="delete_article"),
    path('creative_article/', views.creative_article, name='creative_article'),
    

]
