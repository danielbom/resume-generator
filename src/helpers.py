import re


def center(value: str):
    return f"<para align='center'>{value}</para>"


def u(value: str):
    return f"<u>{value}</u>"


def b(value: str):
    return f"<b>{value}</b>"


def email(value: str):
    return f'<a href="mailto:{value}">{value}</a>'


def link(href: str, label: str | None = None):
    return f'<a href="{href}">{label or href}</a>'


def tel(value: str):
    href = re.sub(r"[^\d\+]", "", value)
    return f'<a href="tel:{href}">{value}</a>'


def visibles(xs: list[dict]):
    return [x for x in xs if x.get('visible')]


def timespan(p: dict):
    return ' - '.join([p['from'], p['to']])


