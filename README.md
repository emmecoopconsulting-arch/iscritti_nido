# Partner Iscritti (Asilo Nido) — Odoo 18

Aggiunge nella scheda **Contatti (res.partner)** una tab **“Asilo Nido”** con l’elenco degli **iscritti** collegati al genitore (uno o più bambini).

## Funzionalità
- Nuovo modello: `pb.nido.iscritto`
- Collegamento 1→N dal genitore (`res.partner`) agli iscritti (`one2many`)
- Campi iscritto:
  - **Nome**, **Cognome**
  - **Data di nascita**
  - **Comune di nascita**
  - **Codice Fiscale** (check lunghezza 16)
  - **Protocollo iscrizione**
  - **File PDF dell'iscrizione**
- Tab dedicata in form partner con tree inline editabile + form

## Requisiti
- Odoo **18.0**
- Moduli base: `base`, `contacts`

## Installazione
1. Posiziona l’addon in una cartella custom (es. `/opt/odoo/custom_addons/partner_iscritti`).
2. Aggiungi la cartella a `addons_path` in `/etc/odoo/odoo.conf`, ad es.: