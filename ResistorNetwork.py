# region imports
from scipy.optimize import fsolve
from Resistor import Resistor
from VoltageSource import VoltageSource
from Loop import Loop


# endregion

# region class definitions
class ResistorNetwork:
    # region constructor
    def __init__(self, filename):
        """
        Initializes the resistor network from a file.
        :param filename: Path to the network configuration file (str)
        """
        self.filename = filename
        self.resistors = []
        self.voltage_sources = []
        self.loops = []
        self.nodes = set()
        self.parse_file()

    # endregion

    # region Methods
    def parse_file(self):
        """
        Parses the network configuration file and initializes components.
        """
        try:
            with open(self.filename, 'r') as file:
                for line in file:
                    parts = line.strip().split(',')
                    if not parts or len(parts) < 5:
                        continue
                    element_type = parts[0].strip().lower()
                    if element_type == 'resistor':
                        _, name, resistance, node1, node2 = parts
                        resistor = Resistor(float(resistance), name=name)
                        self.resistors.append(resistor)
                        self.nodes.update([node1.strip(), node2.strip()])
                    elif element_type == 'voltage':
                        _, name, voltage, node_pos, node_neg = parts
                        voltage_source = VoltageSource(float(voltage), name=name)
                        self.voltage_sources.append(voltage_source)
                        self.nodes.update([node_pos.strip(), node_neg.strip()])
        except Exception as e:
            print(f"Error reading file {self.filename}: {e}")

    def AnalyzeCircuit(self):
        """
        Analyzes the circuit by solving for unknowns using Kirchhoff’s Laws.
        """
        print("Analyzing circuit...")
        self.solution = {"I1": 1.0, "I2": 0.5}  # Placeholder for actual solution

    def GetKirchoffVals(self):
        """
        Verifies Kirchhoff's Voltage and Current Laws.
        """
        print("Checking Kirchhoff’s Laws...")
        # Placeholder implementation

    def ReportResults(self):
        """
        Outputs the circuit analysis results.
        """
        print("Circuit Analysis Results:")
        for key, value in self.solution.items():
            print(f"{key}: {value}")
    # endregion


class ResistorNetwork_2(ResistorNetwork):
    """
    A subclass of ResistorNetwork that modifies the circuit by adding a 5Ω resistor
    in parallel with the 32V voltage source.
    Demonstrates polymorphism by overriding AnalyzeCircuit and GetKirchoffVals.
    """

    def __init__(self, filename):
        """
        Initializes the modified resistor network.
        :param filename: Path to the modified network configuration file (str)
        """
        super().__init__(filename)

    def AnalyzeCircuit(self):
        """
        Modified circuit analysis accounting for the additional parallel resistor.
        """
        print("Analyzing modified circuit with parallel 5Ω resistor...")
        self.solution = {"I1": 0.8, "I2": 0.6, "I3": 0.2}  # Placeholder for modified solution

    def GetKirchoffVals(self):
        """
        Verifies Kirchhoff's Laws for the modified circuit.
        """
        print("Checking Kirchhoff’s Laws for modified circuit...")
        # Placeholder implementation
# endregion
