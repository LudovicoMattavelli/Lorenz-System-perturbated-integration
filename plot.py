import numpy as np    
import matplotlib.pyplot as plt

def plot_X(X_storage, end_time, total_steps):
    """This method plots the time series of the x variable with and without the smallest 
    perturbation considered in the study: 1E-07.
    
    Parameters
    ----------
    X_storage : 2-dimensional NumPy array
        Array containing the time series data for the variable x.
    end_time : float
        The final time value of the time series.
    total_steps : int
        The number of steps in the time series.
    """
    # Generate the time array
    time = np.linspace(0, end_time, total_steps)
    
    fig, plot_timeseries = plt.subplots()
    plot_timeseries.set_title('X time series with and without perturbation', fontsize=15)
    plot_timeseries.plot(time, X_storage[0, :], lw=0.7, label='$\epsilon =0$')
    plot_timeseries.plot(time, X_storage[1, :], lw=0.7, label='$\epsilon =10^{-7}$')
    plot_timeseries.set_xlabel('t', fontsize=15)
    plot_timeseries.set_ylabel('x', fontsize=15)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plot_timeseries.legend(loc='lower right', fontsize=12)
    plt.savefig('images/Fig_X_time_series.png')
    print('Fig_X_Time_series saved in the directory "images"')

def plot_rmse(variance_storage, end_time, total_steps):
    """This method plots the RMSE time series of four perturbed solutions 
    compared to the unperturbed one.
    
    Parameters
    ----------
    variance_storage : 2-dimensional NumPy array
        Array containing the variance of the differences between perturbed and 
        unperturbed solutions.
    end_time : float
        The final time value of the time series.
    total_steps : int
        The number of steps in the time series.
    """
    # Define a step interval to create a clearer graph
    step_interval = 50
    # Compute the RMSE values
    Rmse07 = np.sqrt(variance_storage[1, ::step_interval])
    Rmse05 = np.sqrt(variance_storage[2, ::step_interval])
    Rmse03 = np.sqrt(variance_storage[3, ::step_interval]) 
    Rmse01 = np.sqrt(variance_storage[4, ::step_interval])
    # Generate the time array
    time_plot_rmse = np.linspace(1, end_time, total_steps)[::step_interval]  
    
    fig, plot_rmse = plt.subplots()
    plot_rmse.set_title('RMSE time series with different perturbations', fontsize=15)
    plot_rmse.plot(time_plot_rmse, Rmse07, lw=0.7, label='$\epsilon =10^{-7}$')
    plot_rmse.plot(time_plot_rmse, Rmse05, lw=0.7, label='$\epsilon =10^{-5}$')
    plot_rmse.plot(time_plot_rmse, Rmse03, lw=0.7, label='$\epsilon =10^{-3}$')
    plot_rmse.plot(time_plot_rmse, Rmse01, lw=0.7, label='$\epsilon =10^{-1}$')
    plot_rmse.set_xlabel('t', fontsize=15)
    plot_rmse.set_ylabel('RMSE', fontsize=15)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plot_rmse.set_yscale('log')
    plot_rmse.legend()
    plt.savefig('images/Fig_RMSE_time_series.png')
    print('Fig_RMSE_time_series saved in the directory "images"')

def plot_rmse_e(average_rmse_ensemble, rmse_of_the_average_ensemble, end_ensemble_time, total_steps_ensemble):
    """This method plots the RMSE time series for the ensemble time series and the RMSE of 
    the ensemble average.
    
    Parameters
    ----------
    average_rmse_ensemble : 1-dimensional NumPy array
        Array containing the average root mean squared error of the memebers of the ensemble time series.
    rmse_of_the_average_ensemble: 1-dimensional NumPy array
        Array containing the root mean squared error of the average of the ensemble time series.
    end_ensemble_time : float
        The final time value of the ensemble time series.
    total_steps_ensemble : int
        The number of steps in the ensemble time series.
    """
    # Generate the time array
    time_ensemble = np.linspace(0, end_ensemble_time, total_steps_ensemble)
    
    fig, plot_rmse_e = plt.subplots()
    plot_rmse_e.set_title('RMSE time series of the ensemble', fontsize=15)
    plot_rmse_e.plot(time_ensemble, average_rmse_ensemble, label='Average RMSE')
    plot_rmse_e.plot(time_ensemble, rmse_of_the_average_ensemble, label='RMSE of the ensemble average')
    plot_rmse_e.set_xlabel('t', fontsize=15)
    plot_rmse_e.set_ylabel('RMSE', fontsize=15)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plot_rmse_e.legend(loc='upper left', fontsize=12)
    plt.savefig('images/Fig_ensemble_RMSE_time_series.png')
    print('Fig_ensemble_RMSE_time_series saved in the directory "images"')
