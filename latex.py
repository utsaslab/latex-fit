
class LatexLengthOption:
    def __init__(self, option, value):
        self.option = option
        self.value = value

    def __str__(self):
        return f'\\setlength{{\\{self.option}}}{{{self.value}}}\n'

class LatexCommand:
    def __init__(self, command, options=[], args=[]):
        self.command = command

        if isinstance(options, str):
            self.options = [options]
        else:
            self.options = options

        if isinstance(args, str):
            self.args = [args]
        else:
            self.args = args

    def __str__(self):
        s = f'\\{self.command}'
        if self.options is not None:
            for opt in self.options:
                s += f'[{opt}]'
        if self.args is not None:
            for arg in self.args:
                s += f'{{{arg}}}'
        return s + '\n'

class LatexDoc:
    def __init__(self, file):
        self.file = file
        # Comments above \documentclass
        self.preamble = []
        # \documentclass and commands below it
        self.header = []
        # Starts at \begin{document}, ends at \end{document}
        self.document = []
        # Anything after \end{document}
        self.footer = []
        # Any packages we want to add to the document
        self.extra_packages = []
        # Commands we add to the header of the document
        self.header_commands = []
        # Packages being used in the document
        self.packages = []
        self.read_doc()
        self.read_packages()

    def read_doc(self):
        curr_list = self.preamble
        commented_lines = []
        for line in self.file:
            # If a comment or empty line, we group them together (in
            # case this surrounds a document marker)
            if line.strip().startswith('%') or len(line.strip()) == 0:
                commented_lines += [line]
                continue

            # Find the commands which split the document into its main parts
            elif '\\documentclass' in line:
                self.preamble += commented_lines
                commented_lines = []
                curr_list = self.header
            elif '\\begin{document}' in line:
                curr_list = self.document
            elif '\\end{document}' in line:
                curr_list += [line]
                curr_list = self.footer
                continue
            if len(commented_lines) > 0:
                curr_list += commented_lines
                commented_lines = []
            curr_list += [line]
    
    def read_packages(self):
        for line in self.header:
            if '\\usepackage' in line:
                # line is something like \usepackage{pkgname}...
                open_brack = line.find('{')
                close_brack = line.find('}')
                self.packages += [line[open_brack+1:close_brack]]

    def output_to(self, out):
        full_doc = ['% ~~~~~ PREAMBLE ~~~~~\n']
        full_doc += self.preamble
        full_doc += ['% ~~~~~ HEADER ~~~~~\n']
        full_doc += self.header
        full_doc += ['% ~~~~~ ADDED PACKAGES ~~~~~\n']
        full_doc += self.extra_packages 
        full_doc += ['% ~~~~~ ADDED COMMANDS ~~~~~\n']
        full_doc += self.header_commands
        full_doc += ['% ~~~~~ DOCUMENT ~~~~~\n']
        full_doc += self.document
        full_doc += ['% ~~~~~ FOOTER ~~~~~\n']
        full_doc += self.footer
        for line in full_doc:
            out.write(str(line))
    
    def add_package(self, package, packageOpts=[]):
        if not package in self.packages:
            self.extra_packages += [LatexCommand('usepackage', packageOpts, package)]
    
    def add_header_opt(self, opt):
        self.header_commands += [opt]
    
    def add_body_command(self, target_line, before_command, after_command):
        new_doc = []
        for line in self.document:
            if target_line in line:
                if before_command:
                    new_doc += [before_command]
                new_doc += [line]
                if after_command:
                    new_doc += [after_command]
            else:
                new_doc += [line]
        self.document = new_doc

    def replace_in_body(self, target, replacement):
        new_doc = []
        for line in self.document:
            new_doc += [line.replace(target, replacement)]
        self.document = new_doc

