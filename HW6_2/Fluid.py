#region class definitions
class Fluid:
    #region constructor
    def __init__(self, mu=0.00089, rho=1000):
        """
        Defines fluid properties for pipe flow analysis.
        :param mu: Dynamic viscosity in Pa·s (float)
        :param rho: Density in kg/m³ (float)
        """
        self.viscosity = mu
        self.density = rho
    #endregion

    #region Methods
    def get_reynolds_number(self, velocity, diameter):
        """
        Computes the Reynolds number for a given flow velocity and pipe diameter.
        :param velocity: Flow velocity in m/s (float)
        :param diameter: Pipe diameter in meters (float)
        :return: Reynolds number (float)
        """
        return (self.density * velocity * diameter) / self.viscosity

    def __str__(self):
        """
        Returns a string representation of the fluid properties.
        """
        return f"Fluid: {self.density} kg/m³, {self.viscosity} Pa·s"
    #endregion
#endregion
