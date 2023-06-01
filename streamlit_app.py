import time
import streamlit as st
import bittensor as bt

st.title("Bittensor: Finney")
st.set_page_config(
    page_title="Opentensor Dashboard",
    page_icon="𝜏",
    layout="wide",
)
st.divider()

# Streamlit loop.
placeholder = st.empty()

for i in range(100):
    with placeholder.container():
        metagraph = bt.metagraph( 1 )
        block_metric = st.metric( label="Block", value=str(metagraph.block.item()) )
        block_metric = st.metric( label="UIDs", value=str(metagraph.n.item()) )
        block_metric = st.metric( label="Unique Hotkeys", value=str(len(set(metagraph.hotkeys))) )
        block_metric = st.metric( label="Unique Coldkeys", value=str(len(set(metagraph.coldkeys))) )
        time.sleep( 6 )