import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config import rosbag_visualizer_config

csv_file_encoder = f"../data/csv/{rosbag_visualizer_config.take_label}_joint_states.csv"
df_encoder = pd.read_csv(csv_file_encoder)
result_base_dir = os.path.join(os.path.dirname(__file__), '..', 'results')
result_dir = os.path.join(result_base_dir, rosbag_visualizer_config.take_label)
os.makedirs(result_dir, exist_ok = True)

# dict
rename_dicts = [
    rosbag_visualizer_config.LF_encoder_rename_dict,
    rosbag_visualizer_config.LH_encoder_rename_dict,
    rosbag_visualizer_config.RH_encoder_rename_dict,
    rosbag_visualizer_config.RF_encoder_rename_dict
]
leg_labels = ['LF', 'LH', 'RH', 'RF']

# plot setting
plt.figure(figsize=(12, 7))
colors = ['red', 'blue', 'green', 'orange']

# A list to store the data for each leg
leg_dfs = []

for rd, label, color in zip(rename_dicts, leg_labels, colors):
    df_leg = df_encoder[list(rd.keys())].rename(columns = rd).dropna() # remove NaN
    df_leg['relative_time'] = df_leg['time'] - df_leg['time'].iloc[0]
    df_leg['effort_sum'] = df_leg[['B2C', 'C2F', 'F2T', 'T2E', 'steering', 'driving', 'gripper']].abs().sum(axis = 1)
    
    leg_dfs.append(df_leg[['relative_time', 'effort_sum']].copy())
    # plot per leg
    plt.plot(df_leg['relative_time'], df_leg['effort_sum'], label = f'{label} sum', color = color)

# Create a common timeline
# Cannot be added as is due to the exclusion process od NaN values
min_time = 0
max_time = max([df['relative_time'].max() for df in leg_dfs])
timeline = pd.Series(np.linspace(min_time, max_time, 1000))

# Interpolating data from each leg onto a common timeline
resampled_dfs = []
for df in leg_dfs:
    resampled = pd.DataFrame({'relative_time': timeline})
    resampled['effort_sum'] = np.interp(
        timeline, 
        df['relative_time'].values, 
        df['effort_sum'].values)
    resampled_dfs.append(resampled)

# calculate and plot sum
combined_df = pd.DataFrame({'relative_time': timeline})
combined_df['effort_sum'] = sum(df['effort_sum'] for df in resampled_dfs)
plt.plot(combined_df['relative_time'], combined_df['effort_sum'], label = 'Total sum', color = 'magenta', linestyle = '--')

plt.xlabel('Time [s]')
plt.ylabel('Effort [mA]')
plt.legend()
plt.grid(True)
plt.tight_layout()

save_path = os.path.join(result_dir, f'total_current_{rosbag_visualizer_config.take_label}.png')
plt.savefig(save_path)
plt.show()