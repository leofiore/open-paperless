from __future__ import absolute_import, unicode_literals

from django.utils.translation import ugettext_lazy as _

from permissions import PermissionNamespace

namespace = PermissionNamespace('registers', _('Registro documenti'))

permission_document_register_in = namespace.add_permission(
    name='register_in_document', label=_('Registra documenti in entrata')
)
permission_document_register_in_override = namespace.add_permission(
    name='register_in_document_override', label=_('Forza registro documenti in entrata')
)
permission_document_register_out = namespace.add_permission(
    name='register_out_document', label=_('Registra documenti in uscita')
)
permission_document_register_out_detail_view = namespace.add_permission(
    name='register_out_detail_view', label=_('Check out details view')
)
