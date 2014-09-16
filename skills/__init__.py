import communication
import cowboy


class SkillBase(object):
    base_value = 0
    per_level_increase = 0
    bonus = 0

    @property
    def parent(self):
        return self.__class__.__bases__[0].__name__

    @staticmethod
    def skill_value(self, character_level, level_offset=0):
        """

        :param character_level:
        :type character_level:
        :param level_offset:
        :type level_offset:
        :return:
        :rtype:
        """
        return (
            self.base_value + (self.per_level * character_level - level_offset)
        )
