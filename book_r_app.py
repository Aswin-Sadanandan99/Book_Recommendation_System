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

selected_movie = st.selectbox('Type or select Books',book_list)
if st.button('Show Recommendation'):
    st.write('These are the Books Recommended as per your Preference')
    suggestion = recommender(selected_movie)
    col1, div1, col2, div2, col3, div3, col4, div4, col5 = st.columns([1,0.02,1,0.02,1,0.02,1,0.02,1])
    with col1:
        st.subheader(suggestion[0])
        st.image(suggestion[1])
    with div1:
        st.markdown('|')
    with col2:
        st.subheader(suggestion[2])
        st.image(suggestion[3])
    with div2:
        st.markdown('|')
    with col3:
        st.subheader(suggestion[4])
        st.image(suggestion[5])
    with div3:
        st.markdown('|')
    with col4:
        st.subheader(suggestion[6])
        st.image(suggestion[7])
    with div4:
        st.markdown('|')
    with col5:
        st.subheader(suggestion[8])
         st.image(suggestion[9])
