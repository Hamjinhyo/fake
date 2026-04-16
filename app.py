import streamlit as st

st.set_page_config(page_title="징계 AI 자동화 데모", layout="wide")

st.title("📄 징계 업무 AI 자동화 시스템 (Demo)")

# -----------------------------
# 사이드바 입력
# -----------------------------
st.sidebar.header("사건 정보 입력")

case_type = st.sidebar.selectbox(
    "사건 유형",
    ["지각/결근", "폭언/괴롭힘", "업무 태만", "비위행위", "기타"]
)

severity = st.sidebar.selectbox(
    "심각도",
    ["낮음", "중간", "높음"]
)

repeat = st.sidebar.selectbox(
    "반복 여부",
    ["초범", "반복"]
)

description = st.sidebar.text_area("사건 상세 설명")

# -----------------------------
# 메인 영역
# -----------------------------
col1, col2 = st.columns(2)

# -----------------------------
# AI 판단 결과 (Mock)
# -----------------------------
with col1:
    st.subheader("🤖 AI 징계 판단")

    if st.button("분석 실행"):
        # 간단한 룰 기반 (데모용)
        if severity == "높음" and repeat == "반복":
            result = "정직 또는 해고"
        elif severity == "높음":
            result = "정직"
        elif severity == "중간":
            result = "감봉"
        else:
            result = "경고"

        st.success(f"추천 징계 수준: **{result}**")

        st.write("📊 판단 근거")
        st.write("- 유사 사례 기준 다수 동일 처분")
        st.write("- 반복성 / 고의성 반영")
        st.write("- 내부 정책 기준 적용")

# -----------------------------
# 문서 생성
# -----------------------------
with col2:
    st.subheader("📑 문서 자동 생성")

    if st.button("문서 생성"):
        st.markdown("### 1. 인사위원회 보고서 (요약)")
        st.write(f"""
        - 사건 유형: {case_type}
        - 심각도: {severity}
        - 반복 여부: {repeat}
        - 내용: {description}
        """)

        st.markdown("### 2. 징계 처분장 (초안)")
        st.write(f"""
        해당 직원은 '{case_type}' 관련 행위를 수행하였으며,
        그 정도가 '{severity}' 수준으로 판단됨.

        또한 '{repeat}' 사례로 확인되어
        내부 규정에 따라 적절한 징계가 필요함.

        이에 따라 본 위원회는 징계를 결정함.
        """)

# -----------------------------
# 하단 설명
# -----------------------------
st.divider()
st.caption("※ 본 데모는 AI 판단 보조 시스템이며 최종 판단은 담당자가 수행합니다.")
