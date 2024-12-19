from reactpy import component, html
from reactpy.types import *


@component
def Header() -> VdomDict:
    return html.header(html.h1("Header"))



