# Copyright 2012-2021 Akretion France (http://www.akretion.com/)
# @author: Alexis de Lattre <alexis.delattre@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, models


class HrCandidate(models.Model):
    _name = "hr.candidate"
    _inherit = ["hr.candidate"]
    _phone_name_sequence = 50
    _phone_name_fields = ["partner_phone"]

    @api.onchange("partner_phone")
    def partner_phone_change(self):
        if self.partner_phone:
            self.partner_phone = self.phone_format(self.partner_phone)
