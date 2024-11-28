import streamlit as st # type: ignore
from components.routes import navigation
import os
import pandas as pd
import glob

def extract_test_name(value):

    file_name_without_extension, _ = os.path.splitext(os.path.basename(value))
    return file_name_without_extension


def format_chat(db):
    message = ""
    for i in range(len(db)):
        message += db["type"][i] + ": " + db["content"][i] + "\n"
    return message


def increase_current():
    st.session_state.current += 1
    
def decrease_current():
    st.session_state.current -= 1

def reset_current():
    st.session_state.current = 1

tests = glob.glob("./static/results/*.csv")
users = ["Jose","Carmen", "Leo", "Miguel"]

navigation()
with open('./styles/global.css') as f:
    css = f.read()

st.markdown(f"""
        <style>
            {css}
        </style>""",
        unsafe_allow_html=True)

if 'current' not in st.session_state:
    st.session_state.current = 1

# st.sidebar.markdown("# Page 2 ❄️")

col1, col2, col3= st.columns([5,0.1,5],vertical_alignment="top")


col1.markdown("# Numeric")

eval_container = col1.container(border=False)

# eval = col1.form("numeric_evaluation")
option = eval_container.selectbox(
    "User",
    users,
)

def update_length():
    st.session_state.length += 1

@st.experimental_fragment()
def doc_selector():
    container = st.container()
    tag_container, doc_container = container.columns([1,3])
    tag_selection = tag_container.selectbox(
        "Tag",
        ("RagPT", "LangGraph"),
        key="Tag",
    )
    docs = [] if tag_selection == "RagPT" else tests
    doc_selection = doc_container.selectbox(
        "Doc",
        docs,
        format_func=extract_test_name,
        on_change=reset_current
    )

    db = []
    if doc_selection != None:
        db = pd.read_csv(doc_selection, sep=";", skiprows=1, names=["type","content"])
        container.text_area("Log",value=f"{format_chat(db[0:st.session_state.current+1])}", disabled=True)
    else:
        container.text_area("Log", disabled=True)

    
    criterias = ["Clarity", "Cohesion", "Helpfulness"]
    values = container.columns(len(criterias))
    for i in range(len(criterias)):
        values[i].selectbox(
            criterias[i],
            range(11)[1:],
            key=criterias[i],
    )
        
    container.text_area("Observation")

    

    button_left, space, counter, button_right  = container.columns([1,3, 1,1],vertical_alignment="center")
    button_right.button("Next", type="primary", disabled=st.session_state.current >= len(db)//2, use_container_width=True, on_click=increase_current)
    counter.markdown(f"""<p style="text-align: center">{st.session_state.current if len(db) > 0 else 0}/{len(db)//2}</div>""",
                    unsafe_allow_html=True)
    button_left.button("Back", disabled=st.session_state.current <= 1, use_container_width=True, on_click=decrease_current)

    return tag_selection, doc_selection, db

with eval_container:
    _, doc_selection, db = doc_selector()





col2.html(
            '''
                <div class="divider-vertical-line"></div>
                <style>
                    .divider-vertical-line {
                        border-left: 2px solid rgba(49, 51, 63, 0.2);
                        
                        height: 41rem;
                        display: flex;
                        width: 1px;
                    }
                </style>
            ''')

container = col3.container(border=True)
container.markdown("""## Rules

**Clarity:** 1-10\n
**Cohesion:** 1-10\n
**Helpfulness:** 1-10""")