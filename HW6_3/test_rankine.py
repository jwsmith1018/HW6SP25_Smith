# region imports
from rankine import Rankine


# endregion

# region function definitions
def main():
    """
    Tests the Rankine cycle model by creating instances with different conditions
    and printing reports.
    """
    print("Testing Rankine Cycle with Saturated Steam...")
    cycle1 = Rankine(p_high=8000, p_low=8, x1=1.0)  # Saturated vapor at turbine inlet
    print(cycle1.report())

    print("\nTesting Rankine Cycle with Superheated Steam...")
    cycle2 = Rankine(p_high=8000, p_low=8, T1=600)  # Superheated steam at turbine inlet
    print(cycle2.report())


# endregion

# region function calls
if __name__ == "__main__":
    main()
# endregion
