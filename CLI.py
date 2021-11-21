import sys
from filters import AllFilters

AllFilters = AllFilters()
# exists *args
# exists **kwargs

args = sys.argv

dictionary = {}
listArgs = []

def apply_filters():
    for values in dictionary.keys():
        if "gray" in dictionary[values]:
            AllFilters.gray_filter()

        if "blur" in dictionary[values]:
            AllFilters.blur_filter()

        if "dilate" in dictionary[values]:
            AllFilters.dilate_filter()


def create_dictionnary():
    for value in range(len(listArgs)):
        dictionary[value] = listArgs[value]
        apply_filters()



for strParam in sys.argv[1:]:
    x = strParam.split(":")
    v = str(x).split("|")
    listArgs.extend(v)
    create_dictionnary()








    # dictionary[strParam.split(":")] = 'value'
    #
    # print(dictionary)
    # if strParam == "blur":

    # if strParam == "blur":
    #     dictionary["blur"] = "value"
    #