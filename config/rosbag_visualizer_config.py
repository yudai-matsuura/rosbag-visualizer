## Experiment take
take_label = 'take6'

## Encoder dict
LF_encoder_rename_dict = {
    '__time': 'time',
    '/LF/joint_states/LF_B2C/effort': 'B2C',
    '/LF/joint_states/LF_C2F/effort': 'C2F',
    '/LF/joint_states/LF_F2T/effort': 'F2T',
    '/LF/joint_states/LF_T2E/effort': 'T2E',
    '/LF/joint_states/LF_steering/effort': 'steering',
    '/LF/joint_states/LF_driving/effort': 'driving',
    '/LF/joint_states/LF_gripper/effort': 'gripper'
}
LH_encoder_rename_dict = {
    '__time': 'time',
    '/LH/joint_states/LH_B2C/effort': 'B2C',
    '/LH/joint_states/LH_C2F/effort': 'C2F',
    '/LH/joint_states/LH_F2T/effort': 'F2T',
    '/LH/joint_states/LH_T2E/effort': 'T2E',
    '/LH/joint_states/LH_steering/effort': 'steering',
    '/LH/joint_states/LH_driving/effort': 'driving',
    '/LH/joint_states/LH_gripper/effort': 'gripper'
}
RH_encoder_rename_dict = {
    '__time': 'time',
    '/RH/joint_states/RH_B2C/effort': 'B2C',
    '/RH/joint_states/RH_C2F/effort': 'C2F',
    '/RH/joint_states/RH_F2T/effort': 'F2T',
    '/RH/joint_states/RH_T2E/effort': 'T2E',
    '/RH/joint_states/RH_steering/effort': 'steering',
    '/RH/joint_states/RH_driving/effort': 'driving',
    '/RH/joint_states/RH_gripper/effort': 'gripper'
}
RF_encoder_rename_dict = {
    '__time': 'time',
    '/RF/joint_states/RF_B2C/effort': 'B2C',
    '/RF/joint_states/RF_C2F/effort': 'C2F',
    '/RF/joint_states/RF_F2T/effort': 'F2T',
    '/RF/joint_states/RF_T2E/effort': 'T2E',
    '/RF/joint_states/RF_steering/effort': 'steering',
    '/RF/joint_states/RF_driving/effort': 'driving',
    '/RF/joint_states/RF_gripper/effort': 'gripper'
}
## target velocity dict
LF_target_rename_dict = {
    '__time': 'time',
    '/LF/joint_trajectory_controller/joint_trajectory/points[0]/velocities[0]': 'B2C',
    '/LF/joint_trajectory_controller/joint_trajectory/points[0]/velocities[1]': 'C2F',
    '/LF/joint_trajectory_controller/joint_trajectory/points[0]/velocities[2]': 'F2T',
    '/LF/joint_trajectory_controller/joint_trajectory/points[0]/velocities[3]': 'T2E',
    '/LF/joint_trajectory_controller/joint_trajectory/points[0]/velocities[4]': 'steering',
    '/LF/joint_trajectory_controller/joint_trajectory/points[0]/velocities[5]': 'driving',
    '/LF/joint_trajectory_controller/joint_trajectory/points[0]/velocities[6]': 'gripper'
}
LH_target_rename_dict = {
    '__time': 'time',
    '/LH/joint_trajectory_controller/joint_trajectory/points[0]/velocities[0]': 'B2C',
    '/LH/joint_trajectory_controller/joint_trajectory/points[0]/velocities[1]': 'C2F',
    '/LH/joint_trajectory_controller/joint_trajectory/points[0]/velocities[2]': 'F2T',
    '/LH/joint_trajectory_controller/joint_trajectory/points[0]/velocities[3]': 'T2E',
    '/LH/joint_trajectory_controller/joint_trajectory/points[0]/velocities[4]': 'steering',
    '/LH/joint_trajectory_controller/joint_trajectory/points[0]/velocities[5]': 'driving',
    '/LH/joint_trajectory_controller/joint_trajectory/points[0]/velocities[6]': 'gripper'
}
RH_target_rename_dict = {
    '__time': 'time',
    '/RH/joint_trajectory_controller/joint_trajectory/points[0]/velocities[0]': 'B2C',
    '/RH/joint_trajectory_controller/joint_trajectory/points[0]/velocities[1]': 'C2F',
    '/RH/joint_trajectory_controller/joint_trajectory/points[0]/velocities[2]': 'F2T',
    '/RH/joint_trajectory_controller/joint_trajectory/points[0]/velocities[3]': 'T2E',
    '/RH/joint_trajectory_controller/joint_trajectory/points[0]/velocities[4]': 'steering',
    '/RH/joint_trajectory_controller/joint_trajectory/points[0]/velocities[5]': 'driving',
    '/RH/joint_trajectory_controller/joint_trajectory/points[0]/velocities[6]': 'gripper'
}
RF_target_rename_dict = {
    '__time': 'time',
    '/RF/joint_trajectory_controller/joint_trajectory/points[0]/velocities[0]': 'B2C',
    '/RF/joint_trajectory_controller/joint_trajectory/points[0]/velocities[1]': 'C2F',
    '/RF/joint_trajectory_controller/joint_trajectory/points[0]/velocities[2]': 'F2T',
    '/RF/joint_trajectory_controller/joint_trajectory/points[0]/velocities[3]': 'T2E',
    '/RF/joint_trajectory_controller/joint_trajectory/points[0]/velocities[4]': 'steering',
    '/RF/joint_trajectory_controller/joint_trajectory/points[0]/velocities[5]': 'driving',
    '/RF/joint_trajectory_controller/joint_trajectory/points[0]/velocities[6]': 'gripper'
}