

class IOHandler:

    def __init__(self):
        self.data_fid_npy = "../data/KeplerSampleWErr.npy"
        self.data_fid_csv = "../data/kepDenselcvs.csv"

    def import_numpy_fid(self, numpy_fid):
        data_array = np.load(self.data_fid, allow_pickle=True)
        return data_array

    def read_data(data_fid):
        if 'csv' in self.data_fid:
            return pd.read_csv(self.data_fid)
        else:
            print('whomp whomp')

        