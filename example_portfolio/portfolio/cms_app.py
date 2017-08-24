from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _


class PortfolioApphook(CMSApp):
    name = _("Portfolio")
    urls = ["portfolio.urls", ]

apphook_pool.register(PortfolioApphook)