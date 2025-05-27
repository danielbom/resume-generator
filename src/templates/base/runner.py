from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.pagesizes import A4

from .basics import BasicsT
from .context import Context
from .education import EducationT
from .experience import ExperienceT
from .languages import LanguagesT
from .profiles import ProfilesT
from .projects import ProjectsT
from .skills import SkillsT
from .summary import SummaryT


class SectionsMap:
    def __init__(self):
        self.map = {}

    def add(self, writer):
        self.map[writer.ID] = writer

    def get(self, key):
        return self.map[key]

    def write(self, key, *args, **kargs):
        if key in self.map:
            self.map[key].write(*args, **kargs)
            return True
        else:
            return False


def create_section_map(ctx):
    smap = SectionsMap()
    smap.add(BasicsT(ctx))
    smap.add(ProfilesT(ctx))
    smap.add(ExperienceT(ctx))
    smap.add(EducationT(ctx))
    smap.add(ExperienceT(ctx))
    smap.add(LanguagesT(ctx))
    smap.add(ProjectsT(ctx))
    smap.add(SkillsT(ctx))
    smap.add(SummaryT(ctx))
    return smap



class RunnerT:
    def __init__(self, *args, **kargs):
        self.ctx = Context(*args, **kargs)
        self.smap = create_section_map(self.ctx)

    def run(self, data):
        self.smap.write('basics', data)
        self.smap.write('profiles', data['sections']['profiles'])
        del data['sections']['profiles']
        self.ctx.y(8)
        self.ctx.bar()

        for key in data['metadata']['layout']:
            s = data['sections'][key]
            if s.get('pagebreak') == 'before':
                self.ctx.page_break()
            self.smap.write(s['id'], s)
            if s.get('pagebreak') == 'after':
                self.ctx.page_break()

        doc = SimpleDocTemplate(
            self.ctx.output_path,
            pagesize=A4,
            topMargin=data['metadata']['page']['margin'][0],
            rightMargin=data['metadata']['page']['margin'][1],
            bottomMargin=data['metadata']['page']['margin'][2],
            leftMargin=data['metadata']['page']['margin'][3],
        )
        doc.build(self.ctx.story)

