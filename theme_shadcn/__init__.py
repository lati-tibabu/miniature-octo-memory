# -*- coding: utf-8 -*-
from odoo import models

class ThemeShadcn(models.AbstractModel):
    _inherit = 'theme.utils'

    def _theme_shadcn_post_copy(self, mod):
        self.disable_view('website.template_header_default')
        self.enable_view('theme_shadcn.header')
        self.enable_view('theme_shadcn.footer')
