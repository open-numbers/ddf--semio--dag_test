# coding: utf8

import pandas as pd

if __name__ == '__main__':
    print('new reop!')

    df = pd.DataFrame.from_records(
        [{'concept': 'name', 
        'name': 'Name', 
        'concept_type': 'string'}])
    df.to_csv('../../ddf--concepts.csv', index=False)
