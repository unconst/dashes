import time
import streamlit as st
import bittensor as bt

sub = bt.subtensor()
st.title("Bittensor: Finney")
st.divider()

# Block metric.
block_metric = st.metric( label="Block", value=str(sub.get_current_block()) )

# Streamlit loop.
for i in range(100):
    time.sleep(1)
    sub = bt.subtensor()
    block_metric.value = str( sub.get_current_block() )