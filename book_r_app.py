import pickle as pkl
import streamlit as st
import numpy as np

book = pkl.load(open('Books.pkl','rb'))
pivot = pkl.load(open('pivot.pkl','rb'))
similarity = pkl.load(open('similarity_score.pkl','rb'))
book_l = list(book['Book-Title'].values)
book_l = [" "] + book_l
book_list = []
for x in book_l:
    if x not in book_list:
        book_list.append(x)

def recommender(book_name):
    index = np.where(pivot.index==book_name)[0][0]
    similar = sorted(list(enumerate(similarity[index])),key=lambda x:x[1],reverse=True)[1:6]
    suggestion = []
    for x in similar:
        suggestion.append(pivot.index[x[0]])
        suggestion.append(book['Image-URL-M'][(book['Book-Title'] == pivot.index[x[0]]) & (book['Book-Rating'] == book['Book-Rating'].max())].values[0])
    return suggestion
st.title(':violet[Book Recommendation]')
st.subheader('This system will suggest 5 books by analysing the searched book user ratings and their prefrences.')
selected_movie = st.selectbox('Type or select Books',book_list)
if st.button('Show Recommendation'):
    if selected_movie == " ":
        st.write(':red[No Book was Selected :(]')
    else:
        st.write('These are the Books that you might like: ')
        suggestion = recommender(selected_movie)
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            st.subheader(suggestion[0])
            st.image(suggestion[1])
        with col2:
            st.subheader(suggestion[2])
            st.image(suggestion[3])
        with col3:
            st.subheader(suggestion[4])
            st.image(suggestion[5])
        with col4:
            st.subheader(suggestion[6])
            st.image(suggestion[7])
        with col5:
            st.subheader(suggestion[8])
            st.image(suggestion[9])



