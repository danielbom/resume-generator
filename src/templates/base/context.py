from reportlab.platypus import Paragraph, Spacer, PageBreak, HRFlowable, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY


class Context:
    def __init__(self,
                 primary = 'black',
                 output_path = 'output.pdf'):
        self.primary = primary
        self.output_path = output_path
        self.styles = getSampleStyleSheet()

        self.story = []

        self.s_name = ParagraphStyle('Name', parent=self.styles['Heading1'], spaceBefore=0, spaceAfter=0)
        self.s_headline = ParagraphStyle("Headline", parent=self.styles['Heading2'], spaceBefore=0, spaceAfter=2, fontName='Helvetica')
        self.s_contact = ParagraphStyle("Contact", parent=self.styles['Normal'], spaceAfter=2)
        self.s_section_title = ParagraphStyle('SectionTitle', parent=self.styles['Heading3'], textColor=primary, fontName='Helvetica', spaceBefore=5, spaceAfter=5)
        self.s_subsection_title = ParagraphStyle('SubsectionTitle', parent=self.styles['Heading4'], fontName='Helvetica-Bold', spaceBefore=4, spaceAfter=0)
        self.s_content = ParagraphStyle('Content', parent=self.styles['Normal'], alignment=TA_JUSTIFY, firstLineIndent=8)
        self.s_small_content = ParagraphStyle('SmallContent', parent=self.s_content, fontSize=9, leading=10)
        self.s_tab1 = ParagraphStyle('Tabbed', parent=self.styles['Normal'], firstLineIndent=8)

    def p(self, *args, **kargs):
        self.story.append(Paragraph(*args, **kargs))

    def s(self, width, height):
        self.story.append(Spacer(width, height))

    def y(self, height):
        self.s(1, height)

    def bar(self):
        self.story.append(HRFlowable(width="100%", thickness=1, lineCap='round', color=self.primary or 'black', spaceBefore=1, spaceAfter=1))

    def page_break(self):
        self.story.append(PageBreak())

    @property
    def h1(self):
        return self.styles["Heading1"]

    @property
    def h2(self):
        return self.styles["Heading2"]

    @property
    def h3(self):
        return self.styles["Heading3"]

    @property
    def h4(self):
        return self.styles["Heading4"]


