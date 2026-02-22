{
    "name": "Odoo Bilgi Asistanı",
    "summary": "Odoo hakkında temel bilgileri veren basit RAG tabanlı sohbet asistanı",
    "version": "1.0",
    "author": "Rasim Okutan",
    "category": "Tools",
    "depends": ["base"],
    'data': [
    'security/ir.model.access.csv',
    'views/assistant_view.xml',
],
    "application": True,
    "installable": True,
}
