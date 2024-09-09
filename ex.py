from inventory.models import Brand
from pygments import highlight
from django.db import connection, reset_queries
from pygments.formatters import TerminalFormatter
from sqlparse import format

# pip install pygments sqlparse


Brand.objects.all()
Brand.objects.all().delete()
Brand.objects.create(brand_id = '1', name='nike')
x = Brand.objects.filter(brand_id = 1)

Brand.objects.all()
Brand.objects.all().query
