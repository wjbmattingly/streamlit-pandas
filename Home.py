import streamlit as st
import pandas as pd
import streamlit_pandas as sp

@st.cache_data
def load_data():
    df = pd.read_csv(file)
    return df

file = "./data/titanic.csv"
df = load_data()
create_data = {"Name": "text",
                "Sex": "multiselect",
                "Embarked": "multiselect",
                "Ticket": "text",
                "Pclass": "multiselect"}

all_widgets = sp.create_widgets(df, create_data, ignore_columns=["PassengerId"])
res = sp.filter_df(df, all_widgets)
st.title("Streamlit AutoPandas")
st.header("Original DataFrame")
st.write(df)

st.header("Result DataFrame")
st.write(res)
