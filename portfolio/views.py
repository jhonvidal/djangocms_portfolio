from django.shortcuts import render

# Generics views
from django.views.generic import ListView, DetailView

# Models
from .models import Work

# Paginator
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger


# Settings
from django.conf import settings


class PortfolioWorkListView(ListView):
    model = Work
    template_name = 'portfolio/portfolio_work_list.html'
    context_object_name = "work_list"
    paginate_by = settings.WORK_PAGINATION

    def get_context_data(self, **kwargs):
        context = super(PortfolioWorkListView, self).get_context_data(**kwargs)
        context['WORK_LIST_TRUNCWORDS_COUNT'] = settings.WORK_LIST_TRUNCWORDS_COUNT
        list_work = Work.objects.all().order_by('pub_date')
        paginator = Paginator(list_work, self.paginate_by)

        page = self.request.GET.get('page')

        try:
            list_work = paginator.page(page)
        except PageNotAnInteger:
            list_work = paginator.page(1)
        except EmptyPage:
            list_work = paginator.page(paginator.num_pages)

        context['list_work'] = list_work
        return context


class PortfolioWorkDetailView(DetailView):
    model = Work
    template_name = 'portfolio/portfolio_work_detail.html'


class WorkCategoryListView(ListView):
    model = Work
    context_object_name = 'work_list'
    template_name = 'portfolio/portfolio_work_list.html'
    paginate_by = settings.WORK_PAGINATION
    view_url_name = 'portfolio:work_category'

    def get_queryset(self):
        qs = super(WorkCategoryListView, self).get_queryset()
        return qs.filter(category__slug=self.kwargs['category'])

    def get_context_data(self, **kwargs):
        paginator = Paginator(self.get_queryset(), self.paginate_by)
        kwargs['category'] = (self.kwargs.get('category')
                              if 'category' in self.kwargs else None)
        context = super(WorkCategoryListView, self).get_context_data(**kwargs)
        context['WORK_LIST_TRUNCWORDS_COUNT'] = settings.WORK_LIST_TRUNCWORDS_COUNT

        page = self.request.GET.get('page')

        try:
            list_work = paginator.page(page)
        except PageNotAnInteger:
            list_work = paginator.page(1)
        except EmptyPage:
            list_work = paginator.page(paginator.num_pages)

        context['list_work'] = list_work
        return context


class WorkTagListView(ListView):
    model = Work
    context_object_name = 'work_list'
    template_name = 'portfolio/portfolio_work_list.html'
    paginate_by = settings.WORK_PAGINATION
    view_url_name = 'portfolio:work_tag'

    def get_queryset(self):
        qs = super(WorkTagListView, self).get_queryset()
        return qs.filter(tags__slug=self.kwargs['tag'])

    def get_context_data(self, **kwargs):
        paginator = Paginator(self.get_queryset(), self.paginate_by)
        kwargs['tag'] = (self.kwargs.get('tag')
                              if 'tag' in self.kwargs else None)
        context = super(WorkTagListView, self).get_context_data(**kwargs)
        context['WORK_LIST_TRUNCWORDS_COUNT'] = settings.WORK_LIST_TRUNCWORDS_COUNT

        page = self.request.GET.get('page')

        try:
            list_work = paginator.page(page)
        except PageNotAnInteger:
            list_work = paginator.page(1)
        except EmptyPage:
            list_work = paginator.page(paginator.num_pages)

        context['list_work'] = list_work
        return context