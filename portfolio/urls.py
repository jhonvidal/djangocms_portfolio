from django.conf.urls import *
from .views import PortfolioWorkListView, PortfolioWorkDetailView, WorkTagListView, WorkCategoryListView

urlpatterns = patterns('',
    url(r'^$', PortfolioWorkListView.as_view(), name='portfolio_list'),
    url(r'^tag/(?P<tag>[-\w]+)/$', WorkTagListView.as_view(), name='work_tag'),
    url(r'^category/(?P<category>[-\w]+)/$', WorkCategoryListView.as_view(), name='work_category'),
    url(r'^(?P<slug>[-\w]+)/$', PortfolioWorkDetailView.as_view(), name='work_detail'),
)