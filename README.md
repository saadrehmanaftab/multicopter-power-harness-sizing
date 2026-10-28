# Power supply and wiring harness sizing of a scaled quad rotor

Self initiated study. Every input is ASSUMED, none comes from a measurement or an employer.

## What it does
`power_harness.py` estimates the hover power of a 2 kg quad rotor by momentum theory (rotor diameter 0.254 m, figure of merit 0.60,
motor and speed controller efficiency 0.80), the endurance on a six cell 5 Ah battery (80 percent usable), and the copper loss of the
battery to speed controller harness for three wire gauges (0.30 m one way per motor).

## Results (results.csv)
Hover electrical power 256.9 W, total current 11.57 A, endurance 20.7 min.

| AWG | harness loss W | percent of hover power | voltage drop V | copper g |
|---|---|---|---|---|
| 22 | 1.035 | 0.403 | 0.089 | 7.0 |
| 20 | 0.652 | 0.254 | 0.056 | 11.1 |
| 18 | 0.410 | 0.160 | 0.035 | 17.7 |

## Assumptions and limits
- Momentum theory with a constant figure of merit, hover only, no forward flight, no ground effect, no battery sag or temperature effects.
- Battery nominal voltage 22.2 V and capacity are typed in. The speed controller to motor leads, connectors and contact resistance are not modeled.
- The study compares resistive loss only. Current rating and insulation heating of each gauge are NOT checked, so it is not a harness design.
- Not validated against a measurement.

## Run
`pip install numpy pandas matplotlib` then `python power_harness.py`. It writes results.csv and power_harness.png.
