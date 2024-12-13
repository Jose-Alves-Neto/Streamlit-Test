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
        message += db[i][0] + ": " + db[i][1] + "\n"
    return message


def increase_current():
    st.session_state.current += 2
    
def decrease_current():
    st.session_state.current -= 2

def reset_current():
    st.session_state.current = 0

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
    st.session_state.current = 0



col1, col2, col3= st.columns([5,0.1,5],vertical_alignment="top")


col1.markdown("# Numeric")

eval_container = col1.container(border=False)

@st.experimental_fragment()
def doc_selector():
    container = st.container()
    user = container.selectbox(
        "User",
        users,
    )
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
        db = pd.read_csv(doc_selection, sep=",", skiprows=1, names=["type","content"])
        container.text_area("Log",value=f"{format_chat(db.to_numpy()[st.session_state.current:st.session_state.current+2])}", disabled=True)
    else:
        container.text_area("Log", disabled=True)

    path = f"./static/evaluation/{tag_selection.lower()}/eval.csv"
    if (os.path.isfile(path)):
        notes = pd.read_csv(path, sep=";")

    criterias = ["Clarity", "Accuracy", "AT", "CR", "SC"]
    criteria = {}
    values = container.columns(len(criterias))

    for i in range(len(criterias)):
        criteria[criterias[i]] = values[i].selectbox(
            criterias[i],
            range(11)[1:],
            index=None,
            key=criterias[i],
        )
        
    container.text_area("Observation")

    def on_save(id, test, criteria, message, user):
        res = pd.DataFrame(data={"id":id, "test":test, "message":[message[1]], "user":user})

        for name, value in criteria.items():
            res[name] = [value]

        if (not os.path.isfile(path)):
            res.to_csv(path, sep=";", index=False)
        else:
            res.merge(notes,how="outer").drop_duplicates(["user","id","test"],keep='last').to_csv(path, sep=";", index=False)

        st.toast("Saved sucessfully!")
        return

    _, _, _, counter  = container.columns([1,3, 1,1],vertical_alignment="center")
    button_left, _, button_save, button_right  = container.columns([1,3, 1,1],vertical_alignment="center")
    button_right.button("Next", type="primary", disabled=st.session_state.current >= len(db) - 2, use_container_width=True, on_click=increase_current)
    button_save.button("Save",use_container_width=True, on_click=lambda: on_save((st.session_state.current//2) + 1, extract_test_name(doc_selection), criteria, db.to_numpy()[st.session_state.current+1],user))
    counter.markdown(f"""<p style="text-align: center">{(st.session_state.current//2) + 1 if len(db) > 0 else 0}/{len(db)//2}</div>""",
                    unsafe_allow_html=True)
    button_left.button("Back", disabled=st.session_state.current+2//2 <= 1, use_container_width=True, on_click=decrease_current)

    return tag_selection, doc_selection, db, criteria

with eval_container:
    _, doc_selection, db, criteria = doc_selector()







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

**Clarity (CL):** The response is clear, direct, and easily understandable, without ambiguities.\n
**Precision_and_Accuracy(PA)**:The response is accurate, error-free, and demonstrates full mastery of the subject.\n
**Appropriate Tone(AT):** The response adopts an empathetic and professional tone, suitable for the context.\n
**Context Relevance (CR):** The  response is fully relevant to the user's intent and context, directly addressing the request without adding unnecessary or out-of-scope information.\n
**Service Context (SC):** The response is appropriate for the service context, keeping the conversation in the context of updating the shipping address""")