

class Anomaly:

    def __init__(self):
        pass

    def create_feature(df, object_index):
        t, flux, frequency, power = get_index_data(df, object_index)
        feature = np.array(list(flux) + list(power))
        return feature

    def get_stats(df):
        print_chunk = 10000; counter = 0;
        max_index = df['index'].max()
        ret = {}
        for i in range(max_index):
            t, flux, frequency, power = get_index_data(df, i)
            ave_flux = np.mean(flux)
            ave_power = np.mean(power)
            feature = list(flux) + list(power)
            feature = np.array(feature).reshape(-1, 1)
            if_model = IsolationForest().fit(feature)
            if_score = if_model.decision_function(feature)
            ret[i] = {"ave_flux": ave_flux, "ave_power": ave_power, "if_score": if_score}
            if counter % print_chunk == 0:
                print(f"{counter} fields done")
            counter += 1
        return ret