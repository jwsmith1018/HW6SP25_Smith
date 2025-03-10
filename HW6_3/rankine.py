# region imports
from steam import Steam


# endregion

# region class definitions
class Rankine:
    """
    The Rankine class models a Rankine power cycle, computing thermodynamic state properties
    and cycle efficiency.
    """

    # region constructor
    def __init__(self, p_high, p_low, x1=None, T1=None):
        """
        Initializes the Rankine cycle with given high and low pressures.
        :param p_high: High pressure in kPa (float)
        :param p_low: Low pressure in kPa (float)
        :param x1: Steam quality at turbine inlet (float, optional)
        :param T1: Superheated steam temperature at turbine inlet (float, optional)
        """
        self.p_high = p_high
        self.p_low = p_low
        self.x1 = x1
        self.T1 = T1
        self.states = {}
        self.efficiency = None
        self.calculate_states()

    # endregion

    # region Methods
    def calculate_states(self):
        """
        Computes thermodynamic states and cycle efficiency.
        """
        if self.T1 is None:
            self.states['1'] = Steam(self.p_high, x=1.0)  # Saturated vapor
        else:
            self.states['1'] = Steam(self.p_high, T=self.T1)  # Superheated steam

        self.states['2'] = Steam(self.p_low, s=self.states['1'].get_entropy())  # Isentropic expansion
        self.states['3'] = Steam(self.p_low, x=0.0)  # Condensed liquid
        self.states['4'] = Steam(self.p_high, s=self.states['3'].get_entropy())  # Isentropic pump process

        work_turbine = self.states['1'].get_enthalpy() - self.states['2'].get_enthalpy()
        work_pump = self.states['4'].get_enthalpy() - self.states['3'].get_enthalpy()
        heat_added = self.states['1'].get_enthalpy() - self.states['4'].get_enthalpy()

        self.efficiency = (work_turbine - work_pump) / heat_added

    def report(self):
        """
        Generates a summary report of the Rankine cycle analysis.
        """
        report = f"Rankine Cycle Report:\n"
        report += f"High Pressure: {self.p_high} kPa\n"
        report += f"Low Pressure: {self.p_low} kPa\n"
        report += f"Cycle Efficiency: {self.efficiency * 100:.2f}%\n"
        for state, steam in self.states.items():
            report += f"State {state}: {steam}\n"
        return report
    # endregion
# endregion
