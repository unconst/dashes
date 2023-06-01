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
        block_metric = col1.metric( label="Block", value = history[-1].block.item(), delta = history[-1].block.item() - history[-2].block.item() )
        block_metric = col2.metric( label="UIDs", value = history[-1].n.item(), delta = history[-1].n.item() - history[-2].n.item() )
        block_metric = col3.metric( label="Unique Hotkeys", value = len(set(history[-1].hotkeys)), delta = len(set(history[-1].hotkeys)) - len(set(history[-2].hotkeys) ) )
        block_metric = col4.metric( label="Unique Coldkeys", value = len(set(history[-1].coldkeys)), delta = len(set(history[-1].coldkeys)) - len(set(history[-2].coldkeys)) ) 
        block_metric = col1.metric( label="Unique Endpoints", value = len(set([a.ip for a in history[-1].axons])), delta = len(set([a.ip for a in history[-1].axons])) )

        # Build table.
        col1, col2 = st.columns( 2 )

        # Ranks
        rarr = history[-1].R.tolist()
        rfig, rax = plt.subplots()
        rax.hist( rarr, bins = 20 )
        col1.pyplot( rfig )

        # Trust
        tarr = history[-1].T.tolist()
        tfig, tax = plt.subplots()
        tax.hist( tarr, bins=20)
        col2.pyplot( tfig )

        # Consensus
        carr = history[-1].T.tolist()
        cfig, cax = plt.subplots()
        cax.hist( carr, bins=20)
        col2.pyplot( cfig )

        # Incentives
        iarr = history[-1].T.tolist()
        ifig, iax = plt.subplots()
        iax.hist( iarr, bins=20)
        col2.pyplot( ifig )

        # Dividends
        darr = history[-1].T.tolist()
        dfig, dax = plt.subplots()
        dax.hist( darr, bins=20)
        col2.pyplot( dfig )

        # Emission
        earr = history[-1].T.tolist()
        efig, eax = plt.subplots()
        eax.hist( earr, bins=20)
        col2.pyplot( efig )

        time.sleep( 6 )
        plt.close( fig = rfig )
        plt.close( fig = tfig )
        plt.close( fig = cfig )
        plt.close( fig = ifig )
        plt.close( fig = dfig )
        plt.close( fig = efig )
