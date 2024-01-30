from django.urls import path
from django.views.generic import RedirectView
from webapp.views import IndexView, ArticleCreateView, ArticleView, ArticleUpdateView, ArticleDeleteView, \
    CommentCreateView, CommentUpdateView, CommentDeleteView, toggle_like

app_name = 'webapp'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('articles/', RedirectView.as_view(pattern_name='webapp:index')),
    path('articles/add/', ArticleCreateView.as_view(), name='article_create'),
    path('article/<int:pk>/', ArticleView.as_view(), name='article_view'),
    path('article/<int:pk>/update/', ArticleUpdateView.as_view(), name='article_update_view'),
    path('article/<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete_view'),
    path('article/<int:pk>/comment/add/', CommentCreateView.as_view(), name='comment_add'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment_update_view'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete_view'),
    path('api/toggle_like/<str:model_name>/<int:item_id>/', toggle_like, name='toggle_like'),
]
