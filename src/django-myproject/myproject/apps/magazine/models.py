from django.db import models
from django.utils.translation import gettext_lazy as _


class NewsArticle(models.Model):
    created_at = models.DateTimeField(_("Created at"),
    auto_now_add=True)
    title = models.CharField(_("Title"), max_length=255)
    body = models.TextField(_("Body"))
    theme = models.CharField(_("Theme"), max_length=20)

    class Meta:
        verbose_name = _("New Article")
        verbose_name_plural = _("New Articles")

    def __str__(self):
        return self.title
