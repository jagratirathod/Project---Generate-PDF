from django.urls import path
from users import views as user_views



urlpatterns = [
    # path('',views.hello),
    path('', user_views.UserListView.as_view(), name='user_list_view'),
    path('pdf/<pk>', user_views.users_render_pdf_view, name='user_pdf_view'),
]   