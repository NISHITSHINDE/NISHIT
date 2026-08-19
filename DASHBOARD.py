Last login: Wed Aug 19 22:19:23 on ttys000
nishitshinde@NISHIT ~ % pip3 install streamlit pandas

Collecting streamlit
  Downloading streamlit-1.61.1-py3-none-any.whl.metadata (10 kB)
Collecting pandas
  Downloading pandas-3.0.5-cp313-cp313-macosx_10_13_x86_64.whl.metadata (79 kB)
Collecting altair!=5.4.0,!=5.4.1,<7,>=5.0.0 (from streamlit)
  Downloading altair-6.2.2-py3-none-any.whl.metadata (11 kB)
Collecting blinker<2,>=1.5.0 (from streamlit)
  Downloading blinker-1.9.0-py3-none-any.whl.metadata (1.6 kB)
Collecting click<9,>=7.0 (from streamlit)
  Downloading click-8.4.2-py3-none-any.whl.metadata (2.6 kB)
Collecting numpy<3,>=1.23 (from streamlit)
  Downloading numpy-2.5.2-cp313-cp313-macosx_10_13_x86_64.whl.metadata (6.6 kB)
Collecting packaging>=20 (from streamlit)
  Downloading packaging-26.3-py3-none-any.whl.metadata (3.5 kB)
Collecting pillow<13,>=7.1.0 (from streamlit)
  Downloading pillow-12.3.0-cp313-cp313-macosx_10_13_x86_64.whl.metadata (9.1 kB)
Collecting pydeck<1,>=0.8.b4 (from streamlit)
  Downloading pydeck-0.9.3-py2.py3-none-any.whl.metadata (4.2 kB)
Collecting protobuf<8,>=5.26.1 (from streamlit)
  Downloading protobuf-7.35.1-cp310-abi3-macosx_10_9_universal2.whl.metadata (595 bytes)
Collecting pyarrow<25,>=7.0 (from streamlit)
  Downloading pyarrow-24.0.0-cp313-cp313-macosx_12_0_x86_64.whl.metadata (3.0 kB)
Collecting requests<3,>=2.27 (from streamlit)
  Downloading requests-2.34.2-py3-none-any.whl.metadata (4.8 kB)
Collecting tenacity<10,>=8.1.0 (from streamlit)
  Downloading tenacity-9.1.4-py3-none-any.whl.metadata (1.2 kB)
Collecting toml<2,>=0.10.1 (from streamlit)
  Downloading toml-0.10.2-py2.py3-none-any.whl.metadata (7.1 kB)
Collecting typing-extensions<5,>=4.10.0 (from streamlit)
  Downloading typing_extensions-4.16.0-py3-none-any.whl.metadata (3.3 kB)
Collecting starlette<1.4.0,>=0.46.0 (from streamlit)
  Downloading starlette-1.3.1-py3-none-any.whl.metadata (6.4 kB)
Collecting uvicorn<1,>=0.30.0 (from streamlit)
  Downloading uvicorn-0.52.4-py3-none-any.whl.metadata (6.6 kB)
Collecting httptools<1,>=0.6.3 (from streamlit)
  Downloading httptools-0.8.0-cp313-cp313-macosx_10_13_universal2.whl.metadata (3.5 kB)
Collecting anyio<5,>=4.0.0 (from streamlit)
  Downloading anyio-4.14.2-py3-none-any.whl.metadata (4.6 kB)
Collecting python-multipart<1,>=0.0.10 (from streamlit)
  Downloading python_multipart-0.0.32-py3-none-any.whl.metadata (2.1 kB)
Collecting websockets<17,>=12.0.0 (from streamlit)
  Downloading websockets-16.1.1-cp313-cp313-macosx_10_13_x86_64.whl.metadata (6.8 kB)
Collecting itsdangerous<3,>=2.1.2 (from streamlit)
  Downloading itsdangerous-2.2.0-py3-none-any.whl.metadata (1.9 kB)
Collecting python-dateutil>=2.8.2 (from pandas)
  Downloading python_dateutil-2.9.0.post0-py2.py3-none-any.whl.metadata (8.4 kB)
Collecting jinja2 (from altair!=5.4.0,!=5.4.1,<7,>=5.0.0->streamlit)
  Downloading jinja2-3.1.6-py3-none-any.whl.metadata (2.9 kB)
Collecting jsonschema>=3.0 (from altair!=5.4.0,!=5.4.1,<7,>=5.0.0->streamlit)
  Downloading jsonschema-4.26.0-py3-none-any.whl.metadata (7.6 kB)
Collecting narwhals>=2.4.0 (from altair!=5.4.0,!=5.4.1,<7,>=5.0.0->streamlit)
  Downloading narwhals-2.24.0-py3-none-any.whl.metadata (15 kB)
