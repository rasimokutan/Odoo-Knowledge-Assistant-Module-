from odoo import models, fields, api
from . import rag_engine


class OdooKnowledgeAssistant(models.Model):
    _name = "odoo.knowledge.assistant"
    _description = "Odoo Bilgi Asistanı"

    name = fields.Char(string="Başlık", default="Yeni Soru", required=True)
    question = fields.Text(string="Soru")
    answer = fields.Text(string="Cevap", readonly=True)

    def action_ask(self):
        """Form üzerindeki 'Sor' butonuna basıldığında çalışır."""
        for rec in self:
            if not rec.question:
                rec.answer = "Lütfen önce bir soru yazınız."
            else:
                reply = rag_engine.answer_question(rec.question)
                rec.answer = reply
