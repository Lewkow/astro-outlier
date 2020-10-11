

class Plot_Handler:

    def __init__(self):
        pass

    def plot_lightcurve(df, object_index):
        fig, (ax1, ax2) = plt.subplots(2, 1)
        fig.set_size_inches(12, 9)
        fig.subplots_adjust(hspace=0.5)
        
        if isinstance(object_index, list):
            for z in object_index:
                t, flux, frequency, power = get_index_data(df, z)
                ax1.plot(t, flux)
                ax2.loglog(frequency, power)
        else:
            t, flux, frequency, power = get_index_data(df, object_index)
            ax1.plot(t, flux)
            ax2.loglog(frequency, power)

        ax1.set_xlabel('Observation Time')
        ax1.set_ylabel('Flux')
        ax1.grid(True)
        
        ax2.set_xlabel('Frequency [1/days]')
        ax2.set_ylabel('Power')
        ax2.grid(True)

        plt.show()