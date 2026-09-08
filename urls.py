from django.urls import path
import views

urlpatterns = [
    path("", views.calculator, name="calculator"),
]
