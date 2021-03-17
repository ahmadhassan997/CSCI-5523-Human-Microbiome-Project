import context

from os import path

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    abundance_df = pd.read_csv(path.join(context.proj_dir, 'data', 'abundance.csv'))
    abundance_stool_df = pd.read_csv(path.join(context.proj_dir, 'data', 'abundance_stoolsubset.csv'))
    # marker_presence_df = pd.read_csv(path.join(context.proj_dir, 'data', 'marker_presence.csv'))
    markers2clades_df = pd.read_csv(path.join(context.proj_dir, 'data', 'markers2clades_DB.csv'))

    print(abundance_df.describe())
    print(abundance_stool_df.describe())
    # print(marker_presence_df.describe())
    print(markers2clades_df.describe())
