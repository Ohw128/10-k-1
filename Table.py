import streamlit as st
import sympy
import pandas as pd

st.set_page_config(page_title="10^k - 1 소인수분해", layout="wide")

st.title("🔢 10^k - 1 소인수분해 도구")

st.header("📊 1. 10^k - 1의 소인수분해 (1 ≤ k ≤ 50)")
table_data = []
for k in range(1, 51):
    n = 10 ** k - 1
    try:
        factors = sympy.factorint(n)
        factor_str = " × ".join([f"{p}^{e}" if e > 1 else str(p) for p, e in factors.items()])
    except:
        factor_str = "계산 실패"
    table_data.append({
        "k": k,
        "10^k - 1": f"{n:,}",
        "소인수분해": factor_str
    })

df = pd.DataFrame(table_data)
st.dataframe(df, height=500)

# -----------------------------------------------------------------------------

st.header("🔍 2. 원하는 k에 대해 10^k - 1 소인수분해 보기")
custom_k = st.number_input("k 값을 입력하세요 (1 이상)", min_value=1, max_value=1000, value=60, step=1)

if st.button("소인수분해 계산하기"):
    num = 10 ** custom_k - 1
    st.write(f"**10^{custom_k} - 1 = {num:,}**")
    try:
        factors = sympy.factorint(num)
        st.write("**소인수분해 결과:**")
        for p, e in factors.items():
            st.write(f"- {p}^{e}" if e > 1 else f"- {p}")
    except Exception as e:
        st.warning("⚠️ 너무 커서 계산할 수 없습니다.")

# -----------------------------------------------------------------------------

st.header("🧮 3. 어떤 k에 대해 10^k - 1이 특정 수로 나누어떨어지는지 찾기")
divisor = st.number_input("나눌 수 (d)를 입력하세요", min_value=2, max_value=10**6, value=7, step=1)
k_limit = st.number_input("최대 k 값 (범위 탐색)", min_value=1, max_value=500, value=100, step=1)

if st.button("나누어떨어지는 k 값 찾기"):
    results = []
    for k in range(1, k_limit + 1):
        if (10 ** k - 1) % divisor == 0:
            results.append(k)
    if results:
        st.success(f"✅ 10^k - 1이 {divisor}로 나누어떨어지는 k 값들: {results}")
    else:
        st.info("해당 범위에서는 없습니다.")
