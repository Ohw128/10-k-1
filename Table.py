import streamlit as st
import sympy
import pandas as pd

st.title("🔢 소인수분해: 10^k - 1")
st.write("아래 표는 `10^k - 1`의 소인수분해 결과를 보여줍니다. `k`가 너무 크면 계산이 오래 걸릴 수 있습니다.")

# 안전한 최대 k 값 제한
max_k = st.slider("k의 최대값을 선택하세요", min_value=1, max_value=100, value=30)

data = []

# 진행바 표시
progress_bar = st.progress(0)

for idx, k in enumerate(range(1, max_k + 1)):
    number = 10 ** k - 1

    try:
        factors = sympy.factorint(number, limit=1000000)  # 계산 시간 제한
        factor_str = " × ".join([f"{p}^{e}" if e > 1 else str(p) for p, e in factors.items()])
    except Exception as e:
        factor_str = "⚠️ 너무 커서 계산 실패"

    data.append({
        "k": k,
        "10^k - 1": f"{number:,}",
        "소인수분해": factor_str
    })

    progress_bar.progress((idx + 1) / max_k)

# 표 출력
df = pd.DataFrame(data)
st.dataframe(df, use_container_width=True)
