from skills import communication

class SkillGroup(object):
    group_description = ''
    skill_list = ()


class CommunicationSkill(SkillGroup):
    group_description = (
        "Skills associated with communication and communication equipment."
    )
    skill_list = (communication.BarterSkill, communication.CreativeWritingSkill)

class CowboySkill(SkillGroup):
    pass


class DomesticSkill(SkillGroup):
    pass


class ElectricalSkill(SkillGroup):
    pass


class EspionageSkill(SkillGroup):
    pass


class HorsemanshipSkill(SkillGroup):
    pass


class MechanicalSkill(SkillGroup):
    pass


class MedicalSkill(SkillGroup):
    pass


class MilitarySkill(SkillGroup):
    pass


class PhysicalSkill(SkillGroup):
    pass


class PilotSkill(SkillGroup):
    pass


class PilotRelatedSkill(SkillGroup):
    pass


class RogueSkill(SkillGroup):
    pass


class ScienceSkill(SkillGroup):
    pass


class TechnicalSkill(SkillGroup):
    pass


class WildernessSkill(SkillGroup):
    pass


class WeaponProficiencies(object):
    pass


class AncientWeapons(WeaponProficiencies):
    pass


class ModernWeapons(WeaponProficiencies):
    pass
