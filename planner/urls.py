from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about, name='about'),
    # Replace the home path with blog feed page
    path('', views.planner_dashboard, name='home'),
    path('dashboard/', views.planner_dashboard, name='planner-dashboard'),
    path('holidays/', views.holidays_list, name='holiday-list'),
    path('holidays/new', views.HolidayCreate.as_view(), name='holiday-create'),
    path('holidays/<int:pk>/', views.holidays_detail, name='holiday-detail'),
    path('holidays/<int:holiday_id>/add_destination/',views.add_destination,name='add_destination'),
    path('holidays/<int:holiday_id>/destinations/<int:destination_id>/', views.destinations_detail, name='destinations-detail'),
    path('destinations/<int:destination_id>/itinerary/<int:itinerary_id>/', views.itinerary_detail, name='itinerary-detail'),
    path('accounts/signup/', views.signup, name='signup'),

]

# planner/itinery/add
# planner/itinery/<id>
# planner/itinery/<id>/edit
# planner/itinery/<id>/update
# planner/itinery/<id>/delete

# blog/
# blog/add
# blog/<id>