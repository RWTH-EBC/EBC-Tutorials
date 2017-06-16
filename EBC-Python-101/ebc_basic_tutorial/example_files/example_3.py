import EBC_Tutorial.example_2 as exp2


class Building(exp2.Point):
    """
    Building class. Inheritance of class Point.
    """
    def __init__(self, x, y, th_energy_demand,
                 building_type='residential'):
        """
        Constructor of building object.

        Parameters
        ----------
        x : float
            x-coordinate in m
        y : float
            y-coordinate in m
        th_energy_demand : float
            thermal energy demand of building in kWh
        building_type : str, optional
            Building type (default: 'residential')
        """

        #  Initialize point object (with call to parent
        #  class Building)
        super(Building, self).__init__(x, y)

        #  Add attributes to building
        self.th_energy_demand = th_energy_demand
        self._building_type = building_type
        #  A single '_' defines a private variable. As a user
        #  you should not modify this variable, even if you are
        #  able to do so.


class Energysystem(exp2.Point):
    """
    Energysystem class. Inheritance of class Point
    """
    def __init__(self, x, y, nominal_th_power,
                 th_system_type='boiler'):
        """
        Constructor of energysystem object.

        Parameters
        ----------
        x : float
            x-coordinate in m
        y : float
            y-coordinate in m
        nominal_th_power : float
            Nominal thermal power in W
        th_system_type : str, optional
            Thermal energy system type (default: 'boiler')
        """

        #  Initialize point object (with call to parent
        #  class  Energysystem)
        super(Energysystem, self).__init__(x, y)

        #  Add attributes to energysystem
        self.nominal_th_power = nominal_th_power
        self._th_system_type = th_system_type
        #  Another private variable/attribute
