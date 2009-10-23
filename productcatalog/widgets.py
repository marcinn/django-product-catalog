"""
@author: Marcin Nowak
@license: BSD
"""

from django_widgets import Widget
import models

class ProductsInGroup(ProductList):
    def get_query_set(self, value, options):
        return models.Product.objects.from_group(value).published()
