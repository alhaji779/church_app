# -*- coding: utf-8 -*-

from odoo import models, fields, api

class church_app(models.Model):
	_name = 'church_app.church_app'
	_rec_name = 'f_name'

	name = fields.Char('First Name')
	middle = fields.Char('Middle Name')
	last = fields.Char('Last Name')
	photo = fields.Binary('Photo', attachment=True)
	# image_medium = fields.Binary(
	# 	"Medium-sized photo", attachment=True,
	# 	help="Medium-sized photo of the employee. It is automatically "
	# 		 "resized as a 128x128px image, with aspect ratio preserved. "
	# 		 "Use this field in form views or some kanban views.")
	street = fields.Char('Address')
	email = fields.Char('Email Address')
	phone = fields.Char('Phone Number')
	w_phone = fields.Char('Other Phone Number')
	arm = fields.Selection([('mca','MCA'),('wg','WG'),('pypan','PYPAN'),('cgit','CGIT')], 'ARM')
	ordinance = fields.Selection([('elder','Elder'),('evangelist','Evangelist'),('clergy','Clergy'),('laity','Laity')], 'Ordinance')
	title = fields.Char('Title')
	marital = fields.Selection([('single','Single'),('married','Married'),('cohabitant', 'Legal Cohabitant'),('widower', 'Widower'),('divorced', 'Divorced')], 'Marital Status')
	gender = fields.Selection([('male','Male'),('female','Female')], 'Gender')
	occupation = fields.Char('Occcupation')
	gen_id = fields.Many2one('general.ass', 'Assembly')
	syn_id = fields.Many2one('general.synod', 'Synod')
	pres_id = fields.Many2one('general.pres', 'Presbytery')
	parish_id = fields.Many2one('general.parish', 'Parish')
	cong_id2 = fields.Many2one('general.congregate', 'Congregation')
	f_name = fields.Char('Full Name', compute='_compute_complete_name', store=True)



	@api.depends('title','name', 'middle', 'last')
	def _compute_complete_name(self):
		for department in self:
			if department.name:
				department.f_name = '%s %s %s %s' % (department.title,department.name,department.middle,department.last)
			else:
				department.f_name = department.name


	# @api.multi
 #    def set_full(self):
 #        self.f_name = self.title + self.name + se


class GeneralAss(models.Model):
	_name = 'general.ass'

	name = fields.Char('Name')
	synod = fields.One2many('general.synod', 'gen_id', 'Synod')


class GeneralSynod(models.Model):
	_name = 'general.synod'

	name = fields.Char('Name')
	gen_id = fields.Many2one('general.ass', 'Assembly')
	pres_b = fields.One2many('general.pres', 'syn_id', 'Presbytery')


class GeneralPres(models.Model):
	_name = 'general.pres'

	name = fields.Char('Name')
	gen_id = fields.Many2one('general.ass', 'Assembly')
	syn_id = fields.Many2one('general.synod', 'Synod')
	parish = fields.One2many('general.parish','pres_id', 'Parish')


class GeneralParish(models.Model):
	_name = 'general.parish'

	name = fields.Char('Name')
	gen_id = fields.Many2one('general.ass', 'Assembly')
	syn_id = fields.Many2one('general.synod', 'Synod')
	pres_id = fields.Many2one('general.pres', 'Presbytery')
	cong = fields.One2many('general.congregate','parish_id', 'Congregation')


class GeneralCongregate(models.Model):
	_name = 'general.congregate'

	name = fields.Char('Name')
	gen_id = fields.Many2one('general.ass', 'Assembly')
	syn_id = fields.Many2one('general.synod', 'Synod')
	pres_id = fields.Many2one('general.pres', 'Presbytery')
	parish_id = fields.Many2one('general.parish', 'Parish')
	member = fields.One2many('church_app.church_app','cong_id2', 'Member')



