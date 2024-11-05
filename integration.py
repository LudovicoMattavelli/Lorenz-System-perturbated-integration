import numpy as np
import lorenz as lorenz
import random
import plot

# Open the file with the values of the parameters to define the problem
with open('parameters.txt', 'r') as file:
    file_content = file.read()
# Execute the content of the file
exec(file_content)

# Define the variables for the sensitivity study
total_steps = int(end_time/time_step)
X_storage = np.zeros([len(epsilon), total_steps])
variance_storage = np.zeros([len(epsilon), total_steps])
istant_variable = np.tile(initial_conditions, (len(epsilon), 1))
derivatives = np.zeros(3)

# Define the variables for the ensemble study
total_steps_ensemble = int(end_ensemble_time/time_step)
random.seed(42) 
epsilon_ensemble = [random.uniform(distribution_inf, distribution_sup) for i in range(N_ensemble)]
X_ensemble_storage = np.zeros([N_ensemble, total_steps_ensemble])
variance_ensemble_storage = np.zeros([N_ensemble, total_steps_ensemble])
X_ensemble_storage_mean = np.zeros(total_steps_ensemble)
istant_ensemble_variable = np.tile(initial_conditions, (len(epsilon_ensemble), 1))
average_mse_ensemble = np.zeros(total_steps_ensemble)

# Define the variables for the if conditions 
presence_of_perturbation = np.full(len(epsilon), True)
presence_of_perturbation[0] = False
first_step = True

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
        # Update the firs_step condition to avoid the block for the rest of the iterations
        first_step = False
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
print("End integration.")
        
# Calculate the mean squared error (mse) of the ensemble average
average_ensemble = np.mean(X_ensemble_storage, axis=0)
mse_of_the_average_ensemble = np.power((X_storage[0, :total_steps_ensemble] - average_ensemble), 2) 
# Calculate the two RMSE values for the ensemble
average_rmse_ensemble = np.sqrt(average_mse_ensemble)
rmse_of_the_average_ensemble = np.sqrt(mse_of_the_average_ensemble)

# Call the plot functions
plot.plot_X(X_storage, end_time, total_steps)
plot.plot_rmse(variance_storage, end_time, total_steps)
plot.plot_rmse_e(average_rmse_ensemble, rmse_of_the_average_ensemble, end_ensemble_time, total_steps_ensemble)
