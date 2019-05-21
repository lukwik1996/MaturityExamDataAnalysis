from urllib.request import urlopen


class MaturityExamAnalysis:
    def __init__(self, url):
        self.data = urlopen(url)

    @staticmethod
    def clean_string(text):
        text = str(text)
        text = text.replace("\\xb9", "ą")
        text = text.replace("\\xb3", "ł")
        text = text.replace("\\xea", "ę")
        text = text.replace("\\xbf", "ż")
        text = text.replace("\\x9f", "ź")
        text = text.replace("\\x9c", "ś")
        text = text.replace("\\xf1", "ń")
        text = text.replace("\\x8c", "Ś")
        text = text.replace("\\xa3", "Ł")
        text = text.replace("\\xf3", "ó")
        text = text.replace("b'", "")
        text = text.replace("\\r\\n\'", "")
        return text


if __name__ == "__main__":

    mat = MaturityExamAnalysis("https://www.dane.gov.pl/media/resources/20190513/Liczba_os%C3%B3b_kt%C3%B3re_przystapi%C5%82y"
                         "_lub_zda%C5%82y_egzamin_maturalny.csv")

    iterData = iter(mat.data)
    next(iterData)

    for line in iterData:
        line = mat.clean_string(line)
        print(line)
