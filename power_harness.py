"""Hover power, battery endurance and wiring harness loss of a scaled quad rotor aerial vehicle (momentum theory).
ALL inputs are ASSUMED (self initiated study)."""
import numpy as np, pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

MASS = 2.0           # kg take off mass (assumed)
NROT = 4
DIA = 0.254          # m rotor diameter (10 inch, assumed)
RHO = 1.225
FM = 0.60            # figure of merit (assumed)
ETA = 0.80           # motor and speed controller efficiency (assumed)
VBAT = 22.2          # V six cell pack nominal (assumed)
CAP_AH = 5.0         # Ah (assumed)
USABLE = 0.80
LEN_M = 0.30         # m battery to speed controller harness length per motor, one way (assumed)
RHO_CU = 1.68e-8
AWG = {22: 0.326e-6, 20: 0.518e-6, 18: 0.823e-6}   # copper cross section, m2

A = np.pi * DIA ** 2 / 4
T_ROT = MASS * 9.81 / NROT
P_IDEAL = T_ROT ** 1.5 / np.sqrt(2 * RHO * A)
P_ELEC_ROT = P_IDEAL / FM / ETA
P_ELEC = NROT * P_ELEC_ROT
I_TOT = P_ELEC / VBAT
rows = []
for awg, area in AWG.items():
    i_rot = I_TOT / NROT
    r_loop = RHO_CU * 2 * LEN_M / area
    p_loss = NROT * i_rot ** 2 * r_loop
    rows.append(dict(awg=awg, harness_loss_W=p_loss, loss_pct_of_hover_power=100 * p_loss / P_ELEC, voltage_drop_V=i_rot * r_loop,
                     copper_mass_g=NROT * 2 * LEN_M * area * 8960 * 1e3))
df = pd.DataFrame(rows)
endurance_min = CAP_AH * USABLE * VBAT / P_ELEC * 60
df.to_csv("results.csv", index=False)
print("hover electrical power W: %.1f  total current A: %.2f  endurance min: %.1f" % (P_ELEC, I_TOT, endurance_min))
print(df.round(3).to_string())
plt.figure(figsize=(5, 3.4))
plt.bar([str(a) for a in df.awg], df.loss_pct_of_hover_power)
plt.xlabel("AWG"); plt.ylabel("harness loss (% of hover power)"); plt.title("Harness loss at hover (assumed data)", fontsize=9)
plt.tight_layout(); plt.savefig("power_harness.png", dpi=130)
