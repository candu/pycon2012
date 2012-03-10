from xhpy.pylib import *

from django.conf import settings

class :ui:css(:x:element):
    attribute string path
    def render(self):
        path = self.getAttribute('path')
        return <link href={settings.STATIC_URL + path} rel="stylesheet" type="text/css" />

class :ui:page(:x:element):
    attribute string title
    def render(self):
        title = self.getAttribute('title')
        head = \
        <head>
            <title>{title}</title>
            <ui:css path="base.css" />
        </head>
        container = <div id="container" />
        for child in self.getChildren():
            container.appendChild(child)
        return \
        <x:doctype>
            <html>
                {head}
                <body>
                    {container}
                </body>
            </html>
        </x:doctype>
