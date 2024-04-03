import streamlit as st
def calculator(a,b, op= "+"):
    match op:
        case'+': return a+b
        case'-': return a-b
        case'/': return a/b
        case'*': return a*b
        case'': return a**b

# main 
st.title("Calculator")
st.markdown("very simpleand cheap example of streamlit")

c1, c2, c3 = st.columns(3)
num1 = c1.number_input("enter number", value=62)
num2 = c2.number_input("enter number", value=12)

op = c3.selectbox("select operator", ["+", "-", "/", "", "*"])

try:
    result = calculator(num1, num2, op)
    st.success(f"result: {result}")
except Exception as e:
    st.error(f"error: {e}")