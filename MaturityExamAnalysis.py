from urllib.request import urlopen
import sys


class MaturityExamAnalysis:
    def __init__(self, url="https://www.dane.gov.pl/media/resources/20190513/Liczba_os%C3%B3b_kt%C3%B3re"
                           "_przystapi%C5%82y_lub_zda%C5%82y_egzamin_maturalny.csv"):
        self.data = urlopen(url)
        self.territory = []         # territory
        self.status = []            # participated/passed
        self.gender = []            # gender
        self.year = []              # year
        self.people = []            # number of people
        self.get_data()

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

    def get_data(self):
        iter_data = iter(self.data)
        next(iter_data)
        for line in iter_data:
            line = self.clean_string(line)
            territory_temp, status_temp, gender_temp, year_temp, people_temp = str(line).split(";")

            self.territory.append(territory_temp)
            self.status.append(status_temp)
            self.gender.append(gender_temp)
            self.year.append(int(year_temp))
            self.people.append(int(people_temp))

    def get_number_of_people(self, year_param, gender_param):
        people_count = 0
        average_people_per_voivodeship = []
        for array_index, item in enumerate(self.year):
            if item == int(year_param):
                if gender_param == "both":
                    if self.status[array_index] == "przystąpiło" and self.territory[array_index] != "Polska":
                        people_count += self.people[array_index]
                else:
                    if self.status[array_index] == "przystąpiło" and self.territory[array_index] != "Polska" \
                            and self.gender[index] == gender_param:
                        people_count += self.people[array_index]
        unique_territory = set(self.territory)
        average_people_per_voivodeship.append(people_count // (len(unique_territory) - 1))
        return average_people_per_voivodeship

    @staticmethod
    def fill_arrays_with_0(param_array_length):
        attend_count = []
        pass_count = []
        pass_rate = []
        for _ in range(param_array_length):
            attend_count.append(0)
            pass_count.append(0)
            pass_rate.append(0)
        return attend_count, pass_count, pass_rate

    def fill_arrays_with_data(self, length_of_array, territories_number, years_number, unique_year_set,
                              unique_territory_set, number_attended, number_passed, rate_of_pass, gender_param="both"):
        for array_index in range(length_of_array):
            if self.territory[array_index] in unique_territory_set and self.year[array_index] in unique_year_set:
                if territories_number == 1:
                    i = unique_year_set.index(self.year[array_index])
                elif years_number == 1:
                    i = unique_territory_set.index(self.territory[array_index])
                else:
                    i = unique_year_set.index(self.year[array_index]) * territories_number + \
                        unique_territory_set.index(self.territory[array_index])
                if self.status[array_index] == "przystąpiło":
                    if gender_param == "both":
                        number_attended[i] += self.people[array_index]
                    else:
                        if self.gender[array_index] == gender_param:
                            number_attended[i] += self.people[array_index]
                elif self.status[array_index] == "zdało":
                    if gender_param == "both":
                        number_passed[i] += self.people[array_index]
                    else:
                        if self.gender[array_index] == gender_param:
                            number_passed[i] += self.people[array_index]
        for array_index in range(len(rate_of_pass)):
            rate_of_pass[array_index] = 100 * number_passed[array_index] / number_attended[array_index]

    def get_pass_rate(self, *parameters, gender_param="both"):
        unique_year = sorted(set(self.year))
        unique_territory = sorted(set(self.territory))
        unique_territory.remove("Polska")

        if not parameters:                                                                  # zad 4
            array_length = len(unique_territory) * len(unique_year)
            attend_count, pass_count, pass_rate = self.fill_arrays_with_0(param_array_length=array_length)
            number_of_territories = len(unique_territory)
            number_of_years = len(unique_year)
            self.fill_arrays_with_data(length_of_array=len(self.year), territories_number=number_of_territories,
                                       years_number=number_of_years, unique_year_set=unique_year,
                                       unique_territory_set=unique_territory, number_attended=attend_count,
                                       number_passed=pass_count, rate_of_pass=pass_rate, gender_param=gender_param)
            return pass_rate, unique_territory, unique_year, number_of_territories

        elif any(isinstance(par, int) for par in parameters):                               # zad 3
            array_length = len(unique_territory)
            attend_count, pass_count, pass_rate = self.fill_arrays_with_0(param_array_length=array_length)
            number_of_territories = len(unique_territory)
            number_of_years = len(parameters)
            self.fill_arrays_with_data(length_of_array=len(self.year), territories_number=number_of_territories,
                                       years_number=number_of_years, unique_year_set=parameters,
                                       unique_territory_set=unique_territory, number_attended=attend_count,
                                       number_passed=pass_count, rate_of_pass=pass_rate, gender_param=gender_param)
            return pass_rate, unique_year, unique_territory

        elif any(isinstance(par, str) for par in parameters) and len(parameters) >= 2:      # zad 5
            array_length = 2 * len(unique_year)
            attend_count, pass_count, pass_rate = self.fill_arrays_with_0(param_array_length=array_length)
            number_of_territories = len(parameters)
            number_of_years = len(unique_year)
            self.fill_arrays_with_data(length_of_array=len(self.year), territories_number=number_of_territories,
                                       years_number=number_of_years, unique_year_set=unique_year,
                                       unique_territory_set=parameters, number_attended=attend_count,
                                       number_passed=pass_count, rate_of_pass=pass_rate, gender_param=gender_param)
            return pass_rate, unique_year, unique_territory

        else:                                                                               # zad 2
            array_length = len(unique_year)
            attend_count, pass_count, pass_rate = self.fill_arrays_with_0(param_array_length=array_length)
            number_of_territories = 1
            number_of_years = len(unique_year)
            self.fill_arrays_with_data(length_of_array=len(self.year), territories_number=number_of_territories,
                                       years_number=number_of_years, unique_year_set=unique_year,
                                       unique_territory_set=parameters, number_attended=attend_count,
                                       number_passed=pass_count, rate_of_pass=pass_rate, gender_param=gender_param)
            return pass_rate, unique_year

    # Zadanie 1
    def zad_1(self, year_param, gender_param="both"):
        res = self.get_number_of_people(year_param=year_param, gender_param=gender_param)
        for item in res:
            print(item)

    # Zadanie 2
    def zad_2(self, territory_param, gender_param="both"):
        pass_rate, unique_year = self.get_pass_rate(territory_param, gender_param=gender_param)
        for array_index in range(len(unique_year)):
            print(str(unique_year[array_index]) + " - " + str(round(pass_rate[array_index])))

    # Zadanie 3
    def zad_3(self, year_param, gender_param="both"):
        pass_rate, unique_year, unique_territory = self.get_pass_rate(year_param, gender_param=gender_param)
        max_pass_rate = 0
        max_pass_rate_index = 0

        for i in range(len(pass_rate)):
            if pass_rate[i] > max_pass_rate:
                max_pass_rate = pass_rate[i]
                max_pass_rate_index = i

        print(str(year_param) + " - " + unique_territory[max_pass_rate_index])

    # Zadanie 4
    def zad_4(self, gender_param="both"):
        pass_rate, unique_territory, unique_year, number_of_territories = self.get_pass_rate(gender_param=gender_param)
        results = []
        for array_index in range(len(pass_rate) - number_of_territories):
            if pass_rate[array_index] > pass_rate[array_index + number_of_territories] and \
                    unique_territory[array_index % number_of_territories] != "Polska":
                results.append(unique_territory[array_index % number_of_territories] + ": " +
                               str(unique_year[array_index // number_of_territories]) + " -> " +
                               str(unique_year[(array_index + number_of_territories) // number_of_territories]))
        results.sort()
        for result in results:
            print(result)

    # Zadanie 5
    def zad_5(self, territory_1, territory_2, gender_param="both"):
        pass_rate, unique_year, unique_territory = self.get_pass_rate(territory_1, territory_2,
                                                                      gender_param=gender_param)
        array_index = 0
        territory_set = [territory_1, territory_2]
        # territory_set = sorted(territory_set)
        for _ in range(len(pass_rate) // 2):
            if pass_rate[array_index] >= pass_rate[array_index + 1]:
                better = territory_set[0]
            else:
                better = territory_set[1]
            print(str(unique_year[array_index // 2]) + " - " + better)
            array_index += 2


if __name__ == "__main__":

    if len(sys.argv) > 1:
        function_arg = "mat." + sys.argv[1]
        for index in range(len(sys.argv[2:])):
            if sys.argv[index + 2].isdigit():
                sys.argv[index + 2] = int(sys.argv[index + 2])

        mat = MaturityExamAnalysis("https://www.dane.gov.pl/media/resources/20190513/Liczba_os%C3%B3b_kt%C3%B3re"
                                   "_przystapi%C5%82y_lub_zda%C5%82y_egzamin_maturalny.csv")

        function_dict = {"zad_1": mat.zad_1,
                         "zad_2": mat.zad_2,
                         "zad_3": mat.zad_3,
                         "zad_4": mat.zad_4,
                         "zad_5": mat.zad_5}

        function_dict[sys.argv[1]](*sys.argv[2:])
    else:
        print("Please pass some arguments.")
