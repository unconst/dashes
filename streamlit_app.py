import time
import streamlit as st
import bittensor as bt

st.set_page_config(
    page_title="Opentensor Dashboard",
    page_icon="𝜏",
    layout="wide",
)

sub = bt.subtensor()
st.title("Bittensor: Finney")
st.divider()

# Block metric.
block_metric = st.metric( label="Block", value=str(sub.get_current_block()) )

# # Streamlit loop.
# for i in range(100):
#     time.sleep(1)
#     sub = bt.subtensor()
#     block_metric.value = str( sub.get_current_block() )