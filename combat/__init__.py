from combat import constants as CONST


class CombatObjectBase(object):
    locations = ()
    initiative = 0
    actions = None

    def __init__(self, **kwargs):
        location_list = kwargs.get('location_list')
        self.locations = []
        if location_list:
            for location in location_list:
                new_location = DamageLocation(
                    location_name=location['location'],
                    damage_capacity=location['damage'],
                    is_mdc=location.get('is_mdc', False)
                )
                self.locations.append(new_location)
        else:
            location_name = kwargs.get('location', CONST.BODY)
            damage_capacity = kwargs.get('damage', 0)
            is_mdc = kwargs.get('is_mdc', 'False')
            self.locations.append(
                DamageLocation(location_name, damage_capacity, is_mdc)
            )
        initiative = kwargs.get(CONST.INITIATIVE, 0)
        if initiative:
            self.initiative = initiative

        actions = kwargs.get(CONST.ACTIONS, 0)
        if actions:
            self.actions = actions

    def apply_damage_to_location(self, location_name=CONST.BODY, amount=0, is_mdc=False):
        """
        Helper function to apply damage to a combat object.
        Expects a damage location and amount, and if the damage is megadamage
        or not.

        :param location_name: The location being damaged. If not specified, it
            will apply damage to the main body.
        :type location_name: str
        :param amount: The amound of damage to apply.
        :type amount: int
        :param is_mdc: Flag for if the damage is megadamage or not. Defaults
            to False.
        :type is_mdc: bool
        :return: Returns a flag for if the damage applied destroyed the
            location object.
        :rtype: bool
        """
        location = self._find_location(location_name)
        if location:
            remaining = location.apply_damage(value=amount)
            return remaining > 0
        else:
            raise IndexError("The specified location was not found.")

        
    def _find_location(self, location_name):
        """
        Internal helper method to retrieve a specified location from the
        the location list.

        :param location: The name of the location being found.
        :type location: str
        :return: Returns the element from the locations list.
        :rtype: :class:`~combat.DamageLocation` or None
        """
        return next(
            location for location in self.locations
            if location.name == location_name
        )

    @property
    def is_inert(self):
        return self.actions == 0



class DamageLocation(object):
    name = ""
    current = 0
    maximum = 0
    is_mdc = False

    def __init__(self, location_name=CONST.BODY, damage_capacity=0,
                 is_mdc=False):
        """

        :param location_name:
        :type location_name:
        :param damage_capacity:
        :type damage_capacity:
        :param is_mdc:
        :type is_mdc:
        :return:
        :rtype:
        """
        self.name = location_name
        self.current = damage_capacity
        self.maximum = damage_capacity
        self.is_mdc = is_mdc


    def apply_damage(self, value):
        """
        Helper function that will apply a damage value to the location, then
        return the remaining value left.

        :param value: The amount of damage to inflict.
        :type value: int
        :return: Returns the current total, intended to be used for destruction
            checks.
        :rtype: int
        """
        self.current -= value
        return self.current

    def remove_damage(self, value):
        """

        :param value:
        :type value:
        :return:
        :rtype:
        """
        new_value = self.current + value
        self.current = new_value if new_value <= self.maximum else self.maximum
        return self.current

    @property
    def at_max(self):
        """

        :return:
        :rtype:
        """
        return self.current == self.maximum


class StatusEffect(object):
    # TODO: Expand and implement.
    pass