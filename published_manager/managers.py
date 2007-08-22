from django.db import models
from django.conf import settings

class PublishedManager(models.Manager):
    def get_query_set(self):
        return super(PublishedManager, self).get_query_set().filter(state=settings.STATE_PUBLISHED)
