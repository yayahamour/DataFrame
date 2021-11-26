import streamlit as st
import files as f


def search(multi_select, title_search, actor_search, data, note, time):
    """[summary]

    Args:
        multi_select ([list of string]): [list of the category you want search]
        title_search ([string]): [string of the title you want search]
        actor_search ([string]): [string of the actor you want search]
        data ([dictionary]): [Dictionary where you want search]
        note ([float]): [float of the minimum note of the film you want]
        time ([int]): [int of the duration of the film you want]

    Returns:
        [dctionary]: [result of the different research]
    """
    for select in multi_select:
        data = data.loc[data["Type"].str.contains(select)]
    data = data.loc[data["Actors"].str.contains(actor_search)]
    data = data.loc[data["Titre"].str.contains(title_search)]
    data = data.loc[data["Note"] >= note]
    data = data.loc[data["Duree"].apply(lambda x : f.time_in_minute(str(x))) <= time]    
    return data


def main():
    """[This is the main function to start the project]
    """
    st.title("Recherche :")
    container_movie = st.container()
    movie = f.data_movie()
    container_series = st.container()
    series = f.data_series()
    with container_movie :    
        button_movie = st.sidebar.button("Film")
        multi_select_movie = st.sidebar.multiselect('Genre Film',
                                            ['Drama', 'Action', 'Adventure', 'Sci-Fi', 'Film-Noir',
                                            'War', 'Mystery', 'Thriller', 'Mystery', 'Western', 'Family',
                                            'Fantasy', 'History', 'Romance', 'Comedy', 'Biography', 'Crime',
                                            'Sport'])
        research_title_movie = st.sidebar.text_input("Recherche titre film")
        research_actor_movie = st.sidebar.text_input("Recherche acteur film")
        note_movie = st.sidebar.slider('Note film', 0, 10, 0)
        time_movie = st.sidebar.slider('temps film en minute', 0, 360, 360)
        button_research_movie = st.sidebar.button("Recherche film")
        
        if (button_movie):
            container_movie.dataframe(movie)
        if (button_research_movie):
            research_movie = search(multi_select_movie ,research_title_movie, research_actor_movie , movie, float(note_movie), time_movie)
            container_movie.dataframe(research_movie)



    with container_series :    
        button_series = st.sidebar.button("Serie")
        multi_select_series = st.sidebar.multiselect('Genre Serie',
                                            ['Drama', 'Action', 'Adventure', 'Sci-Fi', 'Film-Noir',
                                            'War', 'Mystery', 'Thriller', 'Mystery', 'Western', 'Family',
                                            'Fantasy', 'History', 'Romance', 'Comedy', 'Biography', 'Crime',
                                            'Sport'])
        research_title_series = st.sidebar.text_input("Recherche titre serie")
        research_actor_series = st.sidebar.text_input("Recherche acteur serie")
        note_series = st.sidebar.slider('Note serie', 0, 10, 0)
        button_research_series = st.sidebar.button("Recherche serie")
        if (button_series):
            container_series.dataframe(series)
        if (button_research_series):
            research_series = search(multi_select_series, research_title_series, research_actor_series, series, float(note_series), 8000)
            container_series.dataframe(research_series)

main()