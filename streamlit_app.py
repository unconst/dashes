import time
import streamlit as st
import bittensor as bt
from bokeh.plotting import figure

st.title("Bittensor: Finney")
st.divider()

# Streamlit loop.
placeholder = st.empty()

for i in range(100):
    with placeholder.container():
        metagraph = bt.metagraph( 1 )
        col1, col2, col3, col4 = st.columns(4)
        block_metric = col1.metric( label="Block", value=str(metagraph.block.item()) )
        block_metric = col2.metric( label="UIDs", value=str(metagraph.n.item()) )
        block_metric = col3.metric( label="Unique Hotkeys", value=str(len(set(metagraph.hotkeys))) )
        block_metric = col4.metric( label="Unique Coldkeys", value=str(len(set(metagraph.coldkeys))) )
        block_metric = col1.metric( label="Unique Endpoints", value=str(len(set([a.ip for a in metagraph.axons]))) )
        time.sleep( 6 )

        x = [1, 2, 3, 4, 5]
        y = [6, 7, 2, 4, 5]
        p = figure(
            title='simple line example',
            x_axis_label='x',
            y_axis_label='y')
        p.line(x, y, legend_label='Trend', line_width=2)
        st.bokeh_chart(p, use_container_width=True)