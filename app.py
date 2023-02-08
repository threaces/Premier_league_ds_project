import importlib
import pandas as pd


class CollectData:
    MODULES_NAMES = ('Weather', 'Table', 'Altitude', 'Scores_fixtures')

    def get_data(self):
        self.actual_data = {}

        for module_name in self.MODULES_NAMES:
            parser_module = importlib.import_module(f'backends.{module_name}.parser')
            parser_obj = parser_module.Parser()
            self.actual_data[module_name] = parser_obj.get_data()

        return self.actual_data
 
    def convert_to_df(self):
        data = self.get_data()
        dataframe = pd.DataFrame.from_dict(data, orient='index')

        return dataframe

    def convert_to_csv(self):
        
        data_df = self.convert_to_df()
        load_to_csv_file = data_df.to_csv('raw_database.csv')

        return load_to_csv_file

object_dict = CollectData()
print(object_dict.convert_to_df())