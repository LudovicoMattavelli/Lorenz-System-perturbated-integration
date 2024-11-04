import numpy as np
import random 

def lorenz_system(variables, system_parameters):
    """This method caculates the derivatives of variables at a single time 
    step.
    
    Parameters
    ----------
    variables : 1-dimensional NumPy array of length 3
        State of the system at the given time step.
    system_parameters: 1-dimensional list of length 3
        Parameters of the system. 
        
    Returns
    -------
    derivatives : 1-dimensional NumPy array of length 3
        Derivative of the state of the system at the given time step.
    """
    derivatives = np.empty(3)
    derivatives[0] = system_parameters[0]*(variables[1] - variables[0])
    derivatives[1] = (system_parameters[2]*variables[0] 
                     - variables[0]*variables[2] - variables[1])
    derivatives[2] = (variables[0]*variables[1] 
                     - system_parameters[1]*variables[2])
    return derivatives

def test_lorenz_known_solution():
    """This method tests the function lorenz_system with a predefined set of
    variables and checks the value of the known solution.
    """
    variables = np.array([2,3,6])
    system_parameters = np.array([10,8/3,28])
    solution = lorenz_system(variables, system_parameters)
    assert solution[0] == 10
    assert solution[1] == 41
    assert solution[2] == -10

def test_lorenz_variables_zeros():
    """This method tests the function lorenz_system with a set of variables 
    all with value zero and checks that the solution is zero for every 
    variable.
    """   
    variables = np.zeros(3)
    system_parameters = np.array([10,8/3,28])
    solution = lorenz_system(variables, system_parameters)
    assert solution[0] == 0
    assert solution[1] == 0
    assert solution[2] == 0
    
def test_lorenz_output_shape():
    """This method tests the function lorenz_system with a random set of  
    variables to check that, for any values of the elements of variables, the
    solution has the correct shape.
    """
    random.seed(42)
    variables = np.empty(3)
    for i in range(3):
        variables[i] = random.random()
    system_parameters = np.array([10.0, 8/3, 28.0])  
    result = lorenz_system(variables, system_parameters)   
    assert result.shape == (3,) 
