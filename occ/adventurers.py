"""Adventurers and Scholar Occupational Character Classes"""

from occ import BaseOCC


class BodyFixer(BaseOCC):
    name = "Body Fixer"
    tags = ('medical',)
    level = 0

    def __init__(self, level=0):
        self.level = level



