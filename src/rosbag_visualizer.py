import pandas as pd
import matplotlib.pyplot as plt
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from include import rosbag_visualizer_config

csv_file = "../data/csv/take6_joint_states.csv"
df = pd.read_csv(csv_file)
result_dir = os.path.join(os.path.dirname(__file__), '..', 'results')
os.makedirs(result_dir, exist_ok = True)

def plot_leg_effort(df, rename_dict, leg_label):
    df_leg = df[list(rename_dict.keys())].rename(columns = rename_dict).dropna()
    df_leg['relative_time'] = df_leg['time'] - df_leg['time'].iloc[0]

    plt.figure(figsize=(10, 6))
    plt.plot(df_leg['relative_time'], df_leg['B2C'], label=f'{leg_label}_B2C', color='red')
    plt.plot(df_leg['relative_time'], df_leg['C2F'], label=f'{leg_label}_C2F', color='blue')
    plt.plot(df_leg['relative_time'], df_leg['F2T'], label=f'{leg_label}_F2T', color='green')
    plt.plot(df_leg['relative_time'], df_leg['T2E'], label=f'{leg_label}_T2E', color='orange')
    plt.plot(df_leg['relative_time'], df_leg['steering'], label=f'{leg_label}_steering', color='yellow')
    plt.plot(df_leg['relative_time'], df_leg['driving'], label=f'{leg_label}_driving', color='cyan')
    plt.plot(df_leg['relative_time'], df_leg['gripper'], label=f'{leg_label}_gripper', color='magenta')
    plt.xlabel('Time [s]')
    plt.ylabel('Effort [mA]')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    save_path = os.path.join(result_dir, f'{leg_label}_effort.png')
    plt.savefig(save_path)

plot_leg_effort(df, rosbag_visualizer_config.LF_rename_dict, 'LF')
plot_leg_effort(df, rosbag_visualizer_config.LH_rename_dict, 'LH')
plot_leg_effort(df, rosbag_visualizer_config.RH_rename_dict, 'RH')
plot_leg_effort(df, rosbag_visualizer_config.RF_rename_dict, 'RF')

plt.show()