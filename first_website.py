# -*- coding: utf-8 -*-
"""
Created on Mon Oct 20 00:02:53 2025

@author: j3nor
"""

import streamlit as st

st.header("Profit calculator")
st.subheader("insert information below")


bet = st.number_input("insert bet amount-")
line =st.number_input("insert odds-")

if st.button("Calculate"):
    if line == 0:
        st.error("Odds cannot be 0.")
    elif bet <= 0:
        st.error("Please enter a valid bet amount.")
    else:
        if line < 0:
            profit = bet * (100 / abs(line))
            total = bet + profit
        else:
            profit = bet * (line / 100)
            total = bet + profit

        # --- Display results ---
        st.markdown(f"### 🧾 With a bet of **${bet:.2f}** at odds **{line:+}:**")
        st.success(f"💵 Profit: **${profit:.2f}**")
        st.info(f"💰 Total payout: **${total:.2f}**")
