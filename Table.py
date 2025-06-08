import streamlit as st
import sympy
import pandas as pd

st.title("🔢 소인수분해: 10^k - 1")
st.write("아래 표는 `10^k - 1`의 소인수분해 결과를 보여줍니다. 더 많은 항을 보려면 슬라이더로 범위를 조절하세요.")

# 사용자로부터 k의 범위 선택
max_k = st.slider("k의 최대값을 선택하세요", min_value=1, max_value=1000, value=50)

data = []
for k in range(1, max_k + 1):
    number = 10 ** k - 1
    factors = sympy.factorint(number)  # 소인수 분해 (딕셔너리 형식: {소인수: 지수})
    factor_str = " × ".join([f"{p}^{e}" if e > 1 else str(p) for p, e in factors.items()])
    data.append({
        "k": k,
        "10^k - 1": f"{number:,}",
        "소인수분해": factor_str
    })

# 표로 출력
df = pd.DataFrame(data)
st.dataframe(df, use_container_width=True)
