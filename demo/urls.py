from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('verify_otp/', views.verify_otp, name='verify_otp'),
    path('login/', views.login_view, name='login'),
    path('home/', views.home_view, name='home'),
    path('profile/', views.user_profile, name='user_profile'),
    path('profile_success/', views.profile_success, name='profile_success'),
    path('recipe_list/', views.recipe_list_view, name='recipe_list'),
    path('recipe_detail/<int:recipe_id>/', views.recipe_detail_view, name='recipe_detail'),
    path('feedback/', views.feedback_page, name='feedback_page'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.home_view, name='root'),
]
