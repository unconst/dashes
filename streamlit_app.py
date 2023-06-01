import time
import streamlit as st
import bittensor as bt
for i in range(100):
    time.sleep(1)
    sub = bt.subtensor()
    st.markdown("# Value of i is: {}".format( sub.get_current_block() ) )