import string

inp_list_string_check = ['ngfnd,', 'ACCd,,aa', 'fgd.gdg!', 'f fvkmf?', 'fn, vl@#!!!', 'df&&&fd&f????']


class TextProcessor(object):

    def _is_punctuation(self, symbol_check: str) -> bool:
        return symbol_check.isalpha()

    def get_clean_string(self, string_check: str) -> str:
        new_string = ''

        for symbol_check in string_check:
            if self._is_punctuation(symbol_check):
                new_string += symbol_check

        return new_string


class TextLoader:
    def __init__(self):
        self.__text_processor = TextProcessor()
        self.__clean_string: str = ""

    @property
    def clean_string(self):
        print('Виводиться вже очищений текст')
        return self.__clean_string

    def set_clean_text(self, raw_string: str):
        clean_str = self.__text_processor.get_clean_string(raw_string)
        self.__clean_string = clean_str


class DataInterface:
    def __init__(self):
        self._text_loader = TextLoader()

    def process_texts(self, text: list):
        for line in text:
            self._text_loader.set_clean_text(line)
            print(self._text_loader.clean_string)


di = DataInterface()

di.process_texts(inp_list_string_check)




