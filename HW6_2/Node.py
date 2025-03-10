# region class definitions
class Node:
    # region constructor
    def __init__(self, name):
        """
        Initializes a node in the pipe network.
        :param name: Name of the node (str)
        """
        self.name = name
        self.pipes = []

    # endregion

    # region Methods
    def add_pipe(self, pipe):
        """
        Adds a pipe connected to this node.
        :param pipe: Pipe object
        """
        self.pipes.append(pipe)

    def mass_balance(self):
        """
        Computes the mass balance at the node.
        Ensures that the sum of incoming and outgoing flows is zero.
        :return: Mass balance residual (float)
        """
        net_flow = sum(pipe.flow_rate for pipe in self.pipes)
        return net_flow  # Should equal zero for mass conservation

    def __str__(self):
        """
        Returns a string representation of the node.
        """
        return f"Node {self.name}: Connected to {len(self.pipes)} pipes"
    # endregion
# endregion