Collecting idna>=2.8 (from anyio<5,>=4.0.0->streamlit)
  Downloading idna-3.19-py3-none-any.whl.metadata (9.2 kB)
Collecting six>=1.5 (from python-dateutil>=2.8.2->pandas)
  Downloading six-1.17.0-py2.py3-none-any.whl.metadata (1.7 kB)
Collecting charset_normalizer<4,>=2 (from requests<3,>=2.27->streamlit)
  Downloading charset_normalizer-3.5.1-cp313-cp313-macosx_10_13_universal2.whl.metadata (45 kB)
Collecting urllib3<3,>=1.26 (from requests<3,>=2.27->streamlit)
  Downloading urllib3-2.7.0-py3-none-any.whl.metadata (6.9 kB)
Collecting certifi>=2023.5.7 (from requests<3,>=2.27->streamlit)
  Downloading certifi-2026.7.22-py3-none-any.whl.metadata (2.5 kB)
Collecting h11>=0.8 (from uvicorn<1,>=0.30.0->streamlit)
  Downloading h11-0.16.0-py3-none-any.whl.metadata (8.3 kB)
Collecting MarkupSafe>=2.0 (from jinja2->altair!=5.4.0,!=5.4.1,<7,>=5.0.0->streamlit)
  Downloading markupsafe-3.0.3-cp313-cp313-macosx_10_13_x86_64.whl.metadata (2.7 kB)
Collecting attrs>=22.2.0 (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<7,>=5.0.0->streamlit)
  Downloading attrs-26.1.0-py3-none-any.whl.metadata (8.8 kB)
Collecting jsonschema-specifications>=2023.03.6 (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<7,>=5.0.0->streamlit)
  Downloading jsonschema_specifications-2025.9.1-py3-none-any.whl.metadata (2.9 kB)
Collecting referencing>=0.28.4 (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<7,>=5.0.0->streamlit)
  Downloading referencing-0.37.0-py3-none-any.whl.metadata (2.8 kB)
Collecting rpds-py>=0.25.0 (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<7,>=5.0.0->streamlit)
  Downloading rpds_py-2026.6.3-cp313-cp313-macosx_10_12_x86_64.whl.metadata (4.1 kB)
