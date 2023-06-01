import time
import streamlit as st
import bittensor as bt
from PIL import Image

# Set up page.
image = Image.open('assets/favicon.ico')
st.image(image, caption='Page favicon')
st.set_page_config(
    page_title = "Opentensor Dashboards",
    page_icon = st.image(image, caption='Page favicon'),
    layout = "wide",
)

for i in range(100):
    time.sleep(1)
    sub = bt.subtensor()
    st.markdown("# Value of i is: {}".format( sub.get_current_block() ) )