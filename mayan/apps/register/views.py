from __future__ import absolute_import, unicode_literals

from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from documents.models import Document
from documents.views import DocumentListView

from acls.models import AccessControlList
from common.generics import (
    ConfirmView, SingleObjectCreateView, SingleObjectDetailView
)
from common.utils import encapsulate

from .models import DocumentRegisterOut
from .permissions import (
    permission_document_register_in,
    permission_document_register_out
)



class RegisterListView(DocumentListView):
    def get_document_queryset(self):
        return DocumentRegister.objects.checked_out_documents()

    def get_extra_context(self):
        context = super(RegisterListView, self).get_extra_context()
        context.update(
            {
                'title': _('Documents checked out'),
                'extra_columns': (
                    {
                        'name': _('User'),
                        'attribute': encapsulate(
                            lambda document: document.checkout_info().user.get_full_name() or document.checkout_info().user
                        )
                    },
                    {
                        'name': _('Checkout time and date'),
                        'attribute': encapsulate(
                            lambda document: document.checkout_info().checkout_datetime
                        )
                    },
                ),
            }
        )
        return context


