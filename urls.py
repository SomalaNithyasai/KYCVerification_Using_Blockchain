from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", view=views.index, name="Index"),
    path("submit/", view=views.submit, name="Submit"),
    path("login/", view=views.login, name="login"),
    path("adminPart/", view=views.adminPart, name="admin"),
    path("view_organisation/", view=views.viewOrgnisations, name="admin"),
    path("user/", view=views.user, name="user"),
    path("organisation/", view=views.organisation, name="organisation"),
    path("uploadMyDetails/", view=views.uploadMyDetails, name="uploadMyDetails"),
    path("updatePoint/", view=views.updatePoint, name="updatePoint"),
    path("profile/", view=views.profile, name="profile"),

]
