import logging
 
class BaseOCC(object):
    #: The full name of the class
    name = ""
    #: Searchable list of tags for class searching
    tags = None
    #: The level of the class object
    level = 0
    #: OCC Skill list of tuples of skill, bonus
    ooc_skills = None
    #: OCC Related skill allowed list of tuples of skill_group, bonus
    occ_related_skills = None
    #: Secondary skill list of tuples of skill_group, bonus