import context

from os import path

import pandas as pd

if __name__ == '__main__':
    abundance_stool_df = pd.read_csv(path.join(context.proj_dir, 'data', 'abundance_stoolsubset.csv'))
    summary = abundance_stool_df.mask(abundance_stool_df == 0).describe()
    summary.reset_index(inplace=True)
    summary = summary.transpose()
    summary.reset_index(inplace=True)
    summary.columns = summary.iloc[0]
    summary.drop([0], inplace=True)
    summary.sort_values(by='count', inplace=True, ascending=False)
    summary.to_csv(path.join(context.proj_dir, 'data_processed', 'summary', 'stool_bacteria_summary.csv'),
                   index=False)
    print('Bacteria Count > 1000', summary[summary['count'] > 1000].shape[0])
    summary = abundance_stool_df.mask(abundance_stool_df == 'nd').describe(include='object')
    summary.reset_index(inplace=True)
    summary = summary.transpose()
    summary.reset_index(inplace=True)
    summary.columns = summary.iloc[0]
    summary.drop([0], inplace=True)
    summary.sort_values(by='count', inplace=True, ascending=False)
    summary.to_csv(path.join(context.proj_dir, 'data_processed', 'summary', 'stool_object_summary.csv'),
                   index=False)
