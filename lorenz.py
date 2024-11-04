import numpy as np

def lorenz_system(variables, system_parameters):
    """This method caculates the derivatives of the variables at a single
    time step.
    
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