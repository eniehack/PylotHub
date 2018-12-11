from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _
from django.utils.html import mark_safe
from markdown import markdown
import uuid

GENRE = (
    ('00', _('None')),
    ('01', _('SF')),
    ('02', _('Fantasy')),
    ('03', _('Horror')),
    ('04', _('history')),
    ('05', _('love')),
    ('06', _('romance')),
    ('07', _('drama')),
)


class Plot(models.Model):
    plot_id = models.UUIDField(_('plot id'), primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    user_id = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,)
    title = models.CharField(_('title'), max_length=50, db_index=True)
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('updated at'), auto_now=True)
    genre = models.CharField(_('genre'), max_length=2, choices=GENRE, default='00')
    content = models.TextField(_('content'))

    def get_content_as_markdown(self):
        return mark_safe(markdown(self.content, safe_mode='escape'))