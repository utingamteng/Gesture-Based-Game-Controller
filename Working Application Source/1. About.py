import streamlit as st

ImagePath = "Assets/App Logo.jpg"

st.title("**:green[Mono]:red[Grip]** 👾🎮")
st.image(ImagePath, width=240)
st.subheader("**:blue[Hand] :green[Gesture Based] :rainbow[Game Controller]** 🖐️🤖")
st.write("Welcome to **:green[Mono]:red[Grip]** game controller! We're glad to see you here! Are you excited and curious about our \
         application? Don't worry! Everyone deserve a chance to know better about our application like **below** :D")

with st.expander("🤔 What is **:green[Mono]:red[Grip]**?"):
    st.write("""
    **:green[Mono]:red[Grip]** is an AI powered game controller that captures human hand gestures and \"translates\" them into
    keyboard inputs. To make it less complicated, it allows you to play games with your own hands :D
    """)

with st.expander("⚙️ How **:green[Mono]:red[Grip]** was made?"):
    st.write("""
    **:green[Mono]:red[Grip]** was built with the help of :blue[**Computer Vision**]. One of :blue[**Computer Vision's**] model
    used for this controller was YOLO (You Only Look Once) found by Joseph Redmon on 2016. This model was considered as one
    of the outstanding Object Detection model for it's amazing accuracy not only in classifying but specifying the location of
    certain objects found in one real time screen.
    """)

with st.expander("❓ How to use **:green[Mono]:red[Grip]**?"):
    st.write("""
    The main function of the app can be found in \"🎮 Controller\" menu. To use the app, you need to activate the controller in
    \"🔥 Activate Controller!\". Upon activating, it would take a while for the system to load. Once you see a real time
    camera view displayed, that means the system has already run! Finally, you can use the application by showing your hand
    gestures on the camera. You will see somekind of colored box which tells what gesture that the system see. There are a total
    of five gestures that can be made where each a translated as below :
    """)

    st.markdown("""
    - 👍 **Thumb**      ->   **Left Key** 
    - 🤙 **Pinky**      ->   **Right Key**
    - 🖐️ **High Five**  ->   **Up Key**
    - ✌️ **Two**        ->   **Down Key** 
    - 🤚 **Flat**       ->   **Spacebar**
    """)

with st.expander("💔 Limitations of **:green[Mono]:red[Grip]**"):
    st.write("""
    Sadly, **:green[Mono]:red[Grip]** has bunch of limitations 🥀
    """)
    st.markdown("""
    - It only support 5 gestures (5 specified keys) and the key bindings are fixed. It means that you can't decide which gesture\
        decide which key bindings.
    - Since the 5 keys are fixed and cannot be changed, you can only play games that are possible to be played using only those five \
        keys
    - It won't work well (unstable) if the lightning is too dark or too bright
    - It will never be fully independent. Meaning you will always need the help of keyboard, such as pressing "New Game", etc
        where the application alone doesn't support
    """)

with st.expander("📷 Demo Video of **:green[Mono]:red[Grip]** usage"):
    st.write("""
    Below is the example usage of **:green[Mono]:red[Grip]** game controller! I tested it to play _Temple Run 2_ since 5 keys
    is enough to play the game
    """)
    st.video("Assets/Demo Application Video.mp4")