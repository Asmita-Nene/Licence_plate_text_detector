import glob
import easyocr
import pandas as pd
from numpy import nan

csv_filepath = r'\licence_plate_numbers.csv'

filepath_lst = glob.glob(r'licence_plates\*.jpg')
print(len(filepath_lst))

plate_nums = []

reader = easyocr.Reader(lang_list=['en'], gpu=True)

for filepath in filepath_lst:
    result = reader.readtext(filepath, detail=0)
    if(len(result) <= 1):
        plate_nums.append(nan)
    else:
        result = str(result[0])
        plate_nums.append(result)


df = pd.DataFrame(data=plate_nums, columns=['Licence_Plate_Numbers'])
df.to_csv(csv_filepath)

print("File saved successfully!")