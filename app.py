import streamlit as st # type: ignore
from components.routes import navigation

navigation()

st.write("Hello world")

add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)

left_column, right_column = st.columns(2)
# You can use a column just like st.sidebar:
left_column.button('Press me!')

# Or even better, call Streamlit functions inside a "with" block:
with right_column:
    chosen = st.radio(
        'Sorting hat',
        ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
    st.write(f"You are in {chosen} house!")


st.markdown("# Main page 🎈")
st.sidebar.markdown("# Main page 🎈")

st.sidebar.page_link(".\pages\evaluation.py",label="Mame")

if 'result' not in st.session_state:
    st.session_state.result = 0

# No argument in the callback; current value to be added is grabbed directly from session state
def my_callback():
    # Get submitted value
    temperature = st.session_state.temperature
    # Append string to key of widget
    st.session_state.my_key =  st.session_state.my_key + str(temperature)
    # Add value to non-widget key in session state
    st.session_state.result += temperature


with st.form("foo"):
    st.text_area("label", key="my_key")
    st.markdown(f'#### The total temperature is {st.session_state.result:.2f}.')
    temp = st.slider(
        "Temperature",
        min_value=0.0,
        max_value=100.0,
        value=1.0,
        key='temperature'
    )

    # Option 1:
    submit = st.form_submit_button(
        "compute",
        on_click=my_callback
    )