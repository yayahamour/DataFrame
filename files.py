import pandas
import re

def time_format(time):
    """[This function change the format Xh Ym with X : hours ans Y : minute to format X:Y]

    Args:
        time ([string]): [time on format Xh Ym]

    Returns:
        [string]: [time on format X:Y]
    """
    hour = 0
    minute = 0
    recherche = (re.findall(r"([0-9]+)h", time))
    if (len(recherche) > 0):
        hour = int(recherche[0])
    recherche = (re.findall(r"([0-9]+)m", time))
    if (len(recherche) > 0):
        minute = int(recherche[0])
    string = str(hour)
    if (minute >= 10):
        string+=":"+str(minute)
    else:
        string+=":0"+str(minute)
    return string


def time_in_minute(time):
    """[This function give the minute of time]

    Args:
        time ([string]): [String of time in format X:Y with  X : hour and Y : minute]

    Returns:
        [int]: [return the time in minute]
    """
    tab = time.split(':')
    if (len(tab) == 2):
        return((int(tab[0])*60) + int(tab[1]))
    tab[0] = tab[0].replace(":", "")
    return (int(tab[0]))


def data_movie():
    """[This function read the data of file film.csv to a dictionary]

    Returns:
        [dictionnary]: [return the dictionary]
    """
    movie = pandas.read_csv("film.csv")
    movie["Duree"] = movie["Duree"].map(lambda time: time.replace(",", ""))
    movie["Duree"] = movie["Duree"].map(lambda time: re.sub("TV Mini Series", "", time))
    movie["Duree"] = movie["Duree"].map(lambda time: re.sub("TV Series", "", time))
    movie["Duree"] = movie["Duree"].map(lambda time: time_format(time))
    movie["Titre_original"] = movie["Titre_original"].fillna("")
    movie["Titre_original"]= movie["Titre_original"].map(lambda time: re.sub("Original title: ", "", time)) 
    return movie

def data_series():
    """[This function read the data of file serie.csv to a dictionary]

    Returns:
        [dictionnary]: [return the dictionary]
    """
    series = pandas.read_csv("serie.csv")
    series["Duree"] = series["Duree"].map(lambda time: time.replace(",", ""))
    series["Duree"] = series["Duree"].map(lambda time: re.sub("TV Mini Series", "", time))
    series["Duree"] = series["Duree"].map(lambda time: re.sub("TV Series", "", time))
    series["Duree"] = series["Duree"].map(lambda time: time_format(time))
    series["Titre_original"] = series["Titre_original"].fillna("")
    series["Titre_original"]= series["Titre_original"].map(lambda time: re.sub("Original title: ", "", time)) 
    return series

