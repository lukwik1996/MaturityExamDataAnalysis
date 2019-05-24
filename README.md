# MaturityExamDataAnalysis
A script for analyzing data about Maturity Exam pass rate in Poland in years 2010 - 2018

There are five different commands available to use with this script. To execute a function, 
you need to pass it's name as an argument. You can either use english or polish function 
and argument names. The full list of available functions is visible below.
___
**AverageAttendants** *year* *gender*

    this function returns the average number of people attending maturity exam in year provided

**PassRateOverYears** *voivodeship* *gender*

    this function returns pass rate over years for the given voivodeship

**TopVoivodeship** *year* *gender*

    this function returns voivodeship with the highest pass rate in given year

**Regression** *gender*

    this function returns when different voivodeships' pass rate decreased from year to year

**CompareTwo** *voivodeship1* *voivodeship2* *gender*

    this function lets you compare two voivodeships over years and for each year it returns the one that has a higher pass rate
___
The *gender* argument is optional in every case and it can be set to either **male** or **female**.