from src.helpers import u, b


class SummaryT:
    ID = "summary"

    def __init__(self, ctx):
        self.ctx = ctx

    def write(self, s):
        self.ctx.p(u(b(s['name'])), self.ctx.s_section_title)
        for line in s['content']:
            self.ctx.p(line, self.ctx.s_content)

