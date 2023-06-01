import time
import streamlit as st
import bittensor as bt
import matplotlib.pyplot as plt
import numpy as np
import queue

st.title("Bittensor: Finney Subnet 1")
st.divider()

# Streamlit loop.
placeholder = st.empty()

# Metagraph history.
metagraph = bt.metagraph( 1 )
history = [ metagraph ]

for i in range(100):
    with placeholder.container():

        # Sync metagraph and add it to history.
        try:
            history.append( bt.metagraph( 1 ) )
        except:
            time.sleep( 3 )
            continue

        # Build items.
        col1, col2, col3, col4 = st.columns(4)
        col1.metric( label="Block", value = history[-1].block.item(), delta = history[-1].block.item() - history[0].block.item() )
        col2.metric( label="UIDs", value = history[-1].n.item(), delta = history[-1].n.item() - history[0].n.item() )
        col3.metric( label="Unique Coldkeys", value = len(set(history[-1].coldkeys)), delta = len(set(history[-1].coldkeys)) - len(set(history[0].coldkeys)) ) 
        col4.metric( label="Unique Endpoints", value = len(set([a.ip for a in history[-1].axons])), delta = len(set([a.ip for a in history[-1].axons])) )

        # Registrations
        st.divider()
        st.header('Registrations')
        scol1.metric( label="Total", value = history[-1].S.max().item(), delta = history[-1].S.max().item() - history[0].S.max().item() )


        # Stake
        st.divider()
        st.header('Stake')
        scol1, scol2, scol3 = st.columns(3)
        scol1.metric( label="Max", value = history[-1].S.max().item(), delta = history[-1].S.max().item() - history[0].S.max().item() )
        scol2.metric( label="Mean", value = history[-1].S.mean().item(), delta = history[-1].S.mean().item() - history[0].S.mean().item() )
        scol3.metric( label="std", value = history[-1].S.std().item(), delta = history[-1].S.std().item() - history[0].S.std().item() )
        sarr = history[-1].S.tolist()
        sfig, sax = plt.subplots()
        sax.hist( sarr, bins = 50 )
        sax.set_title('Stake')
        st.pyplot( sfig )

        # Ranks
        st.divider()
        st.header('Ranks')
        rcol1, rcol2, rcol3 = st.columns(3)
        rcol1.metric( label="Max", value = history[-1].R.max().item(), delta = history[-1].R.max().item() - history[0].R.max().item() )
        rcol2.metric( label="Mean", value = history[-1].R.mean().item(), delta = history[-1].R.mean().item() - history[0].R.mean().item() )
        rcol3.metric( label="std", value = history[-1].R.std().item(), delta = history[-1].R.std().item() - history[0].R.std().item() )
        rarr = history[-1].R.tolist()
        rfig, rax = plt.subplots()
        rax.hist( rarr, bins = 50 )
        rax.set_title('Ranks')
        st.pyplot( rfig )

        # Trust
        st.divider()
        st.header('Trust')
        tcol1, tcol2, tcol3 = st.columns(3)
        tcol1.metric( label="Max", value = history[-1].T.max().item(), delta = history[-1].T.max().item() - history[0].T.max().item() )
        tcol2.metric( label="Mean", value = history[-1].T.mean().item(), delta = history[-1].T.mean().item() - history[0].T.mean().item() )
        tcol3.metric( label="std", value = history[-1].T.std().item(), delta = history[-1].T.std().item() - history[0].T.std().item() )
        tarr = history[-1].T.tolist()
        tfig, tax = plt.subplots()
        tax.hist( tarr, bins = 50 )
        tax.set_title('Trust')
        st.pyplot( tfig )

        # Consensus
        st.divider()
        st.header('Consensus')
        ccol1, ccol2, ccol3 = st.columns(3)
        ccol1.metric( label="Max", value = history[-1].C.max().item(), delta = history[-1].C.max().item() - history[0].C.max().item() )
        ccol2.metric( label="Mean", value = history[-1].C.mean().item(), delta = history[-1].C.mean().item() - history[0].C.mean().item() )
        ccol3.metric( label="std", value = history[-1].C.std().item(), delta = history[-1].C.std().item() - history[0].C.std().item() )
        carr = history[-1].C.tolist()
        cfig, cax = plt.subplots()
        cax.hist( carr, bins = 50 )
        cax.set_title('Consensus')
        st.pyplot( cfig )

        # Incentives
        st.divider()
        st.header('Incentives')
        icol1, icol2, icol3 = st.columns(3)
        icol1.metric( label="Max", value = history[-1].I.max().item(), delta = history[-1].I.max().item() - history[0].I.max().item() )
        icol2.metric( label="Mean", value = history[-1].I.mean().item(), delta = history[-1].I.mean().item() - history[0].I.mean().item() )
        icol3.metric( label="std", value = history[-1].I.std().item(), delta = history[-1].I.std().item() - history[0].I.std().item() )
        iarr = history[-1].I.tolist()
        ifig, iax = plt.subplots()
        iax.hist( iarr, bins = 50 )
        iax.set_title('Incentives')
        st.pyplot( ifig )

        # Dividends
        st.divider()
        st.header('Dividends')
        dcol1, dcol2, dcol3 = st.columns(3)
        dcol1.metric( label="Max", value = history[-1].D.max().item(), delta = history[-1].D.max().item() - history[0].D.max().item() )
        dcol2.metric( label="Mean", value = history[-1].D.mean().item(), delta = history[-1].D.mean().item() - history[0].D.mean().item() )
        dcol3.metric( label="std", value = history[-1].D.std().item(), delta = history[-1].D.std().item() - history[0].D.std().item() )
        darr = history[-1].D.tolist()
        dfig, dax = plt.subplots()
        dax.hist( darr, bins = 50 )
        dax.set_title('Dividends')
        st.pyplot( dfig )

        # Emission
        st.divider()
        st.header('Emission')
        ecol1, ecol2, ecol3 = st.columns(3)
        ecol1.metric( label="Max", value = history[-1].E.max().item(), delta = history[-1].E.max().item() - history[0].E.max().item() )
        ecol2.metric( label="Mean", value = history[-1].E.mean().item(), delta = history[-1].E.mean().item() - history[0].E.mean().item() )
        ecol3.metric( label="std", value = history[-1].E.std().item(), delta = history[-1].E.std().item() - history[0].E.std().item() )
        earr = history[-1].E.tolist()
        efig, eax = plt.subplots()
        eax.hist( earr, bins = 50 )
        eax.set_title('Emission')
        st.pyplot( efig )

        time.sleep( 12 )
        plt.close( fig = rfig )
        plt.close( fig = tfig )
        plt.close( fig = cfig )
        plt.close( fig = ifig )
        plt.close( fig = dfig )
        plt.close( fig = efig )
