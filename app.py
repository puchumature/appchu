
import streamlit as st
import pandas as pd

st.title("🏏 Fantasy XI Predictor - Mobile Friendly")

st.sidebar.header("📋 Match Details")
team1 = st.sidebar.text_input("Team 1", "India")
team2 = st.sidebar.text_input("Team 2", "Australia")
venue = st.sidebar.text_input("Venue", "Wankhede Stadium")

st.subheader("🔢 Upload Player Stats (CSV)")
data = st.file_uploader("Upload a CSV file with Player Stats", type=["csv"])

if data:
    df = pd.read_csv(data)
    st.write("📊 Uploaded Player Stats:")
    st.dataframe(df)

    df['Predicted Points'] = (
        df['Runs'] * 1 +
        df['Wickets'] * 25 +
        df['Catches'] * 8
    )

    df = df.sort_values(by='Predicted Points', ascending=False)
    selected_team = df.head(11)

    st.subheader("🏆 Suggested Fantasy Team")
    st.dataframe(selected_team[['Player', 'Role', 'Credits', 'Predicted Points']])

    captain = selected_team.iloc[0]
    vice_captain = selected_team.iloc[1]

    st.markdown(f"👑 **Captain:** {captain['Player']} (2x Points)")
    st.markdown(f"⭐ **Vice-Captain:** {vice_captain['Player']} (1.5x Points)")
    st.success(f"📈 Total Projected Points: {selected_team['Predicted Points'].sum()}")
else:
    st.warning("⚠️ Please upload a player stats CSV file.")
