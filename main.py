
from fastapi import FastAPI
from reactpy import component, html
from reactpy.backend.fastapi import configure
from reactpy.types import VdomDict
app = FastAPI()

@component
def Header() -> VdomDict:
    return html.header(
        html.h1("HEADer")
    )
    
@component
def Main() -> VdomDict:
    return html.main(Header())



configure(app, Main)