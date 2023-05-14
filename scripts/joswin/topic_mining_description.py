__author__ = 'joswin'

import pandas as pd
from sqlalchemy import create_engine
engine = create_engine('postgresql://postgres:postgres@localhost:5432/linkedin_data')

tmp = pd.read_sql('linkedin_company_base_settu_sir',engine)
text_list = list(tmp['description'])
del tmp

from text_processing import word_transformations
tk = word_transformations.Tokeni