import os
import pandas as pd 

class Helper:

    def read_equipment_excel():
        equipment_list = []
        print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        try:
            parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            data_frame = pd.read_excel(parent_dir + '/src/equipment.xlsx', sheet_name = 'Sheet1', header=None, skiprows=1, engine = 'openpyxl')
        except:
            return None

        for eq in range(len(data_frame)):
            equipment = data_frame.loc[eq,0] + ' ' +  data_frame.loc[eq,1]
            equipment_list.append(equipment)

        return equipment_list
        

if __name__ == '__main__':
    helper = Helper()
    helper.read_equipment_excel()