import streamlit as st

st.title("Thanks for using **:green[Mono]:red[Grip]**!!! ❤️‍🔥")
st.write("We're really hope that you have a great experience with **:green[Mono]:red[Grip]** despite it major limitations. \
         I would also like to thank my colleagues for helping me on developing this application. Without their help, i might \
         not be able to develop such AI powered application. We also like to thank you for using **:green[Mono]:red[Grip]**! \
         In the future, we might as well improve this application in terms of flexibility, increased number of suuported keys \
         and even develop our own games")

tab1, tab2, tab3 = st.tabs([
    "💻 Justin Christian Woeryadi",
    "🎨 Muhammad Aurelio Al Ghazali",
    "📃 Raditya Arya Pradipta"
])

with tab1:
    st.write("An AI student of Binus University with great practical experience in Machine Learning and AI. Having a strong interest \
             in Game Development and actively contribute in organizations, competitions, and other experiences. Contribute in \
             application idea, data preparation and preprocessing, model training, and game integration.")

with tab2:
    st.write("An AI student of Binus University with great practical experience in Game Development especially involving Unity \
             engine. Having an excellent skills in creative things such as art and design. Contribute in application UI design, \
             application name idea, and application logo.")

with tab3:
    st.write("An AI student of Binus University with great practical experience in animating using blender, adobe, and roblox \
             studio. Having an experience in animation based content development and stock trading. Contribute in model research \
             that is necessary for deciding which model to be used for the AI.")