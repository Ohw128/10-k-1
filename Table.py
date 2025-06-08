import streamlit as st
import sympy
import pandas as pd

st.title("🔢 소인수분해: 10^k - 1")
st.write("표가 너무 길어질 경우, 가로 스크롤을 이용해 끝까지 보세요.")

# 사용자 입력
max_k = st.slider("k의 최대값을 선택하세요", min_value=1, max_value=100, value=30)

data = []

for k in range(1, max_k + 1):
    number = 10 ** k - 1
    try:
        factors = sympy.factorint(number, limit=1000000)
        factor_str = " × ".join([f"{p}^{e}" if e > 1 else str(p) for p, e in factors.items()])
    except Exception:
        factor_str = "⚠️ 너무 커서 계산 실패"

    data.append({
        "k": k,
        "10^k - 1": f"{number:,}",
        "소인수분해 결과": factor_str
    })

# 데이터프레임 생성
df = pd.DataFrame(data)

# 가로 스크롤 가능하게 출력 (container width 안 쓰고, 표가 넘치도록 만듦)
st.dataframe(df, height=500)
