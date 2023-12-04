import streamlit as st
import pickle

games = pickle.load(open("games_list.pkl", "rb"))
similarity = pickle.load(open("similarity_scores.pkl", "rb"))


st.header("Game Recommendation System")
selectedGame = st.selectbox("Select Games from dropdown", games)


def recommend(game):
    index = games[games['Title'] == game].index[0]
    distance = sorted(
        list(enumerate(similarity[index])), reverse=True, key=lambda vector: vector[1])
    recommend_games = []

    for i in distance[1:6]:
        recommend_games.append(games.iloc[i[0]].Title)
    return recommend_games


if st.button("Show Recommend"):
    game_recs = recommend(selectedGame)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(game_recs[0])
    with col2:
        st.text(game_recs[1])
    with col3:
        st.text(game_recs[2])
    with col4:
        st.text(game_recs[3])
    with col5:
        st.text(game_recs[4])
