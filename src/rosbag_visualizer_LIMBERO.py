import pandas as pd
import matplotlib.pyplot as plt
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config import rosbag_visualizer_LIMBERO_config

experiment_date = '20250527_LIMBERO' # Change Here
csv_file_encoder = f"../data/{experiment_date}/{rosbag_visualizer_LIMBERO_config.take_label}_joint_states.csv"
# csv_file_target_vel = f"../data/{experiment_date}/{rosbag_visualizer_config.take_label}_joint_trajectory.csv"
df_encoder = pd.read_csv(csv_file_encoder)
# df_target_vel = pd.read_csv(csv_file_target_vel)
result_base_dir = os.path.join(os.path.dirname(__file__), '..', 'results', experiment_date)
result_dir = os.path.join(result_base_dir, rosbag_visualizer_LIMBERO_config.take_label)
os.makedirs(result_dir, exist_ok = True)

# function to plot encoder value
def plot_leg_effort(df, rename_dict, leg_label):
    df_leg = df[list(rename_dict.keys())].rename(columns = rename_dict).dropna() ## remove NaN
    df_leg['relative_time'] = df_leg['time'] - df_leg['time'].iloc[0]

    plt.figure(figsize=(10, 6))
    plt.plot(df_leg['relative_time'], df_leg['B2C'], label=f'{leg_label}_B2C', color='red')
    plt.plot(df_leg['relative_time'], df_leg['C2F'], label=f'{leg_label}_C2F', color='blue')
    plt.plot(df_leg['relative_time'], df_leg['F2T'], label=f'{leg_label}_F2T', color='green')
    plt.plot(df_leg['relative_time'], df_leg['T2E'], label=f'{leg_label}_T2E', color='orange')
    plt.plot(df_leg['relative_time'], df_leg['end_effector'], label=f'{leg_label}_end_effector', color='yellow')
    plt.plot(df_leg['relative_time'], df_leg['palm'], label=f'{leg_label}_palm', color='cyan')
    plt.xlabel('Time [s]')
    plt.ylabel('Effort [mA]')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    save_path = os.path.join(result_dir, f'{leg_label}_effort_{rosbag_visualizer_LIMBERO_config.take_label}.png')
    plt.savefig(save_path)

plot_leg_effort(df_encoder, rosbag_visualizer_LIMBERO_config.LF_encoder_rename_dict, 'LF')
plot_leg_effort(df_encoder, rosbag_visualizer_LIMBERO_config.LH_encoder_rename_dict, 'LH')
plot_leg_effort(df_encoder, rosbag_visualizer_LIMBERO_config.RH_encoder_rename_dict, 'RH')
plot_leg_effort(df_encoder, rosbag_visualizer_LIMBERO_config.RF_encoder_rename_dict, 'RF')

plt.show()