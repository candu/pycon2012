from xhpy.pylib import *

from django.http import HttpResponse

from lightning.ui.list import :ui:list
from lightning.ui.page import :ui:page

def index(request):
    page = \
    <ui:page title="PyCon 2012 - XHPy Lightning Talk">
        <h1>Hello PyCon!</h1>
        <h2>This page was built using XHPy.</h2>
        <ui:list items={range(5)} />
    </ui:page>
    return HttpResponse(page)
