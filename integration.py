import numpy as np
import lorenz as lorenz

#Parameters to define the probem
system_parameters = [10,8/3,28]
time_step = 0.005
end_time = 60
initial_conditions = np.array([9, 10, 18], dtype='float')
epsilon = np.array([0, 1E-07, 1E-05, 1E-03, 1E-01])

# Definition of the variables for the if conditions 
presence_of_perturbation = np.full(len(epsilon), True)
presence_of_perturbation[0] = False
first_step = True

# Definition of the variables for the sensibility study
total_steps = int(end_time/time_step)
X_storage = np.zeros([len(epsilon), total_steps])
variance_storage = np.zeros([len(epsilon), total_steps])
istant_variable = np.tile(initial_conditions, (len(epsilon), 1))
derivates = np.zeros(3)


for i in range (total_steps):   
    if first_step == True:
        # Compute the initial conditions
        istant_variable[:,i] += epsilon
        X_storage[:,i] = istant_variable[:,i]
        variance_storage[:,i] = np.power((X_storage[0,i] - X_storage[:,i]), 2)
        # Change the conditions on the firs_step to skip the code inside the if for the rest of the iteration
        first_step = False
        # Skip the rest of the loop for the first step
        continue    
    
    for j in range (len(epsilon)): 
        derivates = lorenz.lorenz_system(istant_variable[j,:], system_parameters)           
        istant_variable[j,:] = istant_variable[j,:] + derivates[:]*time_step
        X_storage[j,i] = istant_variable[j,0]
        variance_storage[j,i] = np.power((X_storage[0,i] - X_storage[j,i]), 2)