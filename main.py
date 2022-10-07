# from email.policy import default
import streamlit as st
import pandas as pd
import numpy as np
import time
import requests

with open("example.txt", "r") as f:
    example_text = f.read()
st.markdown("## Demo")

input_text = st.text_area("Input Text", example_text)
g = st.button("Generate")
if g:
    url = "http://175.178.103.247:18080/extract_money/"
    print("type of input_text", type(input_text))
    d={"text":input_text}
    r= requests.post(url, data=d)
    print(r.status_code, r.reason)
    st.markdown("- TODO: render the results as graph")
    st.code(str(r.json()), language="json")
st.markdown("## More Examples")
st.markdown("- https://wenshu.court.gov.cn")