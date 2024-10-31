import numpy as np    
import matplotlib.pyplot as plt
def plot_X(X_storage, end_time, total_steps):
    # Computation of the array of time
    time=np.linspace(0, end_time, total_steps)
    # Plot the time series of X with and without the smallest perturbation considered
    fig, plot_timeseries = plt.subplots()
    plot_timeseries.set_title('X time series with and without perturbation',fontsize=15)
    plot_timeseries.plot(time,X_storage[0,:], lw=0.7, label='$\epsilon =0$')
    plot_timeseries.plot(time,X_storage[1,:] , lw=0.7, label='$\epsilon =10^{-7}$')
    plot_timeseries.set_xlabel('t',fontsize=15)
    plot_timeseries.set_ylabel('x',fontsize=15)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plot_timeseries.legend(loc='lower right',fontsize=12)
    plt.savefig('images/Fig_X_time_series.png')
    print('Fig_X_Time_series saved inside the directory "images"')

def plot_rmse(variance_storage, end_time, total_steps):
    # Consider a step interval to have a more clear graph
    step_interval=50
    # Compute the Rmse
    Rmse07 = np.sqrt(variance_storage[1, ::step_interval])
    Rmse05 = np.sqrt(variance_storage[2, ::step_interval])
    Rmse03 = np.sqrt(variance_storage[3, ::step_interval]) 
    Rmse01 = np.sqrt(variance_storage[4, ::step_interval])
    # Computation of the array of time
    time_plot_rmse = np.linspace(1, end_time, total_steps)[::step_interval]  
    # Plot of the behave of the Rmse of X perturbated with respect to the
    # unperturbated case with different perturbations
    fig, plot_rmse = plt.subplots()
    plot_rmse.set_title('Rmse time series with different perturbations', fontsize=15)
    plot_rmse.plot(time_plot_rmse, Rmse07, lw=0.7, label='$\epsilon =10^{-7}$')
    plot_rmse.plot(time_plot_rmse, Rmse05, lw=0.7, label='$\epsilon =10^{-5}$')
    plot_rmse.plot(time_plot_rmse, Rmse03, lw=0.7, label='$\epsilon =10^{-3}$')
    plot_rmse.plot(time_plot_rmse, Rmse01, lw=0.7, label='$\epsilon =10^{-1}$')
    plot_rmse.set_xlabel('t', fontsize=15)
    plot_rmse.set_ylabel('Rmse', fontsize=15)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plot_rmse.set_yscale('log')
    plot_rmse.legend()
    plt.savefig('images/Fig_RMSE_time_series.png')
    print('Fig_RMSE_time_series saved inside the directory "images"')

def plot_rmse_e(X_ensemble_storage, X_storage, average_mse_ensemble, end_ensemble_time, total_steps_ensemble):
    # Computation of the MSE of the average ensemble
    average_ensemble = np.mean(X_ensemble_storage, axis=0)
    mse_of_the_average_ensemble = np.power((X_storage[0, :total_steps_ensemble] - average_ensemble), 2)
    # Computation of the array of time
    time_ensemble=np.linspace(0,end_ensemble_time,total_steps_ensemble)
    # Plot for the comparison of the mse of the average rmse and the rmse of the average of the ensemble
    average_rmse_ensemble = np.sqrt(average_mse_ensemble)
    rmse_of_the_average_ensemble = np.sqrt(mse_of_the_average_ensemble)
    fig, plot_rmse_e=plt.subplots()
    plot_rmse_e.set_title('Rmse of the ensemble time series',fontsize=15)
    plot_rmse_e.plot(time_ensemble, average_rmse_ensemble, label='Average rmse')
    plot_rmse_e.plot(time_ensemble,rmse_of_the_average_ensemble, label='Rmse of the ensemble average')
    plot_rmse_e.set_xlabel('t',fontsize=15)
    plot_rmse_e.set_ylabel('Rmse',fontsize=15)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plot_rmse_e.legend(loc='upper left',fontsize=12)
    plt.savefig('images/Fig_ensemble_RMSE_time_series.png')
    print('Fig_ensemble_RMSE_time_series saved inside the directory "images"')

