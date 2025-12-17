import streamlit as st

pg = st.navigation([
    st.Page("1. About.py", title = "📍 Main"),
    st.Page("2. App.py", title = "🎮 Controller"),
    st.Page("3. Recommended Games.py", title = "❤️‍🔥 Recommended Game"),
    st.Page("4. Credits.py", title = "🔥 Credits")
])
pg.run()