import streamlit as st

# Set up session state variables
if "ten_x" not in st.session_state:
    # ten_x mode changes our buttons to increment and decrement by 10 instead of by 1
    st.session_state.ten_x = 0

if "hundred_x" not in st.session_state:
    st.session_state.hundred_x = 0

if "count" not in st.session_state:
    st.session_state.count = 0


# Set up callbacks for inputs
def increment():
    if st.session_state.ten_x:
        st.session_state.count += 10
    elif st.session_state.hundred_x:
        st.session_state.count += 100
    else:
        st.session_state.count += 1


def decrement():
    if st.session_state.ten_x:
        st.session_state.count -= 10
    elif st.session_state.hundred_x:
        st.session_state.count -= 100
    else:
        st.session_state.count -= 1
    if st.session_state.count < 0:
        # Minimum count value is zero
        st.session_state.count = 0


# Write to page
with st.expander("Options") as options:
    # The key of the checkbox (ten_x) will automatically be added to the session state
    st.checkbox("10x mode", key="ten_x", value=st.session_state.ten_x)
    st.checkbox("100x mode", key="hundred_x", value=st.session_state.hundred_x)
    

st.write(f"Total count is {st.session_state.count}")    

st.button(
    f"plus {'10' if st.session_state.ten_x else '100' if st.session_state.hundred_x else '1'}",
    key="increment",
    on_click=increment,
)
st.button(
    f"minus {'10' if st.session_state.ten_x else '100' if st.session_state.hundred_x else '1'}",
    key="decrement",
    on_click=decrement,
)
