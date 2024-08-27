import streamlit as st
from streamlit.components.v1 import html

# Add a tracking token
html('<script async defer data-website-id="<your_website_id>" src="https://analytics.gnps2.org/umami.js"></script>', width=0, height=0)

# Write the page label
st.set_page_config(
    page_title="Homepage",
    page_icon="👋",
)

# Getting a text field
st.write("Welcome to the homepage!")