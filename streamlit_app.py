import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
st.title("Hello World Mr Pirawat Wareetanyarat Bonjour Yike")


placeholder = st.empty()
status = st.radio("Select an option", ["success", "error"], index=None)

if status == "success":
    placeholder.info("Hello again ! Awersome")
else:
    placeholder.success("Success")


st.info("Hello again! Awersome!")

st.success("This is cool!")

st.error("Error boi!")

st.warning("This is a warning")


st.header("Area Chart")
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.area_chart(chart_data)

df = pd.read_csv(
    "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv")

c = alt.Chart(df).mark_circle(size=60).encode(
    x='bill_length_mm',
    y='body_mass_g',
    color='species',

).interactive()

st.altair_chart(c, use_container_width=True)
