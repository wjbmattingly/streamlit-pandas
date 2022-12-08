![Streamlit pandas logo](https://github.com/wjbmattingly/streamlit-pandas/raw/main/images/streamlit-pandas-logo-blue.png)

# Streamlit Pandas
Streamlit Pandas is a component for the [Streamlit](https://streamlit.io/) library. It allows users to load a Pandas DataFrame and automatically generate Streamlit widgets in the sidebar. These widgets trigger filtering events within the Pandas DataFrame.

# Support
Current support only exists for DataFrame columns with strings and numbers (int64 and float64). A future update will include support for time-series data.

By default, string data generates a text_input Streamlit widget, while numerical data creates sliders with ranges preset to the minimum and maximum values for that column. Users can pass a custom dictionary for handling specific types of data, where each key is the column in the DataFrame and the value is the streamlit widget type.

Sample of a custom dictionary:

```python
create_data = {"Name": "text",
                "Sex": "multiselect",
                "Embarked": "multiselect",
                "Ticket": "text",
                "Pclass": "multiselect"}
```
The current version only supports: text, multiselect, and select.

# Installation
1. First, install Streamlit
```python
pip install streamlit
```
2. Next, install Pandas
```python
pip install pandas
```
3. Install Streamlit Pandas
```python
pip install streamlit-pandas
```

# Usage
```python
import streamlit as st
import pandas as pd
import streamlit_pandas as sp

@st.cache(allow_output_mutation=True)
def load_data():
    df = pd.read_csv(file)
    return df

file = "../data/titanic.csv"
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
```
This will generate the following application:

![Streamlit-Pandas demo application](https://github.com/wjbmattingly/streamlit-pandas/raw/main/images/streamlit-pandas-app.jpg)
