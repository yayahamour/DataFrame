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

def recherche(multi_select, recherche_titre, recherche_actor, in_screen):
    aff = in_screen
    for select in multi_select:
        aff = aff.loc[aff["Type"].str.contains(select)]
    aff = aff.loc[aff["Actors"].str.contains(recherche_actor)]
    aff = aff.loc[aff["Titre"].str.contains(recherche_titre.lower())]
    return aff


st.title("Appli")
serie = data_serie()
film = data_film()
button = st.sidebar.button("Serie")
button1 = st.sidebar.button("Film")
multi_select = st.sidebar.multiselect('Genre',
                                        ['Drama', 'Action', 'Adventure', 'Sci-Fi', 'Film-Noir',
                                         'War', 'Mystery', 'Thriller', 'Mystery', 'Western', 'Family',
                                         'Fantasy', 'History', 'Romance', 'Comedy', 'Biography', 'Crime',
                                         'Sport'])
recherche_titre = st.sidebar.text_input("Recherche titre")
recherche_actor = st.sidebar.text_input("Recherche acteur")
in_screen = film

if (button):
    in_screen = serie
    aff = serie
    st.write(aff)

if (button1):
    in_screen = film
    aff = film
    st.write(aff)

if(recherche_titre):
    aff = recherche(multi_select, recherche_titre, recherche_actor, in_screen)
    st.write(aff)
    
if(recherche_actor):
    aff = recherche(multi_select, recherche_titre, recherche_actor, in_screen)
    st.write(aff)

if (multi_select):
    aff = recherche(multi_select, recherche_titre, recherche_actor, in_screen)
    st.write(aff)
