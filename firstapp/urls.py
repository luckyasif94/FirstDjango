from django.urls import path
from . import views

urlpatterns = [
    path('exam', views.ExamPage, name="exam"),
    path('viewdetails', views.viewDetails, name="viewdetails"),
    path('editdetails/<int:id>', views.editDetails, name="editdetails"),
    path('deletedetails/<int:id>', views.deleteDetails, name="deletedetails"),
    path('update/<int:id>', views.update, name="update"),

    path('register',views.registerPage,name='register'),
    path('login',views.loginPage,name='login'),
    path('registerprocess',views.registerProcess,name='registerprocess'),
    path('loginprocess',views.loginProcess,name='loginprocess'),
    path('logout', views.logout1, name='logout1'),

    path('AdminHome', views.AdminHome, name='AdminHome'),
    path('UserHome', views.UserHome, name='UserHome'),

    path('imageupload', views.imagePage, name='image'),
    path('imageprocess', views.imageProcess, name='imageprocess'),

]