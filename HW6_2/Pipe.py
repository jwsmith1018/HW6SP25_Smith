#region imports
import math
from Fluid import Fluid
#endregion

#region class definitions
class Pipe:
    #region constructor
    def __init__(self, start='A', end='B', L=100, D=200, r=0.00025, fluid=Fluid()):
        """
        Defines a pipe segment for flow analysis.
        :param start: Start node (str)
        :param end: End node (str)
        :param L: Length in meters (float)
        :param D: Diameter in meters (float)
        :param r: Roughness in meters (float)
        :param fluid: Fluid object representing the working fluid
        """
        self.start = start
        self.end = end
        self.length = L
        self.diameter = D
        self.roughness = r
        self.fluid = fluid
        self.flow_rate = None  # To be computed during analysis
    #endregion

    #region Methods
    def compute_reynolds_number(self, velocity):
        """
        Computes the Reynolds number for the given flow velocity.
        :param velocity: Fluid velocity in m/s (float)
        :return: Reynolds number (float)
        """
        return (self.fluid.density * velocity * self.diameter) / self.fluid.viscosity

    def compute_friction_factor(self, velocity):
        """
        Computes the Darcy-Weisbach friction factor based on Reynolds number.
        :param velocity: Fluid velocity in m/s (float)
        :return: Friction factor (float)
        """
        Re = self.compute_reynolds_number(velocity)
        if Re < 2000:
            return 64 / Re  # Laminar flow
        else:
            return 0.25 / (math.log10((self.roughness / (3.7 * self.diameter)) + (5.74 / (Re**0.9)))**2)  # Turbulent flow
    #endregion
#endregion
