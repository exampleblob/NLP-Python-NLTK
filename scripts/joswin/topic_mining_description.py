__author__ = 'joswin'

import pandas as pd
from sqlalchemy import create_engine
engine = create_engine('postgresql://postgres:postgres@localhost:5432/linkedin_data')

tmp = pd.read_sql('linkedin_compan