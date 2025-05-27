from src.helpers import u, b, visibles


class LanguagesT:
    ID = "languages"

    def __init__(self, ctx):
        self.ctx = ctx

    def write(self, s):
        self.ctx.p(b(u(s['name'])), self.ctx.s_section_title)
        for item in visibles(s['items']):
            self.ctx.p(f"• {item['name']} ({item['level']})")
        

