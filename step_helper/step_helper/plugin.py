import logging
import os
import pathlib
import re
from urllib.parse import quote
import logging
from collections import defaultdict

from mkdocs.plugins import BasePlugin

LOG = logging.getLogger("mkdocs.plugins." + __name__)

class StepHelperPlugin(BasePlugin):
    def __init__(self):
        self.counter = 0

    def on_page_markdown(self, markdown, page, config, files, **kwargs):
        img_pattern = re.compile(r'stepi-(.*)')
        sm_img_pattern = re.compile(r"\.stepi-([a-z0-9]{8})(.*)")

        """
import re

text = ".stepi-7870312c .red-ol .green-ol"

pattern = r"\.stepi-([a-z0-9]{8})(.*)"
match = re.match(pattern, text)

if match:
    hash_value = match.group(1)
    classes = match.group(2).strip()
    output = f'![]({hash_value}.jpeg){{.sm{classes} data-gallery="step1-sm"}}'
    print(output)
        """

        self.counter = 0
        self.imgcounter = 0

        lines = []
        for line in markdown.splitlines():
            if '.Stepn' in line:
                self.counter += 1
                self.imgcounter = 0
                lines.append(line.replace('.Stepn', f'###**Step {str(self.counter)}**'))
            elif 'Stepn' in line:
                self.counter += 1
                self.imgcounter = 0
                lines.append(line.replace('Stepn', 'Step '+str(self.counter)))
            elif 'stepn' in line:
                lines.append(line.replace('stepn', 'step'+str(self.counter)))
            elif '.gcard' in line:
                lines.append(line.replace('.gcard', '</div>'))         
            elif 'gcard' in line:
                lines.append(line.replace('gcard', '<div class="grid cards" markdown>'))
            elif '.rcir.' in line:
                lines.append(line.replace('.rcir.', ':red_circle:'))
            elif '.ocir.' in line:
                lines.append(line.replace('.ocir.', ':orange_circle:'))
            elif '.gcir.' in line:
                lines.append(line.replace('.gcir.', ':green_circle:'))
            elif '.bcir.' in line:
                lines.append(line.replace('.bcir.', ':blue_circle:'))
            elif '.pcir.' in line:
                lines.append(line.replace('.pcir.', ':purple_circle:'))
            elif sm_img_pattern.match(line):
                self.imgcounter += 1
                match = sm_img_pattern.match(line)
                img_path, colors = match.group(1), match.group(2).strip()
                lines.append('![](%s.png){.sm %s data-gallery="step%d-sm"}' % (img_path, colors, self.counter))
            elif len(img_pattern.findall(line)) > 0:
                self.imgcounter += 1
                hidden = '.hidden ' if self.imgcounter > 1 else ''
                img_path = img_pattern.findall(line)[0]
                lines.append('![](%s.png){%sdata-gallery="step%d"}' % (img_path, hidden, self.counter))
            else:
                lines.append(line)

        return '\n'.join(lines)