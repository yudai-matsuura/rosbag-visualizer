import pandas as pd
import matplotlib.pyplot as plt

csv_file = "../data/csv/take6_joint_states.csv"
df = pd.read_csv(csv_file)

print(df.columns)

plt.figure(figsize = (10, 6))
plt.plot(df['_time'], df['/LF/joint_states/LF_B2C/effort'], label = 'LF_B2C')

plt.xlabel('Time [s]')
plt.ylabel('Effort')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()