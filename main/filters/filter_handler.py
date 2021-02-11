from main.filters.utils.file_utils import FileUtils
from main.filters.utils.settings_utils import SettingsUtils
from main.filters.primary_filter.primary_filter import PrimaryFilter
from main.filters.api_filter.api_filter import ApiFilter
from main.filters.fasttext_filter.fasttext_filter import FasttextFilter


class FilterHandler():
    def __init__(self):
        SettingsUtils.config_warning_settings()
        SettingsUtils.config_dataframe_settings()
        self.primary_filter = self.__build_primary_filter()
        self.fasttext_filter = self.__build_fasttext_filter()
        self.api_filter = self.__build_api_filter()

    def __build_primary_filter(self) -> PrimaryFilter:
        tmp_primary_filter = PrimaryFilter(filter_list=None)
        return tmp_primary_filter

    def __build_api_filter(self):
        tmp_api_filter = ApiFilter()
        return tmp_api_filter

    def __build_fasttext_filter(self):
        tmp_fasttext_filter = FasttextFilter()
        return tmp_fasttext_filter

    def train_fasttext_model(self):
        self.fasttext_filter.train()

    def load_fasttext_model(self):
        self.fasttext_filter.load()

    def filter(self, text):
        pass