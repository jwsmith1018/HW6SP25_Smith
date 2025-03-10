#region imports
from scipy.optimize import fsolve
import numpy as np
from Fluid import Fluid
from Pipe import Pipe
from Node import Node
#endregion

#region class definitions
class PipeNetwork:
    #region constructor
    def __init__(self, filename):
        """
        Initializes the pipe network from a configuration file.
        :param filename: Path to the pipe network file (str)
        """
        self.filename = filename
        self.pipes = []
        self.nodes = {}
        self.parse_file()
    #endregion

    #region Methods
    def parse_file(self):
        """
        Parses the pipe network configuration file and initializes components.
        """
        try:
            with open(self.filename, 'r') as file:
                for line in file:
                    parts = line.strip().split(',')
                    if len(parts) < 6:
                        continue
                    _, start, end, length, diameter, roughness = parts
                    pipe = Pipe(start.strip(), end.strip(), float(length), float(diameter), float(roughness))
                    self.pipes.append(pipe)
                    if start.strip() not in self.nodes:
                        self.nodes[start.strip()] = Node(start.strip())
                    if end.strip() not in self.nodes:
                        self.nodes[end.strip()] = Node(end.strip())
                    self.nodes[start.strip()].add_pipe(pipe)
                    self.nodes[end.strip()].add_pipe(pipe)
        except Exception as e:
            print(f"Error reading file {self.filename}: {e}")

    def solve_network(self):
        """
        Solves for the flow rates in each pipe segment using fsolve.
        """
        print("Solving for pipe flows...")
        initial_guess = np.ones(len(self.pipes)) * 0.01
        self.solution = fsolve(self.equations, initial_guess)
        for i, pipe in enumerate(self.pipes):
            pipe.flow_rate = self.solution[i]

    def equations(self, flows):
        """
        Constructs the system of equations for mass conservation and head loss.
        :param flows: Array of flow rates (m³/s)
        :return: Residuals of the system equations
        """
        eqs = []
        for node in self.nodes.values():
            eqs.append(node.mass_balance())
        return eqs

    def report_flows(self):
        """
        Prints the computed flow rates for each pipe segment.
        """
        print("Pipe Network Flow Results:")
        for pipe in self.pipes:
            print(f"Flow in segment {pipe.start}-{pipe.end}: {pipe.flow_rate:.4f} m³/s")
    #endregion
#endregion
