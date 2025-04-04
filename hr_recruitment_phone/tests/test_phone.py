# Copyright 2021 Akretion France (http://www.akretion.com/)
# @author: Alexis de Lattre <alexis.delattre@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo.addons.base.tests.common import BaseCommon


class TestRecruitmentPhone(BaseCommon):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.fr_country_id = cls.env.ref("base.fr").id
        cls.phco = cls.env["phone.common"]
        cls.env.company.write({"country_id": cls.fr_country_id})
        cls.partner = cls.env["res.partner"].create(
            {
                "name": "Partner 0",
                "country_id": cls.fr_country_id,
                "phone": "+33 4 78 32 32 32",
            }
        )

    def test_lookup(self):
        res = self.phco.get_record_from_phone_number("0478323232")
        self.assertIsInstance(res, tuple)
        self.assertEqual(res[0], "res.partner")
        self.assertEqual(res[1], self.partner.id)
        self.assertEqual(res[2], self.partner.with_context(callerid=True).display_name)
        res = self.phco.get_record_from_phone_number("0499889988")
        self.assertFalse(res)
