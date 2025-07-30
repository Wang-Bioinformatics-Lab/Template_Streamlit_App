import streamlit as st
from streamlit.components.v1 import html
import subprocess


def get_git_short_rev():
    try:
        with open('.git/logs/HEAD', 'r') as f:
            last_line = f.readlines()[-1]
            hash_val = last_line.split()[1]
        return hash_val[:7]
    except Exception:
        return ".git/ not found"


# Add a tracking token
html('<script async defer data-website-id="<your_website_id>" src="https://analytics.gnps2.org/umami.js"></script>', width=0, height=0)


# TODO: Bump version
app_version = "2025-07-17"
try:
    git_hash = get_git_short_rev()
except:
    git_hash = "unknown"
repo_link = "https://github.com/YOUR-USER/YOUR-REPO"


# Write the page label
st.set_page_config(
    page_title="Homepage",
    page_icon="👋",
    menu_items={"About": (f"**App Version**: {app_version} | "
                          f"[**Git Hash**: {git_hash}]({repo_link}/commit/{git_hash})")},
)

# Getting a text field
st.write("Welcome to the homepage!")
