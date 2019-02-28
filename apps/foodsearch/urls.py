from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index), #home
    url(r'^search$', views.process), #search processing
    url(r'^addrecipe$', views.add_recipe), #add recipe processing
    url(r'^add$', views.view_add), #view add recipe/ingredients
    url(r'^addingre$', views.add_ingre), #add ingredients processing
    url(r'^delete_recipe/(?P<id>\d+)$', views.delete_recipe), #delete recipe processing
    url(r'^delete_ingre/(?P<id>\d+)$', views.delete_ingre), #delete ingredient processing
    url(r'^delete_ingre/(?P<reid>\d+)/(?P<inid>\d+)$', views.delete_ingre_recipe),
    url(r'^dashboard$', views.view_admin), #view database ALL (ingredients and Recipe)
    url(r'^dashboard/addtoge$', views.view_addtoge), #view database ALL (ingredients and Recipe)
    url(r'^dashboard/viewdatabase$', views.view_database),
    url(r'^admin$', views.admin_login), #view admin login page
    url(r'^login$', views.logacc), #button login admin
    url(r'^logout$', views.logoutacc),
    url(r'^edit_recipe/(?P<id>\d+)$', views.edit_recipe), #edit recipe processing
    url(r'^edit_ingre/(?P<id>\d+)$', views.edit_ingre), #edit ingredients processing
    url(r'^BTeditingre$', views.BTeditingre), #button edit ingre
    url(r'^BTeditrecipe$', views.BTeditrecipe), #button edit recipe
    url(r'^detail/(?P<id>\d+)$', views.fulldetail),
    url(r'^test$', views.viewtest),
    url(r'^addtogether$', views.addtogether),
    # url(r'^search/(?P<txtsearch>\w+)$', views.findrecipe),
]