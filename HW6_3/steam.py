# region imports
import numpy as np
from scipy.interpolate import griddata


# endregion

# region class definitions
class Steam:
    """
    The Steam class retrieves thermodynamic properties of steam using interpolation.
    """

    # region constructor
    def __init__(self, pressure, T=None, x=None, s=None):
        """
        Initializes steam state with given properties.
        :param pressure: Pressure in kPa (float)
        :param T: Temperature in °C (float, optional)
        :param x: Quality (0-1) if in mixed region (float, optional)
        :param s: Entropy in kJ/(kg·K) (float, optional)
        """
        self.pressure = pressure
        self.T = T
        self.x = x
        self.s = s
        self.properties = self.interpolate_properties()

    # endregion

    # region Methods
    def interpolate_properties(self):
        """
        Uses griddata to interpolate properties based on inputs from steam tables.
        """
        # Example steam table data (replace with actual data)
        pressures = np.array([100, 500, 1000, 5000, 8000])
        temperatures = np.array([150, 250, 300, 450, 550])
        enthalpies = np.array([2500, 2700, 2800, 3100, 3300])
        entropies = np.array([6.5, 7.0, 7.2, 7.8, 8.2])

        if self.x is not None:
            h = 2000 + self.x * 1500  # Example linear interpolation for quality
            s = 5.5 + self.x * 2.0  # Example linear interpolation for entropy
        elif self.T is not None:
            h = griddata(temperatures, enthalpies, self.T, method='linear')
            s = griddata(temperatures, entropies, self.T, method='linear')
        else:
            h = griddata(pressures, enthalpies, self.pressure, method='linear')
            s = griddata(pressures, entropies, self.pressure, method='linear')

        return {'h': h, 's': s}

    def get_enthalpy(self):
        """
        Retrieves the enthalpy (h) from interpolated properties.
        :return: Enthalpy in kJ/kg (float)
        """
        return self.properties['h']

    def get_entropy(self):
        """
        Retrieves the entropy (s) from interpolated properties.
        :return: Entropy in kJ/(kg·K) (float)
        """
        return self.properties['s']

    def __str__(self):
        """
        Returns a formatted string of the steam properties.
        """
        return f"Steam at {self.pressure} kPa: h={self.get_enthalpy()} kJ/kg, s={self.get_entropy()} kJ/kg·K"
    # endregion
# endregion
