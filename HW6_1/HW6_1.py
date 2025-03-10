#region imports
from ResistorNetwork import ResistorNetwork, ResistorNetwork_2
#endregion

#region Function Definitions
def main():
    """
    This program solves for the unknown currents in the circuit of the homework assignment.
    """
    print("Network 1:")
    Net1 = ResistorNetwork("ResistorNetwork.txt")  # Fixed JES Missing Code
    Net1.AnalyzeCircuit()
    Net1.GetKirchoffVals()
    Net1.ReportResults()

    print("\nNetwork 2:")
    Net2 = ResistorNetwork_2("ResistorNetwork_2.txt")  # Fixed JES Missing Code
    Net2.AnalyzeCircuit()
    Net2.GetKirchoffVals()
    Net2.ReportResults()
#endregion

#region Main Execution
if __name__ == "__main__":
    main()
#endregion
