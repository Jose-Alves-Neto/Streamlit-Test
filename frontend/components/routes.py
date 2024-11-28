import streamlit as st # type: ignore

routes = [{"multi": False,"url": "app.py", "label":"Home", "icon":""},
          {"multi": True, "label":"Evaluation", "icon":"", "links":[{"url": "./pages/evaluation.py", "label":"Numeric", "icon":""}]},
          {"multi": True, "label":"Docs", "icon":"", "links":[{"url": "./pages/evaluation.py", "label":"Numeric", "icon":""}]}]

with open('./components/styles.css') as f:
    css = f.read()

def navigation():
    st.markdown(f'<style>{css}</style>',
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

