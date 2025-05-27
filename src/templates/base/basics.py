from src.helpers import email, link, tel


class BasicsT:
    ID = "basics"

    def __init__(self, ctx):
        self.ctx = ctx

    def write(self, data):
        self.ctx.p(data['basics']['name'], self.ctx.s_name)
        self.ctx.p(data['basics']['headline'], self.ctx.s_headline)
        self.ctx.p(" - ".join([
            tel(data['basics']['phone']),
            email(data['basics']['email']),
            data['basics']['location']
        ]), self.ctx.s_contact)
        self.ctx.p(": ".join([
            data['basics']['url']['label'],
            link(data['basics']['url']['href']),
        ]))

