from latex import LatexCommand, LatexDoc, LatexLengthOption
import yaml

class Config:
    def __init__(self, config_file):
        with open(config_file, 'r') as file:
            try:
                self.config = yaml.safe_load(file)
            except yaml.YAMLError as err:
                print(err)

        self.floats = []
        if 'floats' in self.config:
            for floatOpt in self.config['floats']:
                for opt, val in floatOpt.items():
                    if len(val) > 0 and val != 'default':
                        self.floats += [LatexLengthOption(opt, val)]

        self.compact_items = False
        self.compact_enums = False
        if 'lists' in self.config:
            list_config = self.config['lists']
            if 'compact-items' in list_config:
                self.compact_items = list_config['compact-items']
            if 'compact-enums' in list_config:
                self.compact_enums = list_config['compact-enums']

        self.headings = []        
        if 'headings' in self.config:
            heads_config = self.config['headings']
            for head in heads_config:
                head_config = heads_config[head]
                left = head_config['left'] or "0pt"
                above = head_config['above'] or "0pt"
                below = head_config['below'] or "0pt"
                self.headings += [LatexCommand('titlespacing', None, 
                                               [f'\\{head}', left, above, below])]

        self.paragraphs = []
        if 'paragraphs' in self.config:
            for opt, val in self.config['paragraphs'].items():
                if len(val) > 0 and val != 'default':
                    self.paragraphs += [LatexLengthOption(opt, val)]
 
        self.equations = []
        if 'equations' in self.config:
            for opt, val in self.config['equations'].items():
                if len(val) > 0 and val != 'default':
                    self.equations += [LatexLengthOption(opt, val)]

        spread_factor = 1.0
        if 'line-spread' in self.config:
            spread_factor = self.config['line-spread']
        self.line_spread = [LatexCommand('linespread', [], str(spread_factor))]
        
    def apply_to(self, doc):
        if self.compact_items or self.compact_enums:
            doc.add_package('paralist')
        if self.compact_items:
            doc.replace_in_body('\\begin{itemize}', '\\begin{compactitem}')
            doc.replace_in_body('\\end{itemize}', '\\end{compactitem}')
        if self.compact_items:
            doc.replace_in_body('\\begin{enumerate}', '\\begin{compactenum}')
            doc.replace_in_body('\\end{enumerate}', '\\end{compactenum}')

        if len(self.headings) > 0:
            doc.add_package('titlesec', 'compact')
        header_opts = self.floats + self.equations + self.paragraphs + self.headings + self.line_spread
        for opt in header_opts:
            doc.add_header_opt(opt)
        pass