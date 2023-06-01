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
metagraph = bt.metagraph( 1 )
history = [ metagraph ]

for i in range(100):
    with placeholder.container():

        # Sync metagraph and add it to history.
        history.append( bt.metagraph( 1 ) )

        # Build items.
        col1, col2, col3, col4 = st.columns(4)
        block_metric = col1.metric( label="Block", value=str(history[-1].block.item()), delta = str(history[-1].block.item() - history[-2].block.item()) )
        block_metric = col2.metric( label="UIDs", value=str(history[-1].n.item()), delta = str(history[-1].n.item() - history[-2].n.item()) )
        block_metric = col3.metric( label="Unique Hotkeys", value=str(len(set(history[-1].hotkeys))), delta = str(len(set(history[-1].hotkeys))) - len(set(history[-2].hotkeys))) 
        block_metric = col4.metric( label="Unique Coldkeys", value=str(len(set(history[-1].coldkeys))), delta = str(len(set(history[-1].coldkeys))) - len(set(history[-2].coldkeys))) 
        block_metric = col1.metric( label="Unique Endpoints", value=str(len(set([a.ip for a in history[-1].axons]))), delta = str(len(set([a.ip for a in history[-1].axons]))) )

        # Build table.
        arr = np.random.normal(1, 1, size=100)
        fig, ax = plt.subplots()
        ax.hist(arr, bins=20)
        st.pyplot( fig )

        time.sleep( 6 )
