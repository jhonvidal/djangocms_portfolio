# coding : utf-8

from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from cms.toolbar_pool import toolbar_pool
from cms.toolbar.items import Break
from cms.cms_toolbars import ADMIN_MENU_IDENTIFIER, ADMINISTRATION_BREAK
from cms.toolbar_base import CMSToolbar


@toolbar_pool.register
class PortfolioToolbar(CMSToolbar):
    def populate(self):
        admin_menu = self.toolbar.get_or_create_menu('portfolio', _('Works'))

        # Urls
        url_list_work = reverse('admin:portfolio_work_changelist')
        url_add_work = reverse('admin:portfolio_work_add')
        url_list_category = reverse('admin:portfolio_categorywork_changelist')
        url_add_category = reverse('admin:portfolio_categorywork_add')

        # Works
        admin_menu.add_sideframe_item(_('Add Work'), url=url_add_work)
        admin_menu.add_sideframe_item(_('Works'), url=url_list_work)
        admin_menu.add_break()

        # Categories
        admin_menu.add_sideframe_item(_('Add Category'), url=url_add_category)
        admin_menu.add_sideframe_item(_('Categories'), url=url_list_category)
        admin_menu.add_break()