Downloading streamlit-1.61.1-py3-none-any.whl (10.5 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 10.5/10.5 MB 4.1 MB/s eta 0:00:00
Downloading pandas-3.0.5-cp313-cp313-macosx_10_13_x86_64.whl (10.4 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 10.4/10.4 MB 3.4 MB/s eta 0:00:00
Downloading altair-6.2.2-py3-none-any.whl (797 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 797.6/797.6 kB 2.8 MB/s eta 0:00:00
Downloading anyio-4.14.2-py3-none-any.whl (125 kB)
Downloading blinker-1.9.0-py3-none-any.whl (8.5 kB)
Downloading click-8.4.2-py3-none-any.whl (119 kB)
Downloading httptools-0.8.0-cp313-cp313-macosx_10_13_universal2.whl (205 kB)
Downloading itsdangerous-2.2.0-py3-none-any.whl (16 kB)
Downloading numpy-2.5.2-cp313-cp313-macosx_10_13_x86_64.whl (16.9 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 16.9/16.9 MB 3.4 MB/s eta 0:00:00
Downloading packaging-26.3-py3-none-any.whl (129 kB)
Downloading pillow-12.3.0-cp313-cp313-macosx_10_13_x86_64.whl (5.3 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 5.3/5.3 MB 1.8 MB/s eta 0:00:00
Downloading protobuf-7.35.1-cp310-abi3-macosx_10_9_universal2.whl (433 kB)
Downloading pyarrow-24.0.0-cp313-cp313-macosx_12_0_x86_64.whl (36.7 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 36.7/36.7 MB 2.0 MB/s eta 0:00:00
Downloading pydeck-0.9.3-py2.py3-none-any.whl (11.4 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 11.4/11.4 MB 3.3 MB/s eta 0:00:00
Downloading python_dateutil-2.9.0.post0-py2.py3-none-any.whl (229 kB)
Downloading python_multipart-0.0.32-py3-none-any.whl (30 kB)
Downloading requests-2.34.2-py3-none-any.whl (73 kB)
Downloading starlette-1.3.1-py3-none-any.whl (73 kB)
Downloading tenacity-9.1.4-py3-none-any.whl (28 kB)
Downloading toml-0.10.2-py2.py3-none-any.whl (16 kB)
Downloading typing_extensions-4.16.0-py3-none-any.whl (45 kB)
Downloading uvicorn-0.52.4-py3-none-any.whl (79 kB)
Downloading websockets-16.1.1-cp313-cp313-macosx_10_13_x86_64.whl (177 kB)
Downloading certifi-2026.7.22-py3-none-any.whl (136 kB)
Downloading charset_normalizer-3.5.1-cp313-cp313-macosx_10_13_universal2.whl (340 kB)
Downloading h11-0.16.0-py3-none-any.whl (37 kB)
Downloading idna-3.19-py3-none-any.whl (68 kB)
Downloading jinja2-3.1.6-py3-none-any.whl (134 kB)
Downloading jsonschema-4.26.0-py3-none-any.whl (90 kB)
Downloading narwhals-2.24.0-py3-none-any.whl (461 kB)
Downloading six-1.17.0-py2.py3-none-any.whl (11 kB)
Downloading urllib3-2.7.0-py3-none-any.whl (131 kB)
Downloading attrs-26.1.0-py3-none-any.whl (67 kB)
Downloading jsonschema_specifications-2025.9.1-py3-none-any.whl (18 kB)
Downloading markupsafe-3.0.3-cp313-cp313-macosx_10_13_x86_64.whl (11 kB)
Downloading referencing-0.37.0-py3-none-any.whl (26 kB)
Downloading rpds_py-2026.6.3-cp313-cp313-macosx_10_12_x86_64.whl (343 kB)
Installing collected packages: websockets, urllib3, typing-extensions, toml, tenacity, six, rpds-py, python-multipart, pyarrow, protobuf, pillow, packaging, numpy, narwhals, MarkupSafe, itsdangerous, idna, httptools, h11, click, charset_normalizer, certifi, blinker, attrs, uvicorn, requests, referencing, python-dateutil, jinja2, anyio, starlette, pydeck, pandas, jsonschema-specifications, jsonschema, altair, streamlit
Successfully installed MarkupSafe-3.0.3 altair-6.2.2 anyio-4.14.2 attrs-26.1.0 blinker-1.9.0 certifi-2026.7.22 charset_normalizer-3.5.1 click-8.4.2 h11-0.16.0 httptools-0.8.0 idna-3.19 itsdangerous-2.2.0 jinja2-3.1.6 jsonschema-4.26.0 jsonschema-specifications-2025.9.1 narwhals-2.24.0 numpy-2.5.2 packaging-26.3 pandas-3.0.5 pillow-12.3.0 protobuf-7.35.1 pyarrow-24.0.0 pydeck-0.9.3 python-dateutil-2.9.0.post0 python-multipart-0.0.32 referencing-0.37.0 requests-2.34.2 rpds-py-2026.6.3 six-1.17.0 starlette-1.3.1 streamlit-1.61.1 tenacity-9.1.4 toml-0.10.2 typing-extensions-4.16.0 urllib3-2.7.0 uvicorn-0.52.4 websockets-16.1.1

[notice] A new release of pip is available: 24.3.1 -> 26.2.1
[notice] To update, run: pip3 install --upgrade pip
nishitshinde@NISHIT ~ % 
nishitshinde@NISHIT ~ % >....                                                            
def clean_cache():
    evicted = []
    for item, count in list(st.session_state.popularity.items()):
        if count < 2 and item in st.session_state.cache:
            st.session_state.cache.pop(item, None)
            evicted.append(item)
    if evicted:
        st.session_state.logs.insert(0, f"<0001f9f9> Dynamic TTL Evicted cold items: {', '.join(evicted)}")

# UI Layout
st.title("⚡ Smart Cache Prototype Dashboard")
st.caption("Team Apexx Architecture Simulation")

# Metrics Cards
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
nishitshinde@NISHIT ~ % streamlit run app.py

      👋 Welcome to Streamlit!

      If you'd like to receive helpful onboarding emails, news, offers, promotions,
      and the occasional swag, please enter your email address below. Otherwise,
      leave this field blank.

      Email: itsnishitshinde@gmail.com

  You can find our privacy policy at https://streamlit.io/privacy-policy

  Summary:
  - This open source library collects usage statistics.
  - We cannot see and do not store information contained inside Streamlit apps,
    such as text, charts, images, etc.
  - Telemetry data is stored in servers in the United States.
  - If you'd like to opt out, add the following to ~/.streamlit/config.toml,
    creating that file if necessary:

    [browser]
    gatherUsageStats = false

2026-08-19 22:40:28.965 Uvicorn server started on :::8501

  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.31.198:8501

  Help agents write better Streamlit apps?
  Install the official Streamlit skills by running streamlit skills in your terminal.

  For better performance, install the Watchdog module:

  $ xcode-select --install
  $ pip install watchdog
            

