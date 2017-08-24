
# coding: utf-8

#Import Models

from portfolio.models import Work, CategoryWork
from django import template

register = template.Library()

@register.inclusion_tag('portfolio/tags/latest_work.html')
def get_latest_work(numbers_of_works):
    latest_works = Work.objects.order_by('-pub_date')[:numbers_of_works]
    return {'latest_works': latest_works}

@register.inclusion_tag('portfolio/tags/work_categories_filters.html')
def list_work_categories():
    categories = CategoryWork.objects.all().order_by('title')
    return {'categories': categories}