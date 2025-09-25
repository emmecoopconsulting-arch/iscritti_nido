from odoo import models, fields

class PbNidoIscritto(models.Model):
    _name = "pb.nido.iscritto"
    _description = "Iscritto Asilo Nido"
    _order = "cognome, nome, id"

    parent_id = fields.Many2one(
        'res.partner',
        string="Genitore",
        required=True,
        ondelete='cascade',
        index=True,
        help="Partner genitore a cui è associato l'iscritto."
    )
    nome = fields.Char("Nome", required=True)
    cognome = fields.Char("Cognome", required=True)
    data_nascita = fields.Date("Data di nascita")  # niente required=True
    comune_nascita = fields.Char("Comune di nascita")
    codice_fiscale = fields.Char("Codice Fiscale", size=16, help="16 caratteri")
    protocollo_iscrizione = fields.Char("Protocollo iscrizione")
    iscrizione_state = fields.Selection(
        [
            ("pre_iscrizione", "Pre-iscrizione"),
            ("iscritto", "Iscritto"),
            ("ritirato", "Ritirato"),
        ],
        string="Stato iscrizione",
        default="pre_iscrizione",
        help="Stato della domanda di iscrizione dell'iscritto.",
    )
    iscrizione_pdf = fields.Binary("Iscrizione (PDF)", attachment=True)
    iscrizione_filename = fields.Char("Nome file")

    _sql_constraints = [
        ('cf_len_16',
         "CHECK (codice_fiscale IS NULL OR length(codice_fiscale)=16)",
         "Il Codice Fiscale deve avere 16 caratteri."),
    ]

class ResPartner(models.Model):
    _inherit = 'res.partner'
    nido_iscritto_ids = fields.One2many(
        'pb.nido.iscritto', 'parent_id',
        string="Iscritti"
    )