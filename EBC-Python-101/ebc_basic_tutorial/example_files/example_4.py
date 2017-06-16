import EBC_Tutorial.example_3 as exp3


def example_of_building_and_esys():
    #  Generate Building object
    testbuilding = exp3.Building(x=0, y=0, th_energy_demand=30000)
    #  building_type is automatically set
    #  to 'residential' (default)

    #  Generate energy system object
    testenersys = exp3.Energysystem(x=10, y=10, nominal_th_power=10000)
    #  th_system_type is automatically set
    #  to 'boiler' (default)

    #  Calculate distance between building
    #  and energysystem
    dist = testbuilding.calc_distance_to_other_point(testenersys)
    print('Distance between building '
          'and energysystem:', round(dist, 2))

if __name__ == '__main__':
    #  Execute run
    example_of_building_and_esys()
