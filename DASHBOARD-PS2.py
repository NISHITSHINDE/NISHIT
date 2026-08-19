import streamlit as st

st.title("🛡️ Resource-Leak Guard Dashboard")
col1, col2, col3 = st.columns(3)
col1.metric(label="Total Scans", value="42")
col2.metric(label="Leaks Caught", value="3", delta="-2")
col3.metric(label="Pipeline Status", value="PASSED ✅")

st.divider()

st.subheader("🚨 Detected Open Leaks")

st.warning("File: `database.py` - Unclosed DB Connection at line 14")
st.code("# Suggested Patch\nwith get_db_connection() as conn:\n    conn.query()", language="python")

st.error("File: `file_writer.java` - Unclosed FileWriter at line 45")
st.code("// Suggested Patch\ntry (FileWriter fw = new FileWriter('file.txt')) {\n    fw.write();\n}", language="java")
