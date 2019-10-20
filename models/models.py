# -*- coding: utf-8 -*-

from openerp import models, fields, api


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Record patient'
    _inherit = ['mail.thread', ]
    _rec_name = 'patient_name'

    patient_name = fields.Char(string="Name", required=True, )
    patient_age = fields.Integer(string="Age", required=False, )
    note = fields.Text(string="Notes", required=False, )
    image = fields.Binary(string="Image", )
    name_seq = fields.Char(string="Order reference", required=True, copy=False, index=True, default='New')
    gender = fields.Selection(string="Gender", selection=[('male', 'Male'), ('fe_male', 'Female'), ], default='male' )
    age_group = fields.Selection(string="Age Group", selection=[('major', 'Major'), ('minor', 'Minor'), ], compute='set_age_group', )

    @api.depends('patient_age')
    def set_age_group(self):
        if self.patient_age:
            if self.patient_age < 18:
                self.age_group = 'minor'
            else:
                self.age_group = 'major'


    @api.model
    def create(self, values):
        if values.get('name_seq', 'New') == 'New':
            values['name_seq'] = self.env['ir.sequence'].next_by_code('hospital.patient') or 'New'
        return super(HospitalPatient, self).create(values)