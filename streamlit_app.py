import time
import streamlit as st
import bittensor as bt
import matplotlib.pyplot as plt
import numpy as np
import queue

st.title("Bittensor: Finney")
st.divider()

# Streamlit loop.
placeholder = st.empty()

# Metagraph history.
history = queue.Queue( 10 )

for i in range(100):
    with placeholder.container():
        metagraph = bt.metagraph( 1 )
        col1, col2, col3, col4 = st.columns(4)
        block_metric = col1.metric( label="Block", value=str(metagraph.block.item()) )
        block_metric = col2.metric( label="UIDs", value=str(metagraph.n.item()) )
        block_metric = col3.metric( label="Unique Hotkeys", value=str(len(set(metagraph.hotkeys))) )
        block_metric = col4.metric( label="Unique Coldkeys", value=str(len(set(metagraph.coldkeys))) )
        block_metric = col1.metric( label="Unique Endpoints", value=str(len(set([a.ip for a in metagraph.axons]))) )

        arr = np.random.normal(1, 1, size=100)
        fig, ax = plt.subplots()
        ax.hist(arr, bins=20)
        st.pyplot( fig )

        time.sleep( 6 )
