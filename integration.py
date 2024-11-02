import numpy as np
import lorenz as lorenz
import random
import plot

# Open the file with the values of the parameters to define the problem
with open('parameters.txt', 'r') as file:
    file_content = file.read()
# Execute the content of the file
exec(file_content)

# Definition of the variables for the if conditions 
presence_of_perturbation = np.full(len(epsilon), True)
presence_of_perturbation[0] = False
first_step = True

# Definition of the variables for the sensibility study
total_steps = int(end_time/time_step)
X_storage = np.zeros([len(epsilon), total_steps])
variance_storage = np.zeros([len(epsilon), total_steps])
istant_variable = np.tile(initial_conditions, (len(epsilon), 1))
derivatives = np.zeros(3)
# Definition of the variables for the ensemble study
total_steps_ensemble = int(end_ensemble_time/time_step)
random.seed(42) 
epsilon_ensemble = [random.uniform(distribution_inf, distribution_sup) for i in range(N_ensemble)]
X_ensemble_storage = np.zeros([N_ensemble, total_steps_ensemble])
variance_ensemble_storage = np.zeros([N_ensemble, total_steps_ensemble])
X_ensemble_storage_mean = np.zeros(total_steps_ensemble)
istant_ensemble_variable = np.tile(initial_conditions, (len(epsilon_ensemble), 1))

# Definition of the variables for the mean square error (mse) analysis
average_ensemble = np.zeros(total_steps_ensemble)
average_mse_ensemble = np.zeros(total_steps_ensemble)
mse_of_the_average_ensemble = np.zeros(total_steps_ensemble)

for i in range (total_steps):   
    if first_step == True:
        # Compute the initial conditions
        istant_variable[:,i] += epsilon
        X_storage[:,i] = istant_variable[:,i]
        variance_storage[:,i] = np.power((X_storage[0,i] - X_storage[:,i]), 2)
        istant_ensemble_variable[:,i] += epsilon_ensemble
        X_ensemble_storage[:,i] = istant_ensemble_variable[:,i]
        variance_ensemble_storage[:,i] = np.power((X_storage[0,i] - X_ensemble_storage[:,i]), 2)        
        average_mse_ensemble[0] = np.mean(variance_ensemble_storage[:,i])
        # Change the conditions on the firs_step to skip the code inside the if for the rest of the iteration
        first_step = False
        # Skip the rest of the loop for the first step
        continue    
    
    for j in range (len(epsilon)): 
        derivatives = lorenz.lorenz_system(istant_variable[j,:], system_parameters)           
        istant_variable[j,:] = istant_variable[j,:] + derivatives[:]*time_step
        X_storage[j,i] = istant_variable[j,0]
        if presence_of_perturbation[j] == True :
            # Skip the variance computation for the unperturbated state
            variance_storage[j,i] = np.power((X_storage[0,i] - X_storage[j,i]), 2) 
            
    if i < (total_steps_ensemble):
        # Compute the ensemble only until the end_ensemble_time
        for j in range (N_ensemble):
            derivates = lorenz.lorenz_system(istant_ensemble_variable[j,:], system_parameters)
            istant_ensemble_variable[j,:] = istant_ensemble_variable[j,:] + derivates[:]*time_step
            X_ensemble_storage[j,i] = istant_ensemble_variable[j,0]
            variance_ensemble_storage[j,i] = np.power((X_storage[0,i] - X_ensemble_storage[j,i]), 2)
        average_mse_ensemble[i] = np.mean(variance_ensemble_storage[:,i])
     
plot.plot_X(X_storage, end_time, total_steps)
plot.plot_rmse(variance_storage, end_time, total_steps)
plot.plot_rmse_e(X_ensemble_storage, X_storage, average_mse_ensemble, end_ensemble_time, total_steps_ensemble)