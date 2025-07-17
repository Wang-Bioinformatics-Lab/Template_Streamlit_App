import streamlit as st
from streamlit.components.v1 import html
import subprocess


def get_git_short_rev():
    try:
        return subprocess.check_output(['git', 'rev-parse', '--short', 'HEAD'], stderr=subprocess.DEVNULL).decode().strip()
    except subprocess.CalledProcessError:
        return ".git/ not found"


# Add a tracking token
html('<script async defer data-website-id="<your_website_id>" src="https://analytics.gnps2.org/umami.js"></script>', width=0, height=0)


# TODO: Bump version
app_version = "2025-07-17"
git_hash = get_git_short_rev()
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
