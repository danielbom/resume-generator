import re

from src.helpers import u, b, link, visibles, timespan


class ExperienceT:
    ID = "experience"

    def __init__(self, ctx):
        self.ctx = ctx

    def write(self, s):
        self.ctx.p(b(u(s['name'])), self.ctx.s_section_title)
        for i, item in enumerate(visibles(s['items'])):
            header = f"{item['company']}, {item['position']} ({timespan(item['date'])})"
            self.ctx.p(b(header), self.ctx.s_subsection_title)
            if item.get('tech'):
                self.ctx.p(": ".join([
                    item['tech']['label'],
                    ", ".join(re.split(r",\s*", item['tech']['items']))
                ]), self.ctx.s_tab1)
            if item.get('url', {}).get('href'):
                self.ctx.p(": ".join([
                    item['url']['label'],
                    link(item['url']['href'])
                ]), self.ctx.s_tab1)
            for a in item.get('activities', []):
                self.ctx.p("• " + a)
            for a in item.get('results', []):
                self.ctx.p("• " + a)

