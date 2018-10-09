from __future__ import absolute_import, unicode_literals

from django.utils.translation import ugettext_lazy as _

from events.classes import Event

event_document_auto_register_in = Event(
    name='checkouts_document_auto_register_in',
    label=_('Documento in entrata registrato automaticamente')
)
event_document_register_in = Event(
    name='checkouts_document_register_in', label=_('Document in entrata registrato')
)
event_document_register_out = Event(
    name='checkouts_document_register_out', label=_('Document in uscita registrato')
)
event_document_forceful_register_in = Event(
    name='checkouts_document_forceful_register_in',
    label=_('Document in entrata registrato forzatamente')
)
