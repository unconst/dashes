import time
import streamlit as st
for i in range(100):
    time.sleep(1)
    st.markdown("# Value of i is: {}".format( i ) )