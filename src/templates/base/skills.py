from src.helpers import u, b


class SkillsT:
    ID = "skills"

    def __init__(self, ctx):
        self.ctx = ctx

    def write(self, s):
        self.ctx.p(b(u(s['name'])), self.ctx.s_section_title)
        self.ctx.p(" - ".join(s['items']))

