from django.urls import path
from .views import HomeView, ArticleDetailView, AddPostView, UpdatePostView, DeletePostView, \
    CategoryDetailView, AddCategoryView, UpdateCategoryView, DeleteCategoryView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),

    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
    path('add_post/', AddPostView.as_view(), name="add-post"),
    path('article/<int:pk>/edit', UpdatePostView.as_view(), name="update-post"),
    path('article/<int:pk>/delete', DeletePostView.as_view(), name="delete-post"),

    path('Category/<int:pk>', CategoryDetailView.as_view(), name='category-detail'),
    path('add_category/', AddCategoryView.as_view(), name="add-category"),
    path('Category/<int:pk>/edit', UpdateCategoryView.as_view(), name="update-category"),
    path('Category/<int:pk>/delete', DeleteCategoryView.as_view(), name="delete-category")

]
