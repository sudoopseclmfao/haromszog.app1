import streamlit as st

st.title("Háromszög csoportosítása")
st.write("Add meg a háromszög három belső szögét fokban!")

a = st.number_input("1. szög", value=60.0, step=1.0)
b = st.number_input("2. szög", value=60.0, step=1.0)
c = st.number_input("3. szög", value=60.0, step=1.0)

if st.button("Ellenőrzés"):
    if a <= 0 or b <= 0 or c <= 0:
        st.error("A szögek legyenek pozitívak!")
    elif abs(a + b + c - 180) > 0.001:
        st.error("Ez nem lehet háromszög, a szögek összegének 180 foknak kell lenniük!")
    else:
        legnagyobb = max(a, b, c)
        if legnagyobb == 90:
            st.success("A háromszöged derékszögű!")
        elif legnagyobb > 90:
            st.success("A háromszöged tompaszögű!")
        else:
            st.success("A háromszöged hegyesszögű!")
