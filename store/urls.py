from django.urls import path

from . import views

urlpatterns = [
	#Leave as empty string for base url
	path('', views.store, name="store"),
	path("logout/", views.logout_view, name="logout"),
	path("login/", views.login_request, name="login"),
	path('register/', views.register_request, name="register"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),
	path("details/<int:pk>/",views.details,name="details"),
	# path("cars/<str:cat>",views.cat,name="cars"),
	# path("jeeps/<str:cat>",views.cat,name="jeeps"),
	# path("bikes/<str:cat>",views.cat,name="bikes"),
	# path("cycles/<str:cat>",views.cat,name="cycles"),
]