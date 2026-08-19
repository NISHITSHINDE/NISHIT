import streamlit as st
import pandas as pd

st.set_page_config(page_title="Team Apexx - Smart Cache Dashboard", layout="wide")

DATABASE = {
    "toy_car": "Red Race Car Data",
    "blocks": "Lego Set Data",
    "puzzle": "100-piece Puzzle Data"
}

if "cache" not in st.session_state:
    st.session_state.cache = {}
if "popularity" not in st.session_state:
    st.session_state.popularity = {"toy_car": 0, "blocks": 0, "puzzle": 0}
if "cost_saved" not in st.session_state:
    st.session_state.cost_saved = 0.0
if "logs" not in st.session_state:
    st.session_state.logs = []

def request_item(item):
    if item in st.session_state.cache:
        st.session_state.popularity[item] += 1
        st.session_state.cost_saved += 0.05
        st.session_state.logs.insert(0, f"⚡ Quick Desk HIT: Handed over '{item}' instantly (Saved $0.05)")
    else:
        st.session_state.cache[item] = DATABASE[item]
        st.session_state.popularity[item] = 1
        st.session_state.logs.insert(0, f"🐢 Database MISS: Fetched '{item}' from closet into cache.")

def clean_cache():
    evicted = []
    for item, count in list(st.session_state.popularity.items()):
        if count < 2 and item in st.session_state.cache:
            st.session_state.cache.pop(item, None)
            evicted.append(item)
    if evicted:
        st.session_state.logs.insert(0, f"🧹 Dynamic TTL Evicted cold items: {', '.join(evicted)}")

st.title("⚡ Smart Cache Prototype Dashboard")
st.caption("Team Apexx Architecture Simulation")

m1, m2, m3 = st.columns(3)
m1.metric("Est. Database Cost Saved", f"${st.session_state.cost_saved:.2f}")
m2.metric("Items in Quick Desk Cache", len(st.session_state.cache))
m3.metric("Total Requests Handled", sum(st.session_state.popularity.values()))

st.markdown("---")

col_left, col_right = st.columns([1, 1])

with col_left:
    st.subheader("📥 Request Simulator")
    selected_item = st.selectbox("Select Item to Request:", list(DATABASE.keys()))
    
    c1, c2 = st.columns(2)
    if c1.button("Request Item", use_container_width=True):
        request_item(selected_item)
        st.rerun()
        
    if c2.button("Run Dynamic TTL Engine 🧹", use_container_width=True):
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
