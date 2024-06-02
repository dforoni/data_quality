import pandas as pd
import pandera as pa
from pandera import Check, Column, DataFrameSchema

df = pd.DataFrame({
    'qtd': [5, 10, 12],
    'descricao': ['laranja', 'banana', 'limão'],
    'data': pd.to_datetime(['2024', '2023', '2022'])
})

schema = pa.infer_schema(df)

with open("inferred_schema.py", "w") as file:
    file.write(schema.to_script())
