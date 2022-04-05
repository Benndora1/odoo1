# -*- coding: utf-8 -*-

from odoo import models, fields


# class new_app(models.Model):
#     _name = 'new_app.new_app'
#     _description = 'new_app.new_app'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100





class IncidentReport(models.Model):
    _name = 'incident.report'

    name = fields.Text("Name and Role of the person completing this form:")
    signature = fields.Char("Signature of person completing this form:")
    date = fields.Datetime("Date:")
    date_time = fields.Datetime("Date and Time:")
    victim = fields.Char("Name/s of person/s involved in the incident and their clubs/associations:")
    description = fields.Text("Description od the incidence")
    witness = fields.Text("Witness(include contacts")
    reported_to = fields.Char("Inceident reported to")
    how = fields.Char("How(this form, in person,email,phone):")
    actions = fields.Text("Description of the action taken:")

    

