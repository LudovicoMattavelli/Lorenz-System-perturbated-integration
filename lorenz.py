import numpy as np

def lorenz_system(variables, system_parameters):
    """This method caculates the derivatives of the variables at a single
    time step.
    
    Parameters
    ----------
    variables : state of the system at the given time step.
    system_parameters: parameters of the system. 
        
    Returns
    -------
    derivatives : derivative of the state of the system at the given time step.
    """
    derivatives = np.empty(3)
    derivatives[0] = system_parameters[0]*(variables[1] - variables[0])
    derivatives[1] = (system_parameters[2]*variables[0] 
                     - variables[0]*variables[2] - variables[1])
    derivatives[2] = (variables[0]*variables[1] 
                     - system_parameters[1]*variables[2])
    return derivatives