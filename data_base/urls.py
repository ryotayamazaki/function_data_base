#!coding:utf-8
from django.conf.urls import patterns, url
from data_base import views

urlpatterns = [#patterns('',
#        url(r'^$', views.show, name='show'),
#        url(r'^edit/$', views.edit, name='edit'),
        url(r'^pkg/$', views.pkg_list, name='pkg_list'),   # 一覧
        url(r'^pkg/add/$', views.pkg_edit, name='pkg_add'),  # 登録
        url(r'^pkg/mod/(?P<pkg_id>\d+)/$', views.pkg_edit, name='pkg_mod'),  # 修正
        url(r'^pkg/del/(?P<pkg_id>\d+)/$', views.pkg_del, name='pkg_del'),   # 削除

        # 感想
        url(r'^proglam/(?P<pkg_id>\d+)/$', views.ProglamList.as_view(), name='proglam_list'),  # 一覧
        url(r'^proglam/add/(?P<pkg_id>\d+)/$', views.proglam_edit, name='proglam_add'),        # 登録
        url(r'^proglam/mod/(?P<pkg_id>\d+)/(?P<proglam_id>\d+)/$', views.proglam_edit, name='proglam_mod'),  # 修正
        url(r'^proglam/del/(?P<pkg_id>\d+)/(?P<proglam_id>\d+)/$', views.proglam_del, name='proglam_del'),   # 削除

        url(r'^function/(?P<proglam_id>\d+)/$', views.FunctionList.as_view(), name='function_list'),  # 一覧
        url(r'^function/add/(?P<proglam_id>\d+)/$', views.function_edit, name='function_add'),        # 登録
        url(r'^function/mod/(?P<proglam_id>\d+)/(?P<function_id>\d+)/$', views.function_edit, name='function_mod'),  # 修正
        url(r'^function/del/(?P<proglam_id>\d+)/(?P<function_id>\d+)/$', views.function_del, name='function_del'),   # 削除
        url(r'^function/view/(?P<function_id>\d+)/$', views.function_view, name='function_view'),

        url(r'^pkg/del_check/(?P<target_id>\d+)/$', views.pkg_del_check, name='pkg_del_check'),
        url(r'^proglam/del_check/(?P<target_id>\d+)/(?P<link_id>\d+)/$', views.pro_del_check, name='pro_del_check'),
        url(r'^function/del_check/(?P<target_id>\d+)/(?P<link_id>\d+)/$', views.func_del_check, name='func_del_check'),

        url(r'^pkg/updated/(?P<pkg_id>\d+)/$', views.PkgUpdatedList.as_view(), name='pkgupdated_list'),
        url(r'^pkg/updated/add/(?P<pkg_id>\d+)/$', views.pkgupdated_edit, name='pkgupdated_add'),        # 登録
        url(r'^pkg/updated/mod/(?P<pkg_id>\d+)/(?P<pkgupdated_id>\d+)/$', views.pkgupdated_edit, name='pkgupdated_mod'),  # 修正
        url(r'^pkg/updated/del/(?P<pkg_id>\d+)/(?P<pkgupdated_id>\d+)/$', views.pkgupdated_del, name='pkgupdated_del'),
        url(r'^pkg/updated/del_check/(?P<target_id>\d+)/(?P<link_id>\d+)/$', views.pkgupdated_del_check, name='pkgupdated_del_check'),

        url(r'^proglam/updated/(?P<proglam_id>\d+)/$', views.ProglamUpdatedList.as_view(), name='proglamupdated_list'),
        url(r'^proglam/updated/add/(?P<proglam_id>\d+)/$', views.proglamupdated_edit, name='proglamupdated_add'),        # 登録
        url(r'^proglam/updated/mod/(?P<proglam_id>\d+)/(?P<proglamupdated_id>\d+)/$', views.proglamupdated_edit, name='proglamupdated_mod'),  # 修正
        url(r'^proglam/updated/del/(?P<proglam_id>\d+)/(?P<proglamupdated_id>\d+)/$', views.proglamupdated_del, name='proglamupdated_del'),
        url(r'^proglam/updated/del_check/(?P<target_id>\d+)/(?P<link_id>\d+)/$', views.proglamupdated_del_check, name='proglamupdated_del_check'),
        
        url(r'^function/updated/(?P<function_id>\d+)/$', views.FunctionUpdatedList.as_view(), name='functionupdated_list'),
        url(r'^function/updated/add/(?P<function_id>\d+)/$', views.functionupdated_edit, name='functionupdated_add'),        # 登録
        url(r'^function/updated/mod/(?P<function_id>\d+)/(?P<functionupdated_id>\d+)/$', views.functionupdated_edit, name='functionupdated_mod'),  # 修正
        url(r'^function/updated/del/(?P<function_id>\d+)/(?P<functionupdated_id>\d+)/$', views.functionupdated_del, name='functionupdated_del'),
        url(r'^function/updated/del_check/(?P<target_id>\d+)/(?P<link_id>\d+)/$', views.functionupdated_del_check, name='functionupdated_del_check'),

        url(r'search/$',views.search, name='search'),  # 検索
#        url(r'result/$',views.result, name='result'), #結果
]#)
