import importlib
import pandas as pd


class CollectData:
    MODULES_NAMES = ('Weather', 'Scores_fixtures', 'Table')

    def convert_to_run(self):
        self.actual_data = {}

        for module_name in self.MODULES_NAMES:
            print(module_name)
            parser_module = importlib.import_module(f'backends.{module_name}.parser')
            parser_obj = parser_module.Parser()
            parser_obj.convert_to_csv()

object_dict = CollectData()
object_dict.convert_to_run()