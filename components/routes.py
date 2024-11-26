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
                margin: 0;
            }
            [data-testid="stPageLink"] a p {
                font-weight: 400;
            }
            [data-testid="stPageLink"] {
            
                
            }
            [data-testid="stExpander"] details {
                border-style: none;
                padding: 0px;
            }
            [data-testid="stExpander"] details p {
                border-style: none;
                font-size: 1rem;
                font-weight: 400;
            }
            [data-testid="stExpanderDetails"] {
                padding: 1rem 0 1rem 1rem;
                border-left: solid 1px;
                margin: 0.5rem 0;
            }
            [data-testid="stExpander"] summary {
                padding: 0.75rem 0.5rem;
                border-radius: 0.5rem;
                background-color: transparent;
            }
            [data-testid="stExpander"] summary:hover {
                background-color: rgba(151, 166, 195, 0.15);
                color: rgb(49, 51, 63);
            }
            [data-testid="stExpanderToggleIcon"] {
                color: rgb(49, 51, 63);
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

