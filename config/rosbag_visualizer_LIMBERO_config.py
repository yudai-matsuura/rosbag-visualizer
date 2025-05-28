## Experiment take
take_label = 'take1'

## Encoder dict
LF_encoder_rename_dict = {
    '__time': 'time',
    '/LF/joint_states/LF_B2C/effort': 'B2C',
    '/LF/joint_states/LF_C2F/effort': 'C2F',
    '/LF/joint_states/LF_F2T/effort': 'F2T',
    '/LF/joint_states/LF_T2E/effort': 'T2E',
    '/LF/joint_states/LF_end_effector/effort': 'end_effector',
    '/LF/joint_states/LF_palm/effort': 'palm',
}
LH_encoder_rename_dict = {
    '__time': 'time',
    '/LH/joint_states/LH_B2C/effort': 'B2C',
    '/LH/joint_states/LH_C2F/effort': 'C2F',
    '/LH/joint_states/LH_F2T/effort': 'F2T',
    '/LH/joint_states/LH_T2E/effort': 'T2E',
    '/LH/joint_states/LH_end_effector/effort': 'end_effector',
    '/LH/joint_states/LH_palm/effort': 'palm',
}
RH_encoder_rename_dict = {
    '__time': 'time',
    '/RH/joint_states/RH_B2C/effort': 'B2C',
    '/RH/joint_states/RH_C2F/effort': 'C2F',
    '/RH/joint_states/RH_F2T/effort': 'F2T',
    '/RH/joint_states/RH_T2E/effort': 'T2E',
    '/RH/joint_states/RH_end_effector/effort': 'end_effector',
    '/RH/joint_states/RH_palm/effort': 'palm',
}
RF_encoder_rename_dict = {
    '__time': 'time',
    '/RF/joint_states/RF_B2C/effort': 'B2C',
    '/RF/joint_states/RF_C2F/effort': 'C2F',
    '/RF/joint_states/RF_F2T/effort': 'F2T',
    '/RF/joint_states/RF_T2E/effort': 'T2E',
    '/RF/joint_states/RF_end_effector/effort': 'end_effector',
    '/RF/joint_states/RF_palm/effort': 'palm',
}