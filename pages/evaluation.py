import streamlit as st # type: ignore
from components.routes import navigation

navigation()

st.markdown("""
        <style>
            [data-testid="stMainBlockContainer"] {
                width:100%;
                max-width: 70rem;
            }
            h1, h2 {
                padding-top: 0;
            }
        </style>""",
        unsafe_allow_html=True)

# st.sidebar.markdown("# Page 2 ❄️")

col1, col2, col3= st.columns([5,0.1,5],vertical_alignment="top")


col1.markdown("# Numeric")

eval_container = col1.container(border=False)

# eval = col1.form("numeric_evaluation")
option = eval_container.selectbox(
    "User",
    ("Email", "Home phone", "Mobile phone"),
)
tag_container, doc_container = eval_container.columns([1,3])
tag_selection = tag_container.selectbox(
    "Tag",
    ("RagPT", "LangGraph"),
    key="Tag",
)
docs = ("RagPT-2024") if tag_selection == "RagPT" else ("LangGraph2024")
doc_selection = doc_container.selectbox(
    "Doc",
    docs
)

eval_container.text_area("Log")

criterias = ["Clarity", "Cohesion", "Helpfulness"]
values = eval_container.columns(len(criterias))
for i in range(len(criterias)):
    values[i].selectbox(
        criterias[i],
        range(11)[1:],
        key=criterias[i],
)
    
eval_container.text_area("Observation")

button_left, space, counter, button_right  = eval_container.columns([1,3, 1,1],vertical_alignment="center")
button_right.button("Next", type="primary", use_container_width=True)
counter.markdown("""<p style="text-align: center">1/10</div>""",
                unsafe_allow_html=True)
button_left.button("Back", use_container_width=True)


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