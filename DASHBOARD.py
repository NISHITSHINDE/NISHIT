Last login: Wed Aug 19 22:37:50 on ttys000
maheshshinde@NISHIT ~ % >....                                                   
    if c2.button("Run Dynamic TTL Engine <0001f9f9>", use_container_width=True): 
        clean_cache()
        st.rerun()

    st.subheader("📊 Popularity & Cache Hit Tracking")
    df = pd.DataFrame(
        list(st.session_state.popularity.items()),
        columns=["Item", "Request Count"]
    )
    st.bar_chart(df.set_index("Item"))

with col_right:
    st.subheader("🖥️ Cache Memory State (Redis Simulator)")
    if st.session_state.cache:
        st.json(st.session_state.cache)
    else:
        st.info("Cache is currently empty.")

    st.subheader("📋 System Activity Logs")
    for log in st.session_state.logs[:8]:
        st.text(log)
EOF
maheshshinde@NISHIT ~ % streamlit run app.py

  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.31.198:8501

  Help agents write better Streamlit apps?
  Install the official Streamlit skills by running streamlit skills in your terminal.

  For better performance, install the Watchdog module:

  $ xcode-select --install
  $ pip install watchdog
            

