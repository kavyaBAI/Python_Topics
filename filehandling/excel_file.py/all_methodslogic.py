#here have excel file groupby grade and agin sort by marks here is snippit
import pandas as pd

filepath = r"C:\Users\kavya\OneDrive\Documents\currency convertor\output.xlsx"

df = pd.read_excel(filepath)
grouped_value = df.groupby('grade').mean().reset_index()
sorted_values = grouped_value.sort_values('marks', ascending=False)

output_filepath = r"C:\Users\kavya\OneDrive\Documents\currency convertor\excel.xlsx"
sorted_values.to_excel(output_filepath, index=False)
#________________________________________________________________________________________________________