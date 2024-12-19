from fastapi import FastAPI
from reactpy import component, html
from reactpy.backend.fastapi import configure
from reactpy.types import VdomDict

FastApp = FastAPI()


@component
def Header() -> VdomDict:
    return html.header(html.h1("Header"))


@component
def Main() -> VdomDict:
    return html.main(html.h1("Main"))


@component
def Footer() -> VdomDict:
    return html.footer(html.h1("Footer"))


@component
def WebApp():
    return html._(Header(), Main(), Footer())


configure(FastApp, WebApp)
