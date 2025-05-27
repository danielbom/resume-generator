from src.helpers import u, b, visibles, timespan, link


class EducationT:
    ID = "education"

    def __init__(self, ctx):
        self.ctx = ctx

    def write(self, s):
        self.ctx.p(b(u(s['name'])), self.ctx.s_section_title)
        for item in visibles(s['items']):
            self.ctx.p(item['area'], self.ctx.s_subsection_title)
            self.ctx.p(f"{item['institution']} ({timespan(item['date'])})", self.ctx.s_tab1)
            if item.get('url', {}).get('href'):
                self.ctx.p(": ".join([
                    item['url']['label'],
                    link(item['url']['href'])
                ]), self.ctx.s_tab1)
            if item["summary"]:
                self.ctx.p(item['summary'], self.ctx.s_small_content)
