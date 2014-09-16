from skills.skill_groups import CommunicationSkill
from skills import SkillBase

class BarterSkill(CommunicationSkill, SkillBase):
    base_value = 30
    per_level_increase = 4


class CreativeWritingSkill(CommunicationSkill, SkillBase):
    pass


class CryptographySkill(CommunicationSkill, SkillBase):
    pass

