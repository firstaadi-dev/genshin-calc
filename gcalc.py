import streamlit as st
import streamlit.components.v1 as components
import math
import numpy as np
import matplotlib.pyplot as plt
st.write("""
# Genshin Stats Compare
""")
atk1 = st.number_input("Atk 1")
crate1 = st.number_input("Crit Rate 1")
cdmg1 = st.number_input("Crit Damage 1")
atk2 = st.number_input("Atk 2")
crate2 = st.number_input("Crit Rate 2")
cdmg2 = st.number_input("Crit Damage 2")

crit_rate1 = crate1/100
crit_damage1 = cdmg1/100 + 1
crit_rate2 = crate2/100
crit_damage2 = cdmg2/100 + 1
damage1 = atk1 * (math.exp(-(300/(255+40*4))) + 0.01 * 40)
damage2 = atk2 * (math.exp(-(300/(255+40*4))) + 0.01 * 40)
x = np.arange(0,30,5)
y = []
y2 = []
y3 = []
y4 = []
y5 = []
y6 = []
for atk in x:
  damage_crit1 = round(atk)*damage1*crit_damage1
  damage_noncrit1 = round(atk)*damage1
  damage_est1 = round(atk*crit_rate1)*damage1*crit_damage1 + round(atk*(1-crit_rate1))*damage1
  damage_crit2 = round(atk)*damage2*crit_damage2
  damage_noncrit2 = round(atk)*damage2
  damage_est2 = round(atk*crit_rate2)*damage2*crit_damage2 + round(atk*(1-crit_rate2))*damage2
  y.append(damage_crit1)
  y2.append(damage_noncrit1)
  y3.append(damage_est1)
  y4.append(damage_crit2)
  y5.append(damage_noncrit2)
  y6.append(damage_est2)
fig, ax =plt.subplots()
plt.plot(x,y,label="All hit Crit")
plt.plot(x,y2,label="All hit not-Crit")
plt.plot(x,y3,label="Damage Estimation")
plt.plot(x,y4,label="All hit Crit2")
plt.plot(x,y5,label="All hit not-Crit2")
plt.plot(x,y6,label="Damage Estimation2")
plt.legend()

st.pyplot(fig)