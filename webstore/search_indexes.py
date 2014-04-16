import datetime
from haystack import indexes
from django.utils import timezone
from webstore.models import StoreItem


class StoreIndex(indexes.SearchIndex, indexes.Indexable):
    text  = indexes.CharField(document=True, use_template=True)
    description = indexes.CharField(model_attr='description')
    itemName = indexes.CharField(model_attr='itemName')
    categoryName = indexes.CharField(model_attr='category')
    content_auto = indexes.EdgeNgramField(model_attr='itemName')     

    def get_model(self):
        return StoreItem

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()
