# coding: utf8

import pandas as pd

if __name__ == '__main__':
    print('new reop!')

    concepts = pd.DataFrame.from_records(
        [{'concept': 'name',
          'name': 'Name_2',
          'concept_type': 'string'},
         {'concept': 'dps_e',
          'name': 'datapoints',
          'concept_type': 'measure'},
         {'concept': 'time',
          'name': 'time',
          'concept_type': 'time'},
         {'concept': 'ent',
          'name': 'entity',
          'concept_type': 'entity_domain'}])
    concepts.to_csv('../../ddf--concepts.csv', index=False)

    entities = pd.DataFrame.from_records(
        [{'ent': 'a', 'name': 'a'}]
    )
    entities.to_csv('../../ddf--entities--ent.csv', index=False)

    datapoints = pd.DataFrame.from_records(
        [{'ent': 'a', 'time': 1990, 'dps': 1},
         {'ent': 'a', 'time': 1991, 'dps': 2}]
    )

    datapoints.to_csv('../../ddf--datapoints--dps--by--ent--time.csv', index=False)
