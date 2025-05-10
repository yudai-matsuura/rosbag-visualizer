import pandas as pd
import matplotlib.pyplot as plt
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from include import rosbag_visualizer_config

csv_file = "../data/csv/take6_joint_states.csv"
df = pd.read_csv(csv_file)

### LF
df_lf = df[list(rosbag_visualizer_config.LF_rename_dict.keys())].rename(columns = rosbag_visualizer_config.LF_rename_dict).dropna() ## remove NaN
df_lf['relative_time'] = df_lf['time'] - df_lf['time'].iloc[0]
# plot figure
plt.figure(figsize = (10, 6))
plt.plot(df_lf['relative_time'], df_lf['B2C'], label = 'LF_B2C', color = 'red')
plt.plot(df_lf['relative_time'], df_lf['C2F'], label = 'LF_C2F', color = 'blue')
plt.plot(df_lf['relative_time'], df_lf['F2T'], label = 'LF_F2T', color = 'green')
plt.plot(df_lf['relative_time'], df_lf['T2E'], label = 'LF_T2E', color = 'orange')
plt.plot(df_lf['relative_time'], df_lf['steering'], label = 'LF_steering', color = 'yellow')
plt.plot(df_lf['relative_time'], df_lf['driving'], label = 'LF_driving', color = 'cyan')
plt.plot(df_lf['relative_time'], df_lf['gripper'], label = 'LF_gripper', color = 'magenta')
# figure config
plt.xlabel('Time [s]')
plt.ylabel('Effort')
plt.legend()
plt.grid(True)
plt.tight_layout()

### LH
df_lh = df[list(rosbag_visualizer_config.LH_rename_dict.keys())].rename(columns = rosbag_visualizer_config.LH_rename_dict).dropna() ## remove NaN
df_lh['relative_time'] = df_lh['time'] - df_lh['time'].iloc[0]
# plot figure
plt.figure(figsize = (10, 6))
plt.plot(df_lh['relative_time'], df_lh['B2C'], label = 'LH_B2C', color = 'red')
plt.plot(df_lh['relative_time'], df_lh['C2F'], label = 'LH_C2F', color = 'blue')
plt.plot(df_lh['relative_time'], df_lh['F2T'], label = 'LH_F2T', color = 'green')
plt.plot(df_lh['relative_time'], df_lh['T2E'], label = 'LH_T2E', color = 'orange')
plt.plot(df_lh['relative_time'], df_lh['steering'], label = 'LH_steering', color = 'yellow')
plt.plot(df_lh['relative_time'], df_lh['driving'], label = 'LH_driving', color = 'cyan')
plt.plot(df_lh['relative_time'], df_lh['gripper'], label = 'LH_gripper', color = 'magenta')
# figure config
plt.xlabel('Time [s]')
plt.ylabel('Effort')
plt.legend()
plt.grid(True)
plt.tight_layout()

### RH
df_rh = df[list(rosbag_visualizer_config.RH_rename_dict.keys())].rename(columns = rosbag_visualizer_config.RH_rename_dict).dropna() ## remove NaN
df_rh['relative_time'] = df_rh['time'] - df_rh['time'].iloc[0]
# plot figure
plt.figure(figsize = (10, 6))
plt.plot(df_rh['relative_time'], df_rh['B2C'], label = 'RH_B2C', color = 'red')
plt.plot(df_rh['relative_time'], df_rh['C2F'], label = 'RH_C2F', color = 'blue')
plt.plot(df_rh['relative_time'], df_rh['F2T'], label = 'RH_F2T', color = 'green')
plt.plot(df_rh['relative_time'], df_rh['T2E'], label = 'RH_T2E', color = 'orange')
plt.plot(df_rh['relative_time'], df_rh['steering'], label = 'RH_steering', color = 'yellow')
plt.plot(df_rh['relative_time'], df_rh['driving'], label = 'RH_driving', color = 'cyan')
plt.plot(df_rh['relative_time'], df_rh['gripper'], label = 'RH_gripper', color = 'magenta')
# figure config
plt.xlabel('Time [s]')
plt.ylabel('Effort [mA]')
plt.legend()
plt.grid(True)
plt.tight_layout()

### RF
df_rf = df[list(rosbag_visualizer_config.RF_rename_dict.keys())].rename(columns = rosbag_visualizer_config.RF_rename_dict).dropna() ## remove NaN
df_rf['relative_time'] = df_rf['time'] - df_rf['time'].iloc[0]
# plot figure
plt.figure(figsize = (10, 6))
plt.plot(df_rf['relative_time'], df_rf['B2C'], label = 'RF_B2C', color = 'red')
plt.plot(df_rf['relative_time'], df_rf['C2F'], label = 'RF_C2F', color = 'blue')
plt.plot(df_rf['relative_time'], df_rf['F2T'], label = 'RF_F2T', color = 'green')
plt.plot(df_rf['relative_time'], df_rf['T2E'], label = 'RF_T2E', color = 'orange')
plt.plot(df_rf['relative_time'], df_rf['steering'], label = 'RF_steering', color = 'yellow')
plt.plot(df_rf['relative_time'], df_rf['driving'], label = 'RF_driving', color = 'cyan')
plt.plot(df_rf['relative_time'], df_rf['gripper'], label = 'RF_gripper', color = 'magenta')
# figure config
plt.xlabel('Time [s]')
plt.ylabel('Effort')
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.show()