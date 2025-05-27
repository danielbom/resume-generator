from src.helpers import link


class ProfilesT:
    ID = "profiles"

    def __init__(self, ctx):
        self.ctx = ctx

    def write(self, s):
        for item in s['items']:
            self.ctx.p(": ".join([
                item['url']['label'],
                link(item['url']['href']),
            ]))
