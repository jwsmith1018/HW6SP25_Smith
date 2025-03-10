#region class definitions
class VoltageSource:
    #region constructor
    def __init__(self, V=12.0, name='V1'):
        """
        Defines a voltage source with a specified voltage and name.
        :param V: Voltage in Volts (float)
        :param name: Name of the voltage source (str)
        """
        self.Voltage = V
        self.Name = name
    #endregion

    #region Methods
    def __str__(self):
        """
        Returns a string representation of the voltage source.
        """
        return f"Voltage Source {self.Name}: {self.Voltage} V"
    #endregion
#endregion
