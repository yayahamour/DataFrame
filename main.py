from datetime import date
import streamlit as st
import pandas
import re

def data_film():
    film = pandas.read_csv("film.csv")
    film["Duree"] = film["Duree"].map(lambda time: time.replace(",", ""))
    film["Duree"] = film["Duree"].map(lambda time: time.replace("h ",":"))
    film["Duree"] = film["Duree"].map(lambda time: time.replace("h",""))
    film["Duree"] = film["Duree"].map(lambda time: time.replace("m", ""))
    film["Duree"] = film["Duree"].map(lambda time: re.sub(r"^[0-9]+$", "0:"+time, time))
    film["Titre_original"] = film["Titre_original"].fillna("")
    film["Titre_original"]= film["Titre_original"].map(lambda time: re.sub("Original title: ", "", time)) 
    return film

def data_serie():
    serie = pandas.read_csv("serie.csv")
    serie["Duree"] = serie["Duree"].map(lambda time: time.replace(",", ""))
    serie["Duree"] = serie["Duree"].map(lambda time: time.replace("h ",":"))
    serie["Duree"] = serie["Duree"].map(lambda time: time.replace("m", ""))
    serie["Duree"] = serie["Duree"].map(lambda time: re.sub("TV Mini Series", "", time))
    serie["Duree"] = serie["Duree"].map(lambda time: re.sub("TV Series", "", time))
    serie["Titre_original"] = serie["Titre_original"].fillna("")
    serie["Titre_original"]= serie["Titre_original"].map(lambda time: re.sub("Original title: ", "", time)) 
    return serie

def recherche(multi_select, recherche_titre, recherche_actor, in_screen, note):
    for select in multi_select:
        in_screen = in_screen.loc[in_screen["Type"].str.contains(select)]
    in_screen = in_screen.loc[in_screen["Actors"].str.contains(recherche_actor)]
    in_screen = in_screen.loc[in_screen["Titre"].str.contains(recherche_titre)]
    in_screen = in_screen.loc[in_screen["Note"] >= note]
    return in_screen

def time_minute(time):
    tab = time.split(':')
    return((int(tab[0])*60) + int(tab[1]))

def time_heure(minute):
    heure = 0
    while(minute > 60):
        heure += 1
        minute -= 60
    string = str(heure) + ":" + str(minute)
    return(string)


st.title("Recherche :")
container_film = st.container()
film = data_film()
container_serie = st.container()
serie = data_serie()
with container_film :    
    button_film = st.sidebar.button("Film")
    multi_select_film = st.sidebar.multiselect('Genre Film',
                                         ['Drama', 'Action', 'Adventure', 'Sci-Fi', 'Film-Noir',
                                          'War', 'Mystery', 'Thriller', 'Mystery', 'Western', 'Family',
                                          'Fantasy', 'History', 'Romance', 'Comedy', 'Biography', 'Crime',
                                          'Sport'])
    recherche_titre_film = st.sidebar.text_input("Recherche titre film")
    recherche_actor_film = st.sidebar.text_input("Recherche acteur film")
    note_film = st.sidebar.slider('Note film', 0, 10, 5)
    button_recherche_film = st.sidebar.button("Recherche film")
    
    if (button_film):
        container_film.dataframe(film)
    if (button_recherche_film):
        recherche_film = recherche(multi_select_film, recherche_titre_film, recherche_actor_film, film, float(note_film))
        container_film.dataframe(recherche_film)



with container_serie :    
    button_serie = st.sidebar.button("Serie")
    multi_select_serie = st.sidebar.multiselect('Genre Serie',
                                         ['Drama', 'Action', 'Adventure', 'Sci-Fi', 'Film-Noir',
                                          'War', 'Mystery', 'Thriller', 'Mystery', 'Western', 'Family',
                                          'Fantasy', 'History', 'Romance', 'Comedy', 'Biography', 'Crime',
                                          'Sport'])
    recherche_titre_serie = st.sidebar.text_input("Recherche titre serie")
    recherche_actor_serie = st.sidebar.text_input("Recherche acteur serie")
    note_serie = st.sidebar.slider('Note serie', 0, 10, 5)
    button_recherche_serie = st.sidebar.button("Recherche serie")
    if (button_serie):
        container_serie.dataframe(serie)
    if (button_recherche_serie):
        recherche_serie = recherche(multi_select_serie, recherche_titre_serie, recherche_actor_serie, serie, float(note_serie))
        container_serie.dataframe(recherche_serie)