# coding: utf-8

# Django db
from django.db import models

# Fields (Requirements)
from djangocms_text_ckeditor.fields import HTMLField

# Filer (Requirements)
from filer.fields.image import FilerImageField
from filer.fields.folder import FilerFolderField

# Taggit (Requirements)
from taggit.managers import TaggableManager

# Reverse
from django.urls import reverse

# I18N
from django.utils.translation import ugettext as _


class CategoryWork(models.Model):
    title = models.CharField(_('Title'), max_length=255)
    slug = models.SlugField()

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self):
        return self.title


class Work(models.Model):
    title = models.CharField(_('Title'), max_length=200)
    slug = models.SlugField()
    pub_date = models.DateTimeField(_('Published on'), auto_now_add=True)
    description = HTMLField(_('Work Description'))
    category = models.ForeignKey(CategoryWork, verbose_name=_('Category'), on_delete=models.CASCADE,)
    tags = TaggableManager()
    client = models.CharField(_('Client'), max_length=255, null=True, blank=True)
    location = models.CharField(_('Location'), max_length=255, null=True, blank=True)
    head_picture = FilerImageField(verbose_name=_("Head"))
    folder = FilerFolderField(verbose_name=_('Gallery Folder'), null=True, blank=True)

    class Meta:
        verbose_name = _('Work')
        verbose_name_plural = _('Works')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('work_detail', args=[self.slug])

    def get_next_work(self):
        try:
            next_work = Work.objects.get(pk=self.pk + 1)
            return reverse('work_detail', args=[next_work.slug])
        except:
            return None

    def get_previous_work(self):
        try:
            previous_work = Work.objects.get(pk=self.pk - 1)
            return reverse('work_detail', args=[previous_work.slug])
        except:
            return None
