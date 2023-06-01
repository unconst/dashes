import time
import streamlit as st
import bittensor as bt

sub = bt.subtensor()
st.title("Bittensor: Finney")
st.divider()
st.metric( label="Block", value=str(sub.get_current_block()) )



# st_block = st.markdown("Block: {}".format( sub.get_current_block() ) )
# for i in range(100):
#     time.sleep(1)
#     sub = bt.subtensor()
#     st_block.write( "Block: {}".format( sub.get_current_block() ) )