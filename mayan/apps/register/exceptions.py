from __future__ import unicode_literals

from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext


class DocumentRegisterError(Exception):
    """
    Base checkout exception
    """
    pass


class DocumentNotRegisteredOut(DocumentRegisterError):
    """
    Raised when trying to checkin a document that is not checkedout
    """
    pass


@python_2_unicode_compatible
class DocumentAlreadyRegisteredOut(DocumentRegisterError):
    """
    Raised when trying to checkout an already checkedout document
    """
    def __str__(self):
        return ugettext('Document already registered out.')


class NewDocumentVersionNotAllowed(DocumentRegisterError):
    """
    Uploading new versions for this document is not allowed
    """
    pass
