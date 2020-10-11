


class Data_Handler:

    def __init__(self):
        pass

    def get_index_data(df, z):
        z_index_data = df[df['index'] == z][['observation_time', 'g_flux']]
        t = z_index_data['observation_time'].to_list()
        flux = z_index_data['g_flux'].to_list()
        frequency, power = LombScargle(t, flux).autopower()
        return t, flux, frequency, power