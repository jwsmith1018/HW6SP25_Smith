#region class definitions
class Resistor:
    #region constructor
    def __init__(self, R=1.0, i=0.0, name='ab'):
        """
        Defines a resistor with resistance, current, and name.
        :param R: Resistance in Ohms (float)
        :param i: Current in Amps (float)
        :param name: Name of the resistor (str)
        """
        self.Resistance = R
        self.Current = i
        self.Name = name
    #endregion

    #region Methods
    def GetVoltageDrop(self):
        """
        Calculates and returns the voltage drop across the resistor using Ohm's Law.
        :return: Voltage drop (float)
        """
        return self.Resistance * self.Current  # Fixed JES Missing Code
    
    def __str__(self):
        """
        Returns a string representation of the resistor.
        """
        return f"Resistor {self.Name}: {self.Resistance} Ohms, {self.Current} Amps"
    #endregion
#endregion
