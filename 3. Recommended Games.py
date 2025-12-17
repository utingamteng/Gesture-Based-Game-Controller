import streamlit as st

st.title("👾 :blue[Recommended] :red[Games]")
st.write("""It's important to know that not all games can be played using **:green[Mono]:red[Grip]**. Only games that can be played \
         using the fixed key bindings explained on \"❓ How to use **:green[Mono]:red[Grip]**?\" can be played using **:green[Mono]:red[Grip]**. \
         This app also support the controller only not the game. It means that the game cannot be displayed in this application as \
         most browser games have safety features preventing it to be displayed anywhere around here. Now back to the point!. These \
         are some games that i recommend to be played. There are actually lots of games that can be played using this application, but
         i will be only displaying three
         """)

with st.expander("🗿 Temple Run 2"):
    st.write("""[_Temple Run 2_](https://poki.com/id/g/temple-run-2) is an endless platformer runner games where you need to run from a beast after stealing
             the cursed idol. This game is engaing yet simple as it mainly uses left, right, up, and down key while the
             spacebar is barely used.""")
    
with st.expander("🦖 T-Rex Chrome Game"):
    st.write("""[This game](https://chromedino.com/) is also an endless platformer runner game that displayed during chrome internet \
             error. This simple game can also be accessed through a website so you don't need to cut of your wi-fi just to play the \
             game. This game also requires one key only to be played which is spacebar (or arrow up)
             """)

with st.expander("🔴 Red Ball 4"):
    st.write("""[_Red Ball 4_](https://poki.com/id/g/red-ball-4) is a story based adventure platformer game. In this game, you're controlling \
             a red ball through an adventure where ahead of you awaits bunch of obstacles and threats. This game can be played using only \
             up key, left key, and right key making it one of the perfect game to be played using this app
             """)
    
