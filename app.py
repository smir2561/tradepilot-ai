import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="TradePilot AI",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 TradePilot AI")
st.subheader("AI-Powered Market Research Assistant")

st.info(
    "TradePilot AI helps organize market research into "
    "clear trends, key levels, scenarios and risk factors."
)

assets = [
    "BTC", "ETH", "SOL", "BNB",
    "AAPL", "NVDA", "TSLA", "SPY"
]

asset = st.selectbox("Select Asset", assets)

timeframe = st.selectbox(
    "Select Timeframe",
    ["15m", "1H", "4H", "1D"]
)

price = st.number_input(
    "Current Price",
    min_value=0.0,
    value=100.0,
    step=0.01
)

sentiment = st.selectbox(
    "Market Context",
    ["Bullish", "Neutral", "Bearish"]
)

if st.button("Generate Research Report"):

    support = price * 0.97
    resistance = price * 1.03

    st.divider()

    st.header(f"{asset} Research Report")

    col1, col2, col3 = st.columns(3)

    col1.metric("Market Bias", sentiment)
    col2.metric("Support", f"{support:.2f}")
    col3.metric("Resistance", f"{resistance:.2f}")

    st.markdown("### 🔎 Market Overview")

    st.write(
        f"{asset} is being analyzed on the "
        f"{timeframe} timeframe."
    )

    st.write(
        f"Current market context: **{sentiment}**."
    )

    st.markdown("### 🎯 Scenario Analysis")

    if sentiment == "Bullish":

        st.write(
            f"• Bullish scenario: strength above "
            f"{resistance:.2f}."
        )

        st.write(
            f"• Pullback area to monitor: "
            f"{support:.2f}."
        )

    elif sentiment == "Bearish":

        st.write(
            f"• Bearish scenario: weakness below "
            f"{support:.2f}."
        )

        st.write(
            f"• Recovery scenario: reclaim "
            f"{resistance:.2f}."
        )

    else:

        st.write(
            f"• Current range: {support:.2f} - "
            f"{resistance:.2f}."
        )

        st.write(
            "• Monitor for a confirmed breakout "
            "or breakdown."
        )

    st.markdown("### ⚠️ Risk Checklist")

    st.write(
        "• Market volatility can invalidate technical levels."
    )

    st.write(
        "• News and macro events can change market conditions."
    )

    st.write(
        "• This prototype is for research purposes and "
        "does not execute trades."
    )

    st.caption(
        f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}"
    )

st.divider()

st.caption(
    "TradePilot AI — Hackathon S2 Prototype"
)
