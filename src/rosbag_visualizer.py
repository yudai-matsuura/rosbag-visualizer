import pandas as pd
import matplotlib.pyplot as plt

csv_file = "../data/csv/take6_joint_states.csv"
df = pd.read_csv(csv_file)
df_clean = df[['__time', '/LF/joint_states/LF_B2C/effort']].dropna() ## remove NaN

# print(df.columns)
df_clean['relative_time'] = df_clean['__time'] - df_clean['__time'].iloc[0]
plt.figure(figsize = (10, 6))
plt.plot(df_clean['relative_time'], df_clean['/LF/joint_states/LF_B2C/effort'], label = 'LF_B2C')

plt.xlabel('Time [s]')
plt.ylabel('Effort')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()