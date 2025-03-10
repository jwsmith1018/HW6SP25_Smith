#region class definitions
class Loop:
    #region constructor
    def __init__(self):
        """
        Initializes a loop as a list of node names.
        """
        #region attributes
        self.Nodes = []
        #endregion
    #endregion

    #region Methods
    def AddNode(self, node):
        """
        Adds a node to the loop.
        :param node: Node name (str)
        """
        self.Nodes.append(node)

    def __str__(self):
        """
        Returns a string representation of the loop.
        """
        return f"Loop: {' -> '.join(self.Nodes)}"
    #endregion
#endregion
