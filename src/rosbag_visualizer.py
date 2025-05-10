import pandas as pd
import matplotlib.pyplot as plt

csv_file = "../data/csv/take6_joint_states.csv"
df = pd.read_csv(csv_file)

rename_dict = {
    '__time': 'time',
    '/LF/joint_states/LF_B2C/effort': 'B2C',
    '/LF/joint_states/LF_C2F/effort': 'C2F',
    '/LF/joint_states/LF_F2T/effort': 'F2T',
    '/LF/joint_states/LF_T2E/effort': 'T2E',
    '/LF/joint_states/LF_steering/effort': 'steering',
    '/LF/joint_states/LF_driving/effort': 'driving',
    '/LF/joint_states/LF_gripper/effort': 'gripper'
}

df_clean = df[list(rename_dict.keys())].rename(columns = rename_dict).dropna() ## remove NaN

# print(df.columns) ## for debug
df_clean['relative_time'] = df_clean['time'] - df_clean['time'].iloc[0]

# plot figure
plt.figure(figsize = (10, 6))
plt.plot(df_clean['relative_time'], df_clean['B2C'], label = 'LF_B2C', color = 'red')
plt.plot(df_clean['relative_time'], df_clean['C2F'], label = 'LF_C2F', color = 'blue')
plt.plot(df_clean['relative_time'], df_clean['F2T'], label = 'LF_F2T', color = 'green')
plt.plot(df_clean['relative_time'], df_clean['T2E'], label = 'LF_T2E', color = 'orange')
plt.plot(df_clean['relative_time'], df_clean['steering'], label = 'LF_steering', color = 'yellow')
plt.plot(df_clean['relative_time'], df_clean['driving'], label = 'LF_driving', color = 'cyan')
plt.plot(df_clean['relative_time'], df_clean['gripper'], label = 'LF_gripper', color = 'magenta')

# figure config
plt.xlabel('Time [s]')
plt.ylabel('Effort')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()