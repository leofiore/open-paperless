from __future__ import unicode_literals

import logging

from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse
from django.utils.encoding import force_text, python_2_unicode_compatible
from django.utils.timezone import now
from django.utils.translation import ugettext_lazy as _

from documents.models import Document

from .events import event_document_register_in, event_document_register_out
from .exceptions import DocumentAlreadyRegisteredOut
#from .managers import DocumentRegisterOutManager, NewVersionBlockManager

logger = logging.getLogger(__name__)


@python_2_unicode_compatible
class DocumentRegister(models.Model):
    """
    Model to store the state and information of a document checkout
    """
    document = models.OneToOneField(
        Document, on_delete=models.CASCADE, verbose_name=_('Document')
    )
    register_datetime = models.DateTimeField(
        auto_now_add=True, verbose_name=_('Data di protocollazione')
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        verbose_name=_('User')
    )
    block_new_version = models.BooleanField(
        default=True,
        help_text=_(
            'Do not allow new version of this document to be uploaded.'
        ),
        verbose_name=_('Block new version upload')
    )

#    objects = DocumentRegisterOutManager()

    def __str__(self):
        return force_text(self.document)

    def clean(self):
        if self.expiration_datetime < now():
            raise ValidationError(
                _('Check out expiration date and time must be in the future.')
            )

    def delete(self, *args, **kwargs):
        # TODO: enclose in transaction
#        NewVersionBlock.objects.unblock(self.document)
        super(DocumentRegister, self).delete(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('register', args=(self.document.pk,))

    class Meta:
        verbose_name = _('Protocollazione documento')
        verbose_name_plural = _('Protocollazione documenti')


@python_2_unicode_compatible
class DocumentRegisterIn(models.Model):
    def __str__(self):
        return force_text(self.document)

    def save(self, *args, **kwargs):
        # TODO: enclose in transaction
        new_register = not self.pk
        if not new_register:
            raise DocumentAlreadyRegistered

        result = super(DocumentRegisterIn, self).save(*args, **kwargs)
        if new_register:
            event_document_register_in.commit(
                actor=self.user, target=self.document
            )
            #if self.block_new_version:
            #    NewVersionBlock.objects.block(self.document)

            logger.info(
                'Document "%s" checked out by user "%s"',
                self.document, self.user
            )

        return result

    class Meta:
        verbose_name = _('Protocollazione documento in entrata')
        verbose_name_plural = _('Protocollazione documenti in entrata')


@python_2_unicode_compatible
class DocumentRegisterOut(models.Model):
    def __str__(self):
        return force_text(self.document)

    def save(self, *args, **kwargs):
        # TODO: enclose in transaction
        new_register = not self.pk
        if not new_register:
            raise DocumentAlreadyRegistered

        result = super(DocumentRegisterOut, self).save(*args, **kwargs)
        if new_register:
            event_document_register_out.commit(
                actor=self.user, target=self.document
            )
            #if self.block_new_version:
            #    NewVersionBlock.objects.block(self.document)

            logger.info(
                'Document "%s" checked out by user "%s"',
                self.document, self.user
            )

        return result

    class Meta:
        verbose_name = _('Protocollazione documento in entrata')
        verbose_name_plural = _('Protocollazione documenti in entrata')
#class NewVersionBlock(models.Model):
#    document = models.ForeignKey(
#        Document, on_delete=models.CASCADE, verbose_name=_('Document')
#    )
#
#    objects = NewVersionBlockManager()
#
#    class Meta:
#        verbose_name = _('New version block')
#        verbose_name_plural = _('New version blocks')
