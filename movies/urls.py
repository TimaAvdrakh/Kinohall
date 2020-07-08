from django.urls import path
from .views import index, by_gender, moviepage, RegisterUserView, SearchResultsView, RegisterDoneView, MLoginView, serialspage, series_by_gender, contact, ChangeUserInfoView, MPasswordChangeView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('accounts/password/change', MPasswordChangeView.as_view(), name='password_change'),
    path('accounts/profile/', ChangeUserInfoView.as_view(), name='profile'),
    path('accounts/register/done', RegisterDoneView.as_view(), name='register_done'),
    path('accounts/register/', RegisterUserView.as_view(), name='register'),
    path('accounts/login/', MLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('<int:gender_id>/', by_gender, name='by_gender'),
    path('contact/', contact, name='contact'),
    path('series/gender/<int:gender_id>', series_by_gender, name='series_by_gender'),
    path('series/<int:series_id>/', serialspage, name='seriespage'),
    path('movie/<int:movie_id>/', moviepage, name='moviepage'),
    path('', index, name='index'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
]
