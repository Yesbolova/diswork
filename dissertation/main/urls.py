from django.contrib.auth import login
from django.urls import path
from.import views
from django.contrib import admin
from django.urls import path,include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path (r'^admin/',admin.site.urls),
    path('', views.index, name = "index"),
    path("signup/", views.SignUp.as_view(), name="signup"),
    path('main', views.index),
    path ('about-us',views.about),
    path ('praktika',views.praktika),
    path ('datatype',views.datatype),
path ('arithmeticoperation',views.arithmeticoperation),
path ('syntax',views.syntax),
path ('inputandoutput',views.inputandoutput),
path ('linearalgortm',views.linearalgortm),
path ('workingwithfiles',views.workingwithfiles),
path ('programmingalgorithms01',views.programmingalgorithms01),
path ('programmingalgorithms02',views.programmingalgorithms02),
path ('programmingalgorithms03',views.programmingalgorithms03),
path ('programmingalgorithms04',views.programmingalgorithms04),
path ('operator01',views.operator01),
path ('operator02',views.operator02),
path ('operator03',views.operator03),
path ('operator04',views.operator04),
path ('operator05',views.operator05),
path ('operator06',views.operator06),
path ('task',views.task),
path ('informatiki',views.informatiki),
path ('olimpiada_esepteri',views.olimpiada_esepteri),
path ('birolshemdimassiv',views.birolshemdimassiv),
path ('ekiolshemdimassiv',views.ekiolshemdimassiv),
path ('trassirovka',views.trassirovka),
path ('suryptau',views.suryptau),
path ('orynauystyru',views.orynauystyru),
path ('zhoyujanekiristiru',views.zhoyujanekiristiru),
path ('bagalau',views.bagalau),
path ('maksat',views.maksat),
path ('pygame',views.pygame),
path ('task09',views.task09),
path ('string',views.string),
]+ static(settings.STATIC_URL,document_root = settings.STATIC_ROOT)
