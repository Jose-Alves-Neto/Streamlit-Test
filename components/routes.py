import streamlit as st # type: ignore

routes = [{"multi": False,"url": "app.py", "label":"Home", "icon":""},
          {"multi": True, "label":"Evaluation", "icon":"", "links":[{"url": "./pages/evaluation.py", "label":"Numeric", "icon":""}]},
          {"multi": True, "label":"Docs", "icon":"", "links":[{"url": "./pages/evaluation.py", "label":"Numeric", "icon":""}]}]


def navigation():
    st.markdown("""
        <style>
            [data-testid="stPageLink"] a {
                padding: 0.75rem 0.5rem;
                border-radius: 0.5rem;
            }
            [data-testid="stExpander"] details {
                border-style: none;
                padding: 0px;
            }
            [data-testid="stExpander"] summary {
                padding: 0.75rem 0.5rem;
                border-radius: 0.5rem;
                background-color: rgba(151, 166, 195, 0.15);
                margin-bottom: 0.5rem;
            }
        </style>""",
        unsafe_allow_html=True
    )

    for i in range(len(routes)):
        route=routes[i]
        if route["multi"]:
            expander = st.sidebar.expander(route["label"])
            for j in range(len(route["links"])):
                link=route["links"][j]
                expander.page_link(link["url"], label=link["label"])
        else: 
            st.sidebar.page_link(route["url"], label=route["label"])
    st.sidebar.divider()
    return

