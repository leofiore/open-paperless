from __future__ import absolute_import, unicode_literals


from django.apps import apps
from django.db.models.signals import pre_save
from django.utils.translation import ugettext_lazy as _

from acls import ModelPermission
from common import MayanAppConfig

#from .handlers import check_new_version_creation
from .permissions import (
    permission_document_register_in, permission_document_register_in_override,
    permission_document_register_out, permission_document_register_out_detail_view
)


class RegisterApp(MayanAppConfig):
    has_tests = True
    name = 'register'
    verbose_name = _('Registro documenti')

    def ready(self):
        super(RegisterApp, self).ready()


        Document = apps.get_model(
            app_label='documents', model_name='Document'
        )
        DocumentVersion = apps.get_model(
            app_label='documents', model_name='DocumentVersion'
        )

        DocumentRegister = self.get_model('DocumentRegister')

        Document.add_to_class(
            'check_in',
            lambda document, user=None: DocumentRegister.objects.check_in_document(document, user)
        )
        Document.add_to_class(
            'checkout_info',
            lambda document: DocumentRegister.objects.document_register_out_info(
                document
            )
        )

        ModelPermission.register(
            model=Document, permissions=(
                permission_document_register_out,
                permission_document_register_in,
                permission_document_register_in_override,
                permission_document_register_out_detail_view
            )
        )


        #pre_save.connect(
        #    check_new_version_creation,
        #    dispatch_uid='check_new_version_creation',
        #    sender=DocumentVersion
        #)
