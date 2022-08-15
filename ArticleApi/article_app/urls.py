from django.urls import path
from .views import GenericApiView

# from .views import ArticleList, ArticleDetail
#from .views import article_list, article_detail,

urlpatterns = [
    #function based Urls
    # path('article/', article_list),
    # path('article-detail/<int:pk>', article_detail),

    #Class based views
    # path('article/', ArticleList.as_view()),
    # path('article-detail/<int:id>', ArticleDetail.as_view()),

    path('article/<int:id>', GenericApiView.as_view()),
    path('article/', GenericApiView.as_view()),

]
