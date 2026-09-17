_useless_feature_names = [
    'fw_1018680', 'wl_1018645', 'fw_1018645', 'wl_1018655', 'fw_1018655',
    'wl_1018660', 'fw_1018660', 'wl_1018664', 'fw_1018664', 'fw_1018669',
    'wl_1018685', 'fw_1018685', 'fw_1007604', 'fw_1007642', 'fw_1007653',
    'fw_1007656', 'fw_1007672', 'fw_1007697', 'wl_1018605', 'fw_1018605',
    'wl_1018611', 'fw_1018611', 'wl_1018628', 'fw_1018628', 'fw_1018638',
    'fw_1019667', 'fw_1022644', 'wl_1022659', 'fw_1022659', 'fw_1101609',
    'wl_1022665', 'fw_1022665', 'fw_1101615', 'fw_1101625',
    'wl_1101675', 'fw_1101675', 'wl_1101685', 'fw_1101685',
    'wl_1101690', 'fw_1101690', 'wl_1202630', 'fw_1202630',
    'wl_1202660', 'fw_1202660', 'wl_1202670', 'fw_1202670',

    'fw_1007630', 'fw_1007634', 'fw_1007639', 'fw_1007649', 'fw_1007664',
    'wl_1015639', 'fw_1015680', 'fw_1019637', 'fw_1019675', 'wl_1021660',
    'fw_1021660', 'fw_1023640', 'fw_1023662', 'fw_1101696'
]
_unimportant_feature_names = [
    'fw_1007620', 'fw_1007633', 'fw_1007641', 'fw_1007662', 'fw_1013620',
    'fw_1013652', 'fw_1015630', 'fw_1015639', 'fw_1015640', 'fw_1016655',
    'fw_1016670', 'fw_1016695', 'fw_1017678', 'fw_1017690', 'fw_1018658',
    'fw_1019620', 'fw_1019635', 'fw_1019636', 'fw_1019680', 'fw_1021670',
    'fw_1022642', 'fw_1022643', 'fw_1022645', 'fw_1022662', 'fw_1022664',
    'fw_1022666', 'fw_1022668', 'fw_1023680', 'fw_1101695', 'rf_10074020',
    'rf_10154032', 'rf_10184030', 'rf_10184050', 'rf_10184070', 'rf_10184232',
    'rf_10214020', 'rf_11014130', 'rf_11014140', 'rf_12024010', 'rf_12024020',
    'wl_1007604', 'wl_1007642', 'wl_1007653', 'wl_1007656', 'wl_1007672',
    'wl_1007697', 'wl_1017678', 'wl_1018638', 'wl_1018658', 'wl_1018669',
    'wl_1019636', 'wl_1019637', 'wl_1019667', 'wl_1019680', 'wl_1022642',
    'wl_1022643', 'wl_1022644', 'wl_1022645', 'wl_1022662', 'wl_1022664',
    'wl_1022666', 'wl_1022668', 'wl_1101609', 'wl_1101615', 'wl_1101625'
]

_positive_importances = ['swl_diff2_s1', 'swl_diff1_s2', 'swl_diff1_s3', 'swl_diff2_s3', 'swl_s4', 'swl_diff2_s7',
                         'swl_diff1_s8', 'swl_diff1_s9', 'swl_diff2_s9', 'swl_diff1_s11', 'swl_diff2_s12',
                         'swl_roll3_std', 'swl_absdiff_roll3_mean', 'swl_diff_roll3_sqmean', 'swl_absdiff_roll3_min',
                         'swl_absdiff_roll6_max', 'swl_roll9_std', 'swl_absdiff_roll9_mean', 'swl_absdiff_roll9_max',
                         'swl_roll12_mean', 'swl_roll15_std', 'swl_absdiff_roll18_mean', 'swl_diff_roll18_sqmean',
                         'swl_absdiff_roll18_max', 'inf_s1', 'inf_diff1_s1', 'inf_diff2_s4', 'inf_diff2_s5',
                         'inf_diff1_s6', 'inf_s7', 'inf_diff1_s7', 'inf_diff2_s7', 'inf_s8', 'inf_diff1_s8',
                         'inf_diff2_s11', 'inf_diff1_s12', 'inf_roll3_mean', 'inf_roll3_std', 'inf_roll3_max',
                         'inf_roll6_mean', 'inf_roll6_median', 'inf_roll6_max', 'inf_diff_roll6_sqmean',
                         'inf_absdiff_roll6_min', 'inf_roll9_mean', 'inf_roll9_median', 'inf_roll9_std',
                         'inf_roll9_max', 'inf_roll12_mean', 'inf_roll12_max', 'inf_roll15_mean', 'inf_roll15_std',
                         'inf_roll15_max', 'inf_diff_roll15_sqmean', 'inf_roll18_median', 'inf_roll18_std',
                         'inf_roll18_min', 'sfw_s1', 'sfw_diff2_s1', 'sfw_diff1_s2', 'sfw_diff2_s6', 'sfw_s8',
                         'sfw_diff1_s9', 'sfw_diff2_s9', 'sfw_absdiff_roll3_mean', 'sfw_roll9_std',
                         'sfw_absdiff_roll9_max', 'sfw_roll15_median', 'sfw_roll18_min', 'sfw_diff_roll18_sqmean',
                         'sfw_absdiff_roll18_max', 'ecpc_diff1_s8', 'ecpc_roll18_max', 'tototf_s1', 'tototf_s2',
                         'tototf_diff1_s2', 'tototf_diff2_s2', 'tototf_diff1_s3', 'tototf_s4', 'tototf_s5', 'tototf_s6',
                         'tototf_diff1_s8', 'tototf_diff1_s9', 'tototf_s10', 'tototf_diff1_s10', 'tototf_diff2_s10',
                         'tototf_s11', 'tototf_diff2_s12', 'tototf_roll3_mean', 'tototf_roll3_max', 'tototf_roll3_min',
                         'tototf_roll6_mean', 'tototf_roll6_median', 'tototf_roll6_std', 'tototf_roll6_max',
                         'tototf_roll6_min', 'tototf_diff_roll6_sqmean', 'tototf_roll9_mean', 'tototf_roll9_std',
                         'tototf_roll9_max', 'tototf_roll9_min', 'tototf_roll12_mean', 'tototf_roll12_median',
                         'tototf_roll12_max', 'tototf_absdiff_roll12_mean', 'tototf_roll15_mean', 'tototf_roll15_max',
                         'tototf_absdiff_roll15_mean', 'tototf_diff_roll15_sqmean', 'tototf_absdiff_roll15_max',
                         'tototf_roll18_median', 'tototf_roll18_min', 'wl_1018662_s1', 'wl_1018662_diff1_s1',
                         'wl_1018662_diff2_s1', 'wl_1018662_s2', 'wl_1018662_diff1_s2', 'wl_1018662_diff2_s2',
                         'wl_1018662_s3', 'wl_1018662_diff1_s3', 'wl_1018662_diff2_s3', 'wl_1018662_s4',
                         'wl_1018662_diff1_s4', 'wl_1018662_diff2_s4', 'wl_1018662_s5', 'wl_1018662_diff1_s5',
                         'wl_1018662_diff2_s5', 'wl_1018662_s6', 'wl_1018662_diff1_s6', 'wl_1018662_diff2_s6',
                         'wl_1018662_s7', 'wl_1018662_diff2_s7', 'wl_1018662_s8', 'wl_1018662_diff1_s8',
                         'wl_1018662_diff2_s8', 'wl_1018662_s9', 'wl_1018662_diff1_s9', 'wl_1018662_diff2_s9',
                         'wl_1018662_diff1_s10', 'wl_1018662_diff2_s10', 'wl_1018662_s11', 'wl_1018662_diff1_s11',
                         'wl_1018662_diff2_s11', 'wl_1018662_s12', 'wl_1018662_diff1_s12', 'wl_1018662_diff2_s12',
                         'wl_1018662_roll3_mean', 'wl_1018662_roll3_median', 'wl_1018662_roll3_std',
                         'wl_1018662_roll3_max', 'wl_1018662_roll3_min', 'wl_1018662_absdiff_roll3_mean',
                         'wl_1018662_diff_roll3_sqmean', 'wl_1018662_absdiff_roll3_max', 'wl_1018662_absdiff_roll3_min',
                         'wl_1018662_roll6_mean', 'wl_1018662_roll6_std', 'wl_1018662_roll6_max',
                         'wl_1018662_roll6_min', 'wl_1018662_absdiff_roll6_mean', 'wl_1018662_diff_roll6_sqmean',
                         'wl_1018662_absdiff_roll6_max', 'wl_1018662_absdiff_roll6_min', 'wl_1018662_roll9_median',
                         'wl_1018662_roll9_std', 'wl_1018662_roll9_max', 'wl_1018662_roll9_min',
                         'wl_1018662_absdiff_roll9_mean', 'wl_1018662_diff_roll9_sqmean',
                         'wl_1018662_absdiff_roll9_max', 'wl_1018662_absdiff_roll9_min', 'wl_1018662_roll12_mean',
                         'wl_1018662_roll12_median', 'wl_1018662_roll12_std', 'wl_1018662_roll12_max',
                         'wl_1018662_roll12_min', 'wl_1018662_absdiff_roll12_mean', 'wl_1018662_diff_roll12_sqmean',
                         'wl_1018662_absdiff_roll12_max', 'wl_1018662_absdiff_roll12_min', 'wl_1018662_roll15_mean',
                         'wl_1018662_roll15_std', 'wl_1018662_roll15_min', 'wl_1018662_absdiff_roll15_mean',
                         'wl_1018662_diff_roll15_sqmean', 'wl_1018662_absdiff_roll15_max',
                         'wl_1018662_absdiff_roll15_min', 'wl_1018662_roll18_mean', 'wl_1018662_roll18_median',
                         'wl_1018662_roll18_std', 'wl_1018662_roll18_max', 'wl_1018662_roll18_min',
                         'wl_1018662_absdiff_roll18_mean', 'wl_1018662_diff_roll18_sqmean',
                         'wl_1018662_absdiff_roll18_max', 'wl_1018662_absdiff_roll18_min', 'fw_1018662_s1',
                         'fw_1018662_diff1_s1', 'fw_1018662_diff2_s1', 'fw_1018662_s2', 'fw_1018662_diff1_s2',
                         'fw_1018662_diff2_s2', 'fw_1018662_diff1_s3', 'fw_1018662_diff2_s3', 'fw_1018662_s4',
                         'fw_1018662_diff1_s4', 'fw_1018662_diff2_s4', 'fw_1018662_s5', 'fw_1018662_diff1_s5',
                         'fw_1018662_diff2_s5', 'fw_1018662_s6', 'fw_1018662_diff1_s6', 'fw_1018662_s7',
                         'fw_1018662_diff1_s7', 'fw_1018662_diff2_s7', 'fw_1018662_s8', 'fw_1018662_diff1_s8',
                         'fw_1018662_diff2_s8', 'fw_1018662_s9', 'fw_1018662_diff2_s9', 'fw_1018662_s10',
                         'fw_1018662_diff2_s10', 'fw_1018662_s11', 'fw_1018662_diff1_s11', 'fw_1018662_diff2_s11',
                         'fw_1018662_s12', 'fw_1018662_diff1_s12', 'fw_1018662_diff2_s12', 'fw_1018662_roll3_std',
                         'fw_1018662_roll3_max', 'fw_1018662_roll3_min', 'fw_1018662_absdiff_roll3_mean',
                         'fw_1018662_absdiff_roll3_max', 'fw_1018662_absdiff_roll3_min', 'fw_1018662_roll6_median',
                         'fw_1018662_roll6_std', 'fw_1018662_roll6_max', 'fw_1018662_roll6_min',
                         'fw_1018662_diff_roll6_sqmean', 'fw_1018662_absdiff_roll6_max', 'fw_1018662_roll9_mean',
                         'fw_1018662_roll9_std', 'fw_1018662_roll9_max', 'fw_1018662_roll9_min',
                         'fw_1018662_diff_roll9_sqmean', 'fw_1018662_absdiff_roll9_max', 'fw_1018662_roll12_std',
                         'fw_1018662_roll12_min', 'fw_1018662_diff_roll12_sqmean', 'fw_1018662_absdiff_roll12_max',
                         'fw_1018662_roll15_median', 'fw_1018662_roll15_std', 'fw_1018662_roll15_max',
                         'fw_1018662_roll15_min', 'fw_1018662_diff_roll15_sqmean', 'fw_1018662_absdiff_roll15_max',
                         'fw_1018662_roll18_mean', 'fw_1018662_roll18_std', 'fw_1018662_roll18_min',
                         'fw_1018662_absdiff_roll18_mean', 'fw_1018662_absdiff_roll18_max', 'wl_1018680_s1',
                         'wl_1018680_diff1_s1', 'wl_1018680_diff2_s1', 'wl_1018680_s2', 'wl_1018680_diff1_s2',
                         'wl_1018680_diff2_s2', 'wl_1018680_s3', 'wl_1018680_diff1_s3', 'wl_1018680_diff2_s3',
                         'wl_1018680_s4', 'wl_1018680_diff1_s4', 'wl_1018680_diff2_s4', 'wl_1018680_s5',
                         'wl_1018680_diff1_s5', 'wl_1018680_diff2_s5', 'wl_1018680_s6', 'wl_1018680_diff1_s6',
                         'wl_1018680_diff2_s6', 'wl_1018680_s7', 'wl_1018680_diff1_s7', 'wl_1018680_diff2_s7',
                         'wl_1018680_s8', 'wl_1018680_diff1_s8', 'wl_1018680_diff2_s8', 'wl_1018680_s9',
                         'wl_1018680_diff1_s9', 'wl_1018680_diff2_s9', 'wl_1018680_s10', 'wl_1018680_diff1_s10',
                         'wl_1018680_diff2_s10', 'wl_1018680_s11', 'wl_1018680_diff2_s11', 'wl_1018680_s12',
                         'wl_1018680_diff2_s12', 'wl_1018680_roll3_mean', 'wl_1018680_roll3_median',
                         'wl_1018680_roll3_std', 'wl_1018680_roll3_max', 'wl_1018680_roll3_min',
                         'wl_1018680_absdiff_roll3_mean', 'wl_1018680_diff_roll3_sqmean',
                         'wl_1018680_absdiff_roll3_max', 'wl_1018680_roll6_mean', 'wl_1018680_roll6_std',
                         'wl_1018680_roll6_max', 'wl_1018680_roll6_min', 'wl_1018680_absdiff_roll6_mean',
                         'wl_1018680_diff_roll6_sqmean', 'wl_1018680_absdiff_roll6_max', 'wl_1018680_absdiff_roll6_min',
                         'wl_1018680_roll9_mean', 'wl_1018680_roll9_median', 'wl_1018680_roll9_std',
                         'wl_1018680_roll9_max', 'wl_1018680_roll9_min', 'wl_1018680_absdiff_roll9_mean',
                         'wl_1018680_diff_roll9_sqmean', 'wl_1018680_roll12_mean', 'wl_1018680_roll12_std',
                         'wl_1018680_roll12_max', 'wl_1018680_roll12_min', 'wl_1018680_absdiff_roll12_mean',
                         'wl_1018680_diff_roll12_sqmean', 'wl_1018680_absdiff_roll12_max',
                         'wl_1018680_absdiff_roll12_min', 'wl_1018680_roll15_std', 'wl_1018680_roll15_max',
                         'wl_1018680_roll15_min', 'wl_1018680_absdiff_roll15_mean', 'wl_1018680_absdiff_roll15_max',
                         'wl_1018680_roll18_mean', 'wl_1018680_roll18_std', 'wl_1018680_roll18_max',
                         'wl_1018680_roll18_min', 'wl_1018680_absdiff_roll18_mean', 'wl_1018680_diff_roll18_sqmean',
                         'wl_1018680_absdiff_roll18_max', 'wl_1018683_s1', 'wl_1018683_diff1_s1', 'wl_1018683_diff2_s1',
                         'wl_1018683_s2', 'wl_1018683_diff1_s2', 'wl_1018683_diff2_s2', 'wl_1018683_s3',
                         'wl_1018683_diff1_s3', 'wl_1018683_diff2_s3', 'wl_1018683_s4', 'wl_1018683_diff1_s4',
                         'wl_1018683_diff2_s4', 'wl_1018683_diff1_s5', 'wl_1018683_diff2_s5', 'wl_1018683_s6',
                         'wl_1018683_diff1_s6', 'wl_1018683_diff2_s6', 'wl_1018683_diff1_s7', 'wl_1018683_diff2_s7',
                         'wl_1018683_s8', 'wl_1018683_diff1_s8', 'wl_1018683_diff2_s8', 'wl_1018683_s9',
                         'wl_1018683_diff1_s9', 'wl_1018683_diff2_s9', 'wl_1018683_s10', 'wl_1018683_diff2_s10',
                         'wl_1018683_s11', 'wl_1018683_diff1_s11', 'wl_1018683_diff2_s11', 'wl_1018683_s12',
                         'wl_1018683_diff2_s12', 'wl_1018683_roll3_mean', 'wl_1018683_roll3_median',
                         'wl_1018683_roll3_std', 'wl_1018683_roll3_max', 'wl_1018683_roll3_min',
                         'wl_1018683_absdiff_roll3_mean', 'wl_1018683_diff_roll3_sqmean',
                         'wl_1018683_absdiff_roll3_max', 'wl_1018683_absdiff_roll3_min', 'wl_1018683_roll6_mean',
                         'wl_1018683_roll6_std', 'wl_1018683_roll6_max', 'wl_1018683_roll6_min',
                         'wl_1018683_absdiff_roll6_mean', 'wl_1018683_diff_roll6_sqmean',
                         'wl_1018683_absdiff_roll6_max', 'wl_1018683_absdiff_roll6_min', 'wl_1018683_roll9_median',
                         'wl_1018683_roll9_std', 'wl_1018683_roll9_max', 'wl_1018683_roll9_min',
                         'wl_1018683_absdiff_roll9_mean', 'wl_1018683_diff_roll9_sqmean',
                         'wl_1018683_absdiff_roll9_max', 'wl_1018683_absdiff_roll9_min', 'wl_1018683_roll12_mean',
                         'wl_1018683_roll12_median', 'wl_1018683_roll12_std', 'wl_1018683_roll12_max',
                         'wl_1018683_roll12_min', 'wl_1018683_absdiff_roll12_mean', 'wl_1018683_absdiff_roll12_max',
                         'wl_1018683_roll15_mean', 'wl_1018683_roll15_median', 'wl_1018683_roll15_std',
                         'wl_1018683_roll15_max', 'wl_1018683_roll15_min', 'wl_1018683_absdiff_roll15_mean',
                         'wl_1018683_diff_roll15_sqmean', 'wl_1018683_roll18_mean', 'wl_1018683_roll18_median',
                         'wl_1018683_roll18_std', 'wl_1018683_roll18_min', 'wl_1018683_absdiff_roll18_mean',
                         'wl_1018683_diff_roll18_sqmean', 'fw_1018683_s1', 'fw_1018683_diff1_s1', 'fw_1018683_diff2_s1',
                         'fw_1018683_s2', 'fw_1018683_diff1_s2', 'fw_1018683_diff2_s2', 'fw_1018683_diff1_s3',
                         'fw_1018683_diff2_s3', 'fw_1018683_diff1_s4', 'fw_1018683_diff2_s4', 'fw_1018683_s5',
                         'fw_1018683_diff1_s5', 'fw_1018683_diff2_s5', 'fw_1018683_s6', 'fw_1018683_diff1_s6',
                         'fw_1018683_diff2_s6', 'fw_1018683_s7', 'fw_1018683_diff1_s7', 'fw_1018683_diff2_s7',
                         'fw_1018683_s8', 'fw_1018683_diff1_s8', 'fw_1018683_diff2_s8', 'fw_1018683_s9',
                         'fw_1018683_diff1_s9', 'fw_1018683_diff2_s9', 'fw_1018683_s10', 'fw_1018683_diff2_s10',
                         'fw_1018683_s11', 'fw_1018683_diff1_s11', 'fw_1018683_diff2_s11', 'fw_1018683_s12',
                         'fw_1018683_diff1_s12', 'fw_1018683_diff2_s12', 'fw_1018683_roll3_mean',
                         'fw_1018683_roll3_median', 'fw_1018683_roll3_std', 'fw_1018683_roll3_max',
                         'fw_1018683_roll3_min', 'fw_1018683_absdiff_roll3_mean', 'fw_1018683_diff_roll3_sqmean',
                         'fw_1018683_absdiff_roll3_max', 'fw_1018683_absdiff_roll3_min', 'fw_1018683_roll6_mean',
                         'fw_1018683_roll6_median', 'fw_1018683_roll6_std', 'fw_1018683_roll6_max',
                         'fw_1018683_roll6_min', 'fw_1018683_absdiff_roll6_mean', 'fw_1018683_diff_roll6_sqmean',
                         'fw_1018683_absdiff_roll6_max', 'fw_1018683_absdiff_roll6_min', 'fw_1018683_roll9_mean',
                         'fw_1018683_roll9_median', 'fw_1018683_roll9_std', 'fw_1018683_roll9_max',
                         'fw_1018683_roll9_min', 'fw_1018683_absdiff_roll9_mean', 'fw_1018683_diff_roll9_sqmean',
                         'fw_1018683_absdiff_roll9_max', 'fw_1018683_roll12_mean', 'fw_1018683_roll12_std',
                         'fw_1018683_roll12_max', 'fw_1018683_roll12_min', 'fw_1018683_diff_roll12_sqmean',
                         'fw_1018683_absdiff_roll12_max', 'fw_1018683_roll15_mean', 'fw_1018683_roll15_median',
                         'fw_1018683_roll15_std', 'fw_1018683_roll15_max', 'fw_1018683_roll15_min',
                         'fw_1018683_roll18_mean', 'fw_1018683_roll18_median', 'fw_1018683_roll18_std',
                         'fw_1018683_roll18_max', 'fw_1018683_roll18_min', 'fw_1018683_absdiff_roll18_mean',
                         'fw_1018683_diff_roll18_sqmean', 'fw_1018683_absdiff_roll18_max', 'wl_1019630_s1',
                         'wl_1019630_diff1_s1', 'wl_1019630_diff2_s1', 'wl_1019630_s2', 'wl_1019630_diff1_s2',
                         'wl_1019630_diff2_s2', 'wl_1019630_s3', 'wl_1019630_diff1_s3', 'wl_1019630_diff2_s3',
                         'wl_1019630_s4', 'wl_1019630_diff1_s4', 'wl_1019630_diff2_s4', 'wl_1019630_s5',
                         'wl_1019630_diff1_s5', 'wl_1019630_diff2_s5', 'wl_1019630_s6', 'wl_1019630_diff1_s6',
                         'wl_1019630_diff2_s6', 'wl_1019630_diff1_s7', 'wl_1019630_diff2_s7', 'wl_1019630_s8',
                         'wl_1019630_diff1_s8', 'wl_1019630_diff2_s8', 'wl_1019630_s9', 'wl_1019630_diff1_s9',
                         'wl_1019630_diff2_s9', 'wl_1019630_s10', 'wl_1019630_diff1_s10', 'wl_1019630_diff2_s10',
                         'wl_1019630_s11', 'wl_1019630_diff1_s11', 'wl_1019630_diff2_s11', 'wl_1019630_s12',
                         'wl_1019630_diff1_s12', 'wl_1019630_diff2_s12', 'wl_1019630_roll3_mean',
                         'wl_1019630_roll3_median', 'wl_1019630_roll3_std', 'wl_1019630_roll3_max',
                         'wl_1019630_roll3_min', 'wl_1019630_absdiff_roll3_mean', 'wl_1019630_diff_roll3_sqmean',
                         'wl_1019630_absdiff_roll3_max', 'wl_1019630_absdiff_roll3_min', 'wl_1019630_roll6_median',
                         'wl_1019630_roll6_std', 'wl_1019630_roll6_max', 'wl_1019630_roll6_min',
                         'wl_1019630_absdiff_roll6_mean', 'wl_1019630_diff_roll6_sqmean',
                         'wl_1019630_absdiff_roll6_max', 'wl_1019630_absdiff_roll6_min', 'wl_1019630_roll9_mean',
                         'wl_1019630_roll9_std', 'wl_1019630_roll9_max', 'wl_1019630_roll9_min',
                         'wl_1019630_absdiff_roll9_mean', 'wl_1019630_diff_roll9_sqmean',
                         'wl_1019630_absdiff_roll9_max', 'wl_1019630_absdiff_roll9_min', 'wl_1019630_roll12_mean',
                         'wl_1019630_roll12_median', 'wl_1019630_roll12_std', 'wl_1019630_roll12_max',
                         'wl_1019630_roll12_min', 'wl_1019630_absdiff_roll12_mean', 'wl_1019630_diff_roll12_sqmean',
                         'wl_1019630_absdiff_roll12_max', 'wl_1019630_roll15_mean', 'wl_1019630_roll15_median',
                         'wl_1019630_roll15_std', 'wl_1019630_roll15_max', 'wl_1019630_roll15_min',
                         'wl_1019630_absdiff_roll15_mean', 'wl_1019630_diff_roll15_sqmean',
                         'wl_1019630_absdiff_roll15_max', 'wl_1019630_roll18_mean', 'wl_1019630_roll18_median',
                         'wl_1019630_roll18_std', 'wl_1019630_roll18_max', 'wl_1019630_roll18_min',
                         'wl_1019630_absdiff_roll18_mean', 'wl_1019630_diff_roll18_sqmean',
                         'wl_1019630_absdiff_roll18_max', 'fw_1019630_s1', 'fw_1019630_diff1_s1', 'fw_1019630_diff2_s1',
                         'fw_1019630_s2', 'fw_1019630_diff1_s2', 'fw_1019630_diff2_s2', 'fw_1019630_s3',
                         'fw_1019630_diff1_s3', 'fw_1019630_diff2_s3', 'fw_1019630_s4', 'fw_1019630_diff1_s4',
                         'fw_1019630_diff2_s4', 'fw_1019630_s5', 'fw_1019630_diff1_s5', 'fw_1019630_diff2_s5',
                         'fw_1019630_s6', 'fw_1019630_diff2_s6', 'fw_1019630_s7', 'fw_1019630_diff1_s7',
                         'fw_1019630_diff2_s7', 'fw_1019630_s8', 'fw_1019630_diff1_s8', 'fw_1019630_diff2_s8',
                         'fw_1019630_s9', 'fw_1019630_diff1_s9', 'fw_1019630_diff2_s9', 'fw_1019630_s10',
                         'fw_1019630_diff1_s10', 'fw_1019630_diff2_s10', 'fw_1019630_diff1_s11', 'fw_1019630_diff2_s11',
                         'fw_1019630_s12', 'fw_1019630_diff1_s12', 'fw_1019630_diff2_s12', 'fw_1019630_roll3_mean',
                         'fw_1019630_roll3_median', 'fw_1019630_roll3_std', 'fw_1019630_roll3_max',
                         'fw_1019630_roll3_min', 'fw_1019630_absdiff_roll3_mean', 'fw_1019630_diff_roll3_sqmean',
                         'fw_1019630_absdiff_roll3_max', 'fw_1019630_absdiff_roll3_min', 'fw_1019630_roll6_mean',
                         'fw_1019630_roll6_median', 'fw_1019630_roll6_std', 'fw_1019630_roll6_max',
                         'fw_1019630_roll6_min', 'fw_1019630_absdiff_roll6_mean', 'fw_1019630_absdiff_roll6_max',
                         'fw_1019630_absdiff_roll6_min', 'fw_1019630_roll9_mean', 'fw_1019630_roll9_std',
                         'fw_1019630_roll9_max', 'fw_1019630_absdiff_roll9_max', 'fw_1019630_roll12_median',
                         'fw_1019630_roll12_std', 'fw_1019630_roll12_min', 'fw_1019630_absdiff_roll12_mean',
                         'fw_1019630_absdiff_roll12_max', 'fw_1019630_roll15_median', 'fw_1019630_roll15_std',
                         'fw_1019630_roll15_max', 'fw_1019630_roll15_min', 'fw_1019630_absdiff_roll15_mean',
                         'fw_1019630_diff_roll15_sqmean', 'fw_1019630_absdiff_roll15_max', 'fw_1019630_roll18_mean',
                         'fw_1019630_roll18_median', 'fw_1019630_roll18_std', 'fw_1019630_roll18_max',
                         'fw_1019630_roll18_min', 'wl_1018640_s1', 'wl_1018640_diff2_s1', 'wl_1018640_s2',
                         'wl_1018640_diff1_s2', 'wl_1018640_diff2_s2', 'wl_1018640_s3', 'wl_1018640_diff1_s3',
                         'wl_1018640_diff2_s3', 'wl_1018640_s4', 'wl_1018640_diff2_s4', 'wl_1018640_s5',
                         'wl_1018640_diff2_s5', 'wl_1018640_diff1_s6', 'wl_1018640_s7', 'wl_1018640_s8',
                         'wl_1018640_diff2_s8', 'wl_1018640_s9', 'wl_1018640_s10', 'wl_1018640_diff1_s10',
                         'wl_1018640_s12', 'wl_1018640_roll3_mean', 'wl_1018640_roll3_median', 'wl_1018640_roll3_max',
                         'wl_1018640_roll3_min', 'wl_1018640_roll6_mean', 'wl_1018640_roll6_median',
                         'wl_1018640_roll6_max', 'wl_1018640_roll6_min', 'wl_1018640_diff_roll6_sqmean',
                         'wl_1018640_roll9_median', 'wl_1018640_roll9_max', 'wl_1018640_roll9_min',
                         'wl_1018640_roll12_mean', 'wl_1018640_roll12_max', 'wl_1018640_roll12_min',
                         'wl_1018640_absdiff_roll12_mean', 'wl_1018640_diff_roll12_sqmean', 'wl_1018640_roll15_mean',
                         'wl_1018640_roll15_min', 'wl_1018640_absdiff_roll15_max', 'wl_1018640_roll18_mean',
                         'wl_1018640_roll18_median', 'wl_1018640_roll18_max', 'wl_1018640_roll18_min', 'fw_1018640_s1',
                         'fw_1018640_diff2_s1', 'fw_1018640_diff2_s2', 'fw_1018640_s4', 'fw_1018640_diff1_s4',
                         'fw_1018640_s5', 'fw_1018640_s6', 'fw_1018640_diff2_s6', 'fw_1018640_diff2_s7',
                         'fw_1018640_s10', 'fw_1018640_diff2_s10', 'fw_1018640_s11', 'fw_1018640_s12',
                         'fw_1018640_diff2_s12', 'fw_1018640_roll3_mean', 'fw_1018640_roll3_min',
                         'fw_1018640_roll6_mean', 'fw_1018640_roll6_median', 'fw_1018640_roll6_std',
                         'fw_1018640_roll6_min', 'fw_1018640_roll9_median', 'fw_1018640_roll9_std',
                         'fw_1018640_roll9_min', 'fw_1018640_roll12_mean', 'fw_1018640_roll12_std',
                         'fw_1018640_roll12_min', 'fw_1018640_absdiff_roll12_min', 'fw_1018640_roll15_mean',
                         'fw_1018640_roll15_median', 'fw_1018640_roll15_std', 'fw_1018640_roll15_max',
                         'fw_1018640_roll15_min', 'fw_1018640_absdiff_roll15_mean', 'fw_1018640_absdiff_roll15_max',
                         'fw_1018640_roll18_min', 'fw_1018640_absdiff_roll18_mean', 'wl_1018670_roll9_std',
                         'wl_1018670_roll12_mean', 'fw_1018670_absdiff_roll12_min', 'fw_1018670_absdiff_roll18_mean',
                         'fw_1018670_absdiff_roll18_max', 'wl_1018675_s1', 'wl_1018675_diff1_s1',
                         'wl_1018675_diff2_s10', 'wl_1018675_diff1_s11', 'wl_1018675_diff2_s12',
                         'wl_1018675_roll3_median', 'wl_1018675_roll3_std', 'wl_1018675_absdiff_roll12_max',
                         'wl_1018675_roll18_std', 'wl_1018675_absdiff_roll18_mean', 'fw_1018675_diff1_s3',
                         'fw_1018675_roll3_std', 'fw_1018675_roll3_max', 'wl_1018695_s1',
                         'wl_1018695_absdiff_roll3_max', 'wl_1018695_roll6_std', 'wl_1018695_diff_roll9_sqmean',
                         'wl_1018695_roll18_mean', 'wl_1018695_roll18_std', 'wl_1018695_roll18_min',
                         'wl_1018695_absdiff_roll18_mean', 'fw_1018695_diff1_s3', 'fw_1018695_roll3_std',
                         'fw_1018695_roll6_std', 'fw_1018695_roll9_std', 'wl_1018697_s1', 'wl_1018697_diff1_s1',
                         'wl_1018697_diff2_s1', 'wl_1018697_s2', 'wl_1018697_diff2_s2', 'wl_1018697_diff2_s4',
                         'wl_1018697_diff2_s5', 'wl_1018697_s7', 'wl_1018697_s8', 'wl_1018697_s9', 'wl_1018697_s10',
                         'wl_1018697_s11', 'wl_1018697_s12', 'wl_1018697_roll3_max', 'wl_1018697_roll3_min',
                         'wl_1018697_absdiff_roll3_max', 'wl_1018697_absdiff_roll3_min', 'wl_1018697_roll6_max',
                         'wl_1018697_absdiff_roll6_mean', 'wl_1018697_absdiff_roll6_min', 'wl_1018697_roll9_median',
                         'wl_1018697_absdiff_roll9_max', 'wl_1018697_absdiff_roll9_min', 'wl_1018697_roll12_min',
                         'wl_1018697_roll15_median', 'wl_1018697_roll15_min', 'wl_1018697_absdiff_roll15_max',
                         'wl_1018697_absdiff_roll15_min', 'wl_1018697_roll18_mean', 'wl_1018697_roll18_max',
                         'wl_1018697_roll18_min', 'wl_1018697_absdiff_roll18_mean', 'fw_1018697_s1',
                         'fw_1018697_diff1_s1', 'fw_1018697_diff2_s1', 'fw_1018697_diff2_s2', 'fw_1018697_diff1_s3',
                         'fw_1018697_diff2_s4', 'fw_1018697_diff1_s5', 'fw_1018697_diff2_s5', 'fw_1018697_diff1_s9',
                         'fw_1018697_roll3_std', 'fw_1018697_roll3_min', 'fw_1018697_absdiff_roll3_mean',
                         'fw_1018697_roll6_std', 'fw_1018697_roll9_mean', 'fw_1018697_roll9_min',
                         'fw_1018697_absdiff_roll12_mean', 'fw_1018697_roll15_min', 'fw_1018697_roll18_max',
                         'fw_1018697_roll18_min', 'wl_1007605_s1', 'wl_1007605_s9', 'wl_1007605_s11', 'wl_1007605_s12',
                         'wl_1007605_roll9_std', 'wl_1007605_roll15_min', 'wl_1007605_roll18_min',
                         'fw_1007605_roll3_std', 'fw_1007605_absdiff_roll12_max', 'fw_1007605_roll15_min',
                         'fw_1007605_roll18_std', 'wl_1007615_s1', 'wl_1007615_s7', 'wl_1007615_s8',
                         'wl_1007615_roll3_std', 'wl_1007615_roll9_std', 'wl_1007615_roll12_min',
                         'wl_1007615_roll18_max', 'fw_1007615_s5', 'fw_1007615_roll3_std',
                         'fw_1007615_absdiff_roll9_max', 'wl_1007617_s4', 'fw_1007617_s4',
                         'fw_1007617_absdiff_roll3_min', 'wl_1007620_absdiff_roll9_mean', 'wl_1007620_roll12_max',
                         'wl_1007625_s1', 'wl_1007625_diff2_s2', 'wl_1007625_roll6_std', 'wl_1007625_roll9_mean',
                         'wl_1007625_absdiff_roll9_mean', 'wl_1007625_absdiff_roll15_max', 'fw_1007625_s1',
                         'fw_1007625_diff2_s1', 'fw_1007625_diff2_s2', 'fw_1007625_diff1_s3', 'fw_1007625_diff2_s3',
                         'fw_1007625_s4', 'fw_1007625_diff1_s4', 'fw_1007625_diff2_s4', 'fw_1007625_s6',
                         'fw_1007625_diff1_s8', 'fw_1007625_diff2_s8', 'fw_1007625_diff1_s9', 'fw_1007625_s11',
                         'fw_1007625_diff1_s11', 'fw_1007625_diff2_s11', 'fw_1007625_diff_roll3_sqmean',
                         'fw_1007625_absdiff_roll3_max', 'fw_1007625_roll6_mean', 'fw_1007625_roll6_std',
                         'fw_1007625_roll6_min', 'fw_1007625_diff_roll6_sqmean', 'fw_1007625_roll9_min',
                         'fw_1007625_absdiff_roll9_mean', 'fw_1007625_absdiff_roll9_max', 'fw_1007625_roll12_mean',
                         'fw_1007625_absdiff_roll12_max', 'fw_1007625_roll15_mean', 'fw_1007625_roll15_median',
                         'fw_1007625_roll15_std', 'fw_1007625_roll18_max', 'fw_1007625_absdiff_roll18_max',
                         'wl_1007630_diff2_s2', 'wl_1007630_roll9_std', 'wl_1007633_diff1_s2', 'wl_1007633_diff2_s3',
                         'wl_1007633_diff1_s4', 'wl_1007633_diff2_s7', 'wl_1007633_diff1_s10', 'wl_1007633_roll3_max',
                         'wl_1007633_roll18_std', 'wl_1007634_diff2_s1', 'wl_1007634_s7', 'wl_1007634_diff2_s10',
                         'wl_1007634_diff1_s11', 'wl_1007634_s12', 'wl_1007634_diff1_s12', 'wl_1007634_diff2_s12',
                         'wl_1007634_roll6_min', 'wl_1007634_diff_roll6_sqmean', 'wl_1007634_roll9_mean',
                         'wl_1007634_absdiff_roll12_mean', 'wl_1007635_s3', 'wl_1007635_diff2_s3', 'wl_1007635_s6',
                         'wl_1007635_roll3_std', 'fw_1007635_s1', 'fw_1007635_diff2_s2', 'fw_1007635_diff1_s5',
                         'fw_1007635_s6', 'fw_1007635_diff1_s6', 'fw_1007635_s7', 'fw_1007635_diff2_s7',
                         'fw_1007635_diff1_s9', 'fw_1007635_diff1_s10', 'fw_1007635_s11', 'fw_1007635_diff1_s11',
                         'fw_1007635_diff1_s12', 'fw_1007635_diff2_s12', 'fw_1007635_roll3_mean',
                         'fw_1007635_roll6_std', 'fw_1007635_diff_roll6_sqmean', 'fw_1007635_roll9_median',
                         'fw_1007635_roll9_std', 'fw_1007635_roll12_std', 'fw_1007635_roll15_mean',
                         'fw_1007635_roll15_min', 'wl_1007639_diff2_s5', 'wl_1007639_diff_roll9_sqmean',
                         'wl_1007639_roll18_max', 'wl_1007639_roll18_min', 'wl_1007640_diff2_s8', 'fw_1007640_diff1_s1',
                         'fw_1007640_s3', 'fw_1007640_diff1_s4', 'fw_1007640_roll3_std', 'fw_1007640_roll9_std',
                         'fw_1007640_roll15_std', 'wl_1007641_diff2_s11', 'wl_1007641_roll3_mean',
                         'wl_1007641_absdiff_roll3_mean', 'wl_1007641_roll6_min', 'wl_1007641_roll9_std',
                         'wl_1007641_roll12_mean', 'wl_1007641_roll12_std', 'wl_1007641_absdiff_roll15_mean',
                         'wl_1007645_s2', 'wl_1007645_roll6_std', 'wl_1007645_roll15_std', 'wl_1007645_roll18_max',
                         'fw_1007645_roll6_std', 'fw_1007645_roll9_std', 'wl_1007649_diff2_s1', 'wl_1007649_s3',
                         'wl_1007649_s4', 'wl_1007649_diff1_s5', 'wl_1007649_s8', 'wl_1007649_s10',
                         'wl_1007649_diff1_s12', 'wl_1007649_roll12_mean', 'wl_1007650_diff1_s1', 'wl_1007650_diff2_s1',
                         'wl_1007650_diff1_s2', 'wl_1007650_diff2_s6', 'wl_1007650_absdiff_roll3_mean',
                         'wl_1007650_absdiff_roll6_mean', 'wl_1007650_roll9_min', 'wl_1007650_roll15_std',
                         'fw_1007650_s2', 'fw_1007650_roll15_max', 'fw_1007650_absdiff_roll15_mean',
                         'fw_1007650_roll18_std', 'wl_1007655_s6', 'wl_1007655_diff2_s7', 'wl_1007655_s10',
                         'wl_1007655_roll9_median', 'wl_1007655_roll9_std', 'wl_1007655_roll18_min', 'fw_1007655_s5',
                         'fw_1007655_roll6_min', 'wl_1007660_s12', 'wl_1007660_roll12_std', 'wl_1007660_roll15_std',
                         'wl_1007660_diff_roll15_sqmean', 'fw_1007660_s1', 'fw_1007660_diff1_s1', 'fw_1007660_diff2_s1',
                         'fw_1007660_diff1_s2', 'fw_1007660_s4', 'fw_1007660_diff1_s4', 'fw_1007660_s6',
                         'fw_1007660_diff1_s6', 'fw_1007660_diff2_s6', 'fw_1007660_diff1_s8', 'fw_1007660_diff1_s9',
                         'fw_1007660_s10', 'fw_1007660_diff1_s10', 'fw_1007660_s11', 'fw_1007660_diff1_s12',
                         'fw_1007660_diff2_s12', 'fw_1007660_absdiff_roll6_mean', 'fw_1007660_roll9_std',
                         'fw_1007660_roll12_median', 'fw_1007660_roll12_std', 'fw_1007660_roll12_max',
                         'fw_1007660_absdiff_roll12_mean', 'fw_1007660_roll15_mean', 'fw_1007660_roll15_max',
                         'fw_1007660_absdiff_roll15_mean', 'fw_1007660_diff_roll15_sqmean', 'fw_1007660_roll18_mean',
                         'fw_1007660_roll18_median', 'fw_1007660_roll18_max', 'fw_1007660_diff_roll18_sqmean',
                         'wl_1007662_diff1_s4', 'wl_1007662_s9', 'wl_1007662_roll6_max', 'wl_1007662_roll15_max',
                         'wl_1007662_roll18_max', 'wl_1007664_diff1_s3', 'wl_1007664_s6', 'wl_1007664_diff1_s6',
                         'wl_1007664_diff2_s6', 'wl_1007664_diff1_s8', 'wl_1007664_s9', 'wl_1007664_diff2_s10',
                         'wl_1007664_diff1_s11', 'wl_1007664_diff2_s11', 'wl_1007664_absdiff_roll3_mean',
                         'wl_1007664_roll6_std', 'wl_1007664_roll9_std', 'wl_1007664_roll12_median',
                         'wl_1007664_diff_roll12_sqmean', 'wl_1007664_roll15_std', 'wl_1007664_roll15_min',
                         'wl_1007680_roll3_std', 'wl_1007680_roll6_std', 'wl_1007680_roll18_max',
                         'fw_1007680_diff1_s10', 'fw_1007680_diff2_s11', 'fw_1007680_roll15_std',
                         'fw_1007680_absdiff_roll15_mean', 'fw_1007680_absdiff_roll18_max', 'wl_1007685_s1',
                         'wl_1007685_s3', 'wl_1007685_s4', 'wl_1007685_s9', 'wl_1007685_s10', 'wl_1007685_s11',
                         'wl_1007685_roll3_max', 'wl_1007685_roll3_min', 'wl_1007685_absdiff_roll3_mean',
                         'wl_1007685_roll6_std', 'wl_1007685_diff_roll6_sqmean', 'wl_1007685_roll9_min',
                         'wl_1007685_roll12_mean', 'wl_1007685_roll12_max', 'wl_1007685_roll15_max',
                         'wl_1007685_roll15_min', 'wl_1007685_roll18_max', 'wl_1007685_roll18_min',
                         'wl_1007685_absdiff_roll18_mean', 'fw_1007685_s1', 'fw_1007685_diff1_s1', 'fw_1007685_s2',
                         'fw_1007685_diff1_s2', 'fw_1007685_diff2_s2', 'fw_1007685_s3', 'fw_1007685_diff1_s3',
                         'fw_1007685_diff2_s3', 'fw_1007685_diff1_s5', 'fw_1007685_diff2_s6', 'fw_1007685_s7',
                         'fw_1007685_diff2_s8', 'fw_1007685_s9', 'fw_1007685_diff2_s9', 'fw_1007685_s10',
                         'fw_1007685_diff1_s10', 'fw_1007685_s11', 'fw_1007685_diff2_s11', 'fw_1007685_diff1_s12',
                         'fw_1007685_roll3_mean', 'fw_1007685_roll3_median', 'fw_1007685_roll3_max',
                         'fw_1007685_absdiff_roll3_max', 'fw_1007685_roll6_std', 'fw_1007685_absdiff_roll6_mean',
                         'fw_1007685_roll9_mean', 'fw_1007685_roll9_std', 'fw_1007685_roll9_min',
                         'fw_1007685_absdiff_roll9_mean', 'fw_1007685_absdiff_roll9_max',
                         'fw_1007685_diff_roll12_sqmean', 'fw_1007685_roll15_std', 'fw_1007685_roll15_min',
                         'fw_1007685_absdiff_roll15_mean', 'fw_1007685_absdiff_roll15_min', 'fw_1007685_roll18_std',
                         'fw_1007685_absdiff_roll18_mean', 'fw_1007685_absdiff_roll18_max', 'wl_1007690_s1',
                         'wl_1007690_diff2_s6', 'wl_1007690_s10', 'wl_1007690_roll3_mean', 'wl_1007690_roll3_std',
                         'wl_1007690_roll3_max', 'wl_1007690_roll18_min', 'fw_1007690_s5', 'fw_1007690_diff2_s7',
                         'fw_1007690_diff1_s11', 'fw_1007690_diff2_s11', 'fw_1007690_roll15_mean',
                         'fw_1007690_absdiff_roll18_max', 'wl_1013620_diff1_s4', 'wl_1013620_s5', 'wl_1013620_diff2_s5',
                         'wl_1013652_s4', 'wl_1013652_s6', 'wl_1013652_diff1_s6', 'wl_1013652_diff2_s8',
                         'wl_1013652_s9', 'wl_1013652_s11', 'wl_1013652_s12', 'wl_1013652_diff2_s12',
                         'wl_1013652_roll3_median', 'wl_1013652_roll3_std', 'wl_1013652_roll9_median',
                         'wl_1013652_roll9_max', 'wl_1013652_roll12_max', 'wl_1013652_roll18_median',
                         'wl_1013652_roll18_std', 'wl_1013655_s1', 'wl_1013655_diff1_s1', 'wl_1013655_diff1_s8',
                         'wl_1013655_diff2_s8', 'wl_1013655_s9', 'wl_1013655_roll9_std',
                         'wl_1013655_absdiff_roll12_max', 'wl_1013655_roll15_std', 'wl_1013655_roll18_std',
                         'fw_1013655_s1', 'fw_1013655_diff2_s7', 'fw_1013655_roll3_std', 'fw_1013655_roll12_std',
                         'wl_1015630_diff1_s1', 'wl_1015630_diff1_s2', 'wl_1015630_s3', 'wl_1015630_diff1_s9',
                         'wl_1015630_diff2_s9', 'wl_1015630_diff2_s12', 'wl_1015630_absdiff_roll3_mean',
                         'wl_1015630_roll6_std', 'wl_1015630_absdiff_roll18_mean', 'wl_1015630_diff_roll18_sqmean',
                         'wl_1015640_s1', 'wl_1015640_diff1_s1', 'wl_1015640_diff2_s1', 'wl_1015640_s2',
                         'wl_1015640_diff1_s2', 'wl_1015640_s4', 'wl_1015640_diff2_s5', 'wl_1015640_diff2_s6',
                         'wl_1015640_s7', 'wl_1015640_diff1_s9', 'wl_1015640_diff2_s9', 'wl_1015640_s10',
                         'wl_1015640_s12', 'wl_1015640_roll3_std', 'wl_1015640_absdiff_roll3_mean',
                         'wl_1015640_absdiff_roll6_mean', 'wl_1015640_diff_roll6_sqmean',
                         'wl_1015640_absdiff_roll6_max', 'wl_1015640_roll9_std', 'wl_1015640_roll9_max',
                         'wl_1015640_absdiff_roll9_mean', 'wl_1015640_absdiff_roll12_mean',
                         'wl_1015640_diff_roll12_sqmean', 'wl_1015640_roll15_median', 'wl_1015640_roll15_max',
                         'wl_1015640_roll18_mean', 'wl_1015640_absdiff_roll18_max', 'wl_1015644_s1',
                         'wl_1015644_diff1_s1', 'wl_1015644_diff2_s1', 'wl_1015644_s8', 'wl_1015644_s9',
                         'wl_1015644_s10', 'wl_1015644_diff2_s10', 'wl_1015644_s12', 'wl_1015644_diff1_s12',
                         'wl_1015644_roll3_median', 'wl_1015644_roll6_std', 'wl_1015644_roll6_min',
                         'wl_1015644_absdiff_roll6_max', 'wl_1015644_roll9_std', 'wl_1015644_roll9_min',
                         'wl_1015644_roll12_min', 'wl_1015644_roll15_mean', 'wl_1015644_roll15_std',
                         'wl_1015644_roll18_std', 'wl_1015644_roll18_max', 'wl_1015644_roll18_min',
                         'fw_1015644_diff1_s1', 'fw_1015644_diff1_s2', 'fw_1015644_diff2_s3', 'fw_1015644_diff1_s5',
                         'fw_1015644_diff1_s6', 'fw_1015644_diff1_s8', 'fw_1015644_s10', 'fw_1015644_diff1_s11',
                         'fw_1015644_roll3_std', 'fw_1015644_absdiff_roll6_max', 'fw_1015644_roll18_std',
                         'fw_1015644_absdiff_roll18_mean', 'wl_1015645_s1', 'wl_1015645_s3', 'wl_1015645_s4',
                         'wl_1015645_s5', 'wl_1015645_s7', 'wl_1015645_diff1_s7', 'wl_1015645_s9',
                         'wl_1015645_diff1_s9', 'wl_1015645_s11', 'wl_1015645_roll3_max', 'wl_1015645_roll3_min',
                         'wl_1015645_roll9_median', 'wl_1015645_roll12_max', 'wl_1015645_roll15_std',
                         'wl_1015645_roll15_min', 'wl_1015645_roll18_median', 'wl_1015645_roll18_min', 'fw_1015645_s4',
                         'fw_1015645_s5', 'fw_1015645_s7', 'fw_1015645_diff1_s7', 'fw_1015645_diff2_s7',
                         'fw_1015645_diff1_s8', 'fw_1015645_s9', 'fw_1015645_s12', 'fw_1015645_diff2_s12',
                         'fw_1015645_absdiff_roll6_mean', 'fw_1015645_diff_roll6_sqmean', 'fw_1015645_roll9_max',
                         'fw_1015645_roll9_min', 'fw_1015645_absdiff_roll9_max', 'fw_1015645_absdiff_roll15_mean',
                         'fw_1015645_roll18_max', 'fw_1015645_roll18_min', 'wl_1015680_s1', 'wl_1015680_s7',
                         'wl_1015680_s8', 'wl_1015680_s9', 'wl_1015680_s11', 'wl_1015680_diff2_s11', 'wl_1015680_s12',
                         'wl_1015680_roll3_std', 'wl_1015680_roll6_max', 'wl_1015680_roll9_mean',
                         'wl_1015680_roll9_std', 'wl_1015680_roll12_std', 'wl_1015680_roll12_min',
                         'wl_1015680_absdiff_roll12_mean', 'wl_1015680_roll15_mean', 'wl_1015680_roll15_median',
                         'wl_1015680_roll15_std', 'wl_1015680_roll15_min', 'wl_1015680_roll18_min',
                         'wl_1016607_diff1_s3', 'wl_1016607_s11', 'wl_1016607_roll3_std', 'wl_1016607_roll15_max',
                         'fw_1016607_s3', 'fw_1016607_roll3_mean', 'fw_1016607_roll9_std', 'wl_1016650_s1',
                         'wl_1016650_diff2_s1', 'wl_1016650_diff1_s2', 'wl_1016650_diff_roll3_sqmean',
                         'wl_1016650_absdiff_roll3_min', 'wl_1016650_absdiff_roll18_mean', 'fw_1016650_s1',
                         'fw_1016650_diff1_s1', 'fw_1016650_diff1_s12', 'wl_1016655_diff1_s2', 'wl_1016655_diff2_s2',
                         'wl_1016655_diff1_s3', 'wl_1016655_s8', 'wl_1016655_diff1_s11', 'wl_1016655_diff2_s11',
                         'wl_1016655_roll3_mean', 'wl_1016655_absdiff_roll3_mean', 'wl_1016655_diff_roll3_sqmean',
                         'wl_1016655_absdiff_roll3_max', 'wl_1016655_absdiff_roll9_max', 'wl_1016655_roll12_std',
                         'wl_1016655_absdiff_roll12_mean', 'wl_1016655_roll15_std', 'wl_1016660_roll3_std',
                         'wl_1016670_diff2_s1', 'wl_1016670_diff2_s3', 'wl_1016670_diff2_s10', 'wl_1016670_diff2_s12',
                         'wl_1016670_roll3_std', 'wl_1016670_diff_roll6_sqmean', 'wl_1016670_absdiff_roll6_max',
                         'wl_1016670_roll9_std', 'wl_1016670_absdiff_roll9_mean', 'wl_1016670_roll15_std',
                         'wl_1016670_roll18_std', 'wl_1016695_s1', 'wl_1016695_s3', 'wl_1016695_diff1_s9',
                         'wl_1016695_s10', 'wl_1016695_roll3_mean', 'wl_1016695_roll3_median', 'wl_1016695_roll3_max',
                         'wl_1016695_roll3_min', 'wl_1016695_roll9_min', 'wl_1016695_diff_roll9_sqmean',
                         'wl_1016695_roll12_median', 'wl_1016695_diff_roll18_sqmean', 'wl_1017690_s1',
                         'wl_1017690_diff2_s3', 'wl_1017690_s4', 'wl_1017690_diff2_s5', 'wl_1017690_diff2_s7',
                         'wl_1017690_s10', 'wl_1017690_roll3_mean', 'wl_1017690_roll3_median',
                         'wl_1017690_absdiff_roll3_mean', 'wl_1017690_absdiff_roll3_min',
                         'wl_1017690_absdiff_roll6_mean', 'wl_1017690_diff_roll6_sqmean',
                         'wl_1017690_absdiff_roll9_mean', 'wl_1017690_roll12_std', 'wl_1017690_roll12_min',
                         'wl_1017690_diff_roll12_sqmean', 'wl_1017690_roll15_std', 'wl_1017690_roll15_min',
                         'wl_1017690_absdiff_roll15_mean', 'wl_1017690_roll18_min', 'wl_1017690_absdiff_roll18_mean',
                         'wl_1018610_s1', 'wl_1018610_s2', 'wl_1018610_s4', 'wl_1018610_s5', 'wl_1018610_diff2_s5',
                         'wl_1018610_s6', 'wl_1018610_diff2_s6', 'wl_1018610_s7', 'wl_1018610_diff2_s7',
                         'wl_1018610_s12', 'wl_1018610_roll3_mean', 'wl_1018610_roll3_max', 'wl_1018610_roll3_min',
                         'wl_1018610_roll6_mean', 'wl_1018610_roll6_median', 'wl_1018610_roll6_max',
                         'wl_1018610_roll6_min', 'wl_1018610_roll9_mean', 'wl_1018610_roll9_median',
                         'wl_1018610_roll9_max', 'wl_1018610_roll9_min', 'wl_1018610_absdiff_roll9_mean',
                         'wl_1018610_roll12_mean', 'wl_1018610_roll12_std', 'wl_1018610_roll12_max',
                         'wl_1018610_roll12_min', 'wl_1018610_roll15_median', 'wl_1018610_roll15_max',
                         'wl_1018610_roll15_min', 'wl_1018610_roll18_mean', 'fw_1018610_s1', 'fw_1018610_s2',
                         'fw_1018610_diff1_s2', 'fw_1018610_s3', 'fw_1018610_diff1_s3', 'fw_1018610_s4',
                         'fw_1018610_diff2_s5', 'fw_1018610_s6', 'fw_1018610_diff2_s6', 'fw_1018610_s7',
                         'fw_1018610_diff2_s7', 'fw_1018610_s8', 'fw_1018610_diff2_s8', 'fw_1018610_s9',
                         'fw_1018610_s10', 'fw_1018610_diff2_s11', 'fw_1018610_s12', 'fw_1018610_roll3_mean',
                         'fw_1018610_roll3_max', 'fw_1018610_roll3_min', 'fw_1018610_roll6_mean',
                         'fw_1018610_roll6_median', 'fw_1018610_roll6_max', 'fw_1018610_roll6_min',
                         'fw_1018610_roll9_max', 'fw_1018610_roll9_min', 'fw_1018610_roll12_mean',
                         'fw_1018610_roll12_median', 'fw_1018610_roll12_max', 'fw_1018610_roll15_max',
                         'fw_1018610_roll15_min', 'fw_1018610_roll18_mean', 'fw_1018610_roll18_std',
                         'fw_1018610_roll18_min', 'wl_1018620_s1', 'wl_1018620_roll18_std', 'fw_1018620_roll6_std',
                         'wl_1018623_s1', 'wl_1018623_diff1_s2', 'wl_1018623_s8', 'wl_1018623_diff1_s9',
                         'wl_1018623_diff1_s11', 'wl_1018623_diff1_s12', 'wl_1018623_roll6_mean',
                         'wl_1018623_roll9_max', 'wl_1018623_roll12_std', 'wl_1018623_absdiff_roll12_mean',
                         'wl_1018623_diff_roll12_sqmean', 'wl_1018623_roll15_std', 'wl_1018623_absdiff_roll15_min',
                         'wl_1018623_roll18_max', 'wl_1018623_absdiff_roll18_mean', 'wl_1018623_diff_roll18_sqmean',
                         'wl_1018623_absdiff_roll18_max', 'wl_1018623_absdiff_roll18_min', 'fw_1018623_roll3_std',
                         'fw_1018623_roll6_std', 'wl_1018625_s1', 'wl_1018625_roll3_std', 'wl_1018625_roll12_min',
                         'wl_1018625_roll15_std', 'wl_1018625_roll18_max', 'fw_1018625_diff1_s1', 'fw_1018625_s10',
                         'fw_1018625_absdiff_roll18_min', 'wl_1018630_roll6_mean', 'wl_1018630_roll18_mean',
                         'fw_1018630_s1', 'fw_1018630_roll15_std', 'wl_1018635_s1', 'wl_1018635_s2',
                         'wl_1018635_diff1_s2', 'wl_1018635_diff1_s9', 'wl_1018635_roll3_std', 'wl_1018635_roll15_min',
                         'wl_1018635_roll18_min', 'fw_1018635_diff1_s5', 'fw_1018635_diff1_s6', 'fw_1018635_diff1_s7',
                         'fw_1018635_diff1_s10', 'fw_1018635_diff2_s12', 'fw_1018635_absdiff_roll9_min',
                         'fw_1018635_roll18_mean', 'wl_1018650_s1', 'wl_1018650_roll6_mean', 'wl_1018650_roll15_max',
                         'fw_1018650_diff1_s4', 'fw_1018650_absdiff_roll15_max', 'fw_1018650_roll18_max',
                         'fw_1018650_roll18_min', 'wl_1018665_s1', 'wl_1018665_s7', 'wl_1018665_roll15_std',
                         'wl_1018665_roll18_max', 'fw_1018665_diff2_s10', 'wl_1018690_roll6_std',
                         'wl_1018690_roll12_min', 'wl_1018690_roll15_min', 'wl_1018690_roll18_std', 'fw_1018690_s1',
                         'fw_1018690_diff1_s8', 'fw_1018690_roll3_std', 'fw_1018690_roll3_min', 'wl_1018693_s1',
                         'wl_1018693_diff2_s1', 'wl_1018693_diff1_s4', 'wl_1018693_s8', 'wl_1018693_roll3_mean',
                         'wl_1018693_roll3_max', 'wl_1018693_roll6_mean', 'wl_1018693_roll6_std',
                         'wl_1018693_absdiff_roll9_mean', 'wl_1018693_absdiff_roll12_mean', 'wl_1018693_roll18_mean',
                         'wl_1018693_absdiff_roll18_mean', 'fw_1018693_s1', 'fw_1018693_diff1_s1',
                         'fw_1018693_diff1_s2', 'fw_1018693_diff1_s5', 'fw_1018693_diff1_s8', 'fw_1018693_s9',
                         'fw_1018693_diff1_s9', 'fw_1018693_diff1_s11', 'fw_1018693_s12', 'fw_1018693_roll3_std',
                         'fw_1018693_roll6_median', 'fw_1018693_roll9_max', 'fw_1018693_roll12_mean',
                         'fw_1018693_roll15_std', 'fw_1018693_roll18_mean', 'fw_1018693_roll18_std',
                         'wl_1019620_diff2_s8', 'wl_1019620_s12', 'wl_1019620_roll9_max',
                         'wl_1019620_absdiff_roll9_mean', 'wl_1019620_absdiff_roll12_max', 'wl_1019635_s1',
                         'wl_1019635_diff2_s5', 'wl_1019635_s6', 'wl_1019635_diff2_s6', 'wl_1019635_s7',
                         'wl_1019635_roll3_median', 'wl_1019635_roll3_std', 'wl_1019635_diff_roll3_sqmean',
                         'wl_1019635_roll6_mean', 'wl_1019635_roll6_min', 'wl_1019635_roll9_std',
                         'wl_1019635_roll9_min', 'wl_1019635_roll12_std', 'wl_1019675_s1', 'wl_1019675_diff2_s1',
                         'wl_1019675_s2', 'wl_1019675_diff1_s2', 'wl_1019675_diff2_s2', 'wl_1019675_s3',
                         'wl_1019675_diff1_s3', 'wl_1019675_diff2_s3', 'wl_1019675_s4', 'wl_1019675_diff1_s4',
                         'wl_1019675_diff2_s4', 'wl_1019675_s5', 'wl_1019675_diff2_s5', 'wl_1019675_s6',
                         'wl_1019675_diff1_s6', 'wl_1019675_diff2_s6', 'wl_1019675_s7', 'wl_1019675_diff1_s7',
                         'wl_1019675_diff2_s7', 'wl_1019675_s8', 'wl_1019675_diff1_s8', 'wl_1019675_diff2_s8',
                         'wl_1019675_s9', 'wl_1019675_diff1_s9', 'wl_1019675_diff2_s9', 'wl_1019675_s10',
                         'wl_1019675_diff1_s10', 'wl_1019675_diff2_s10', 'wl_1019675_s11', 'wl_1019675_diff1_s11',
                         'wl_1019675_diff2_s11', 'wl_1019675_s12', 'wl_1019675_diff1_s12', 'wl_1019675_diff2_s12',
                         'wl_1019675_roll3_mean', 'wl_1019675_roll3_std', 'wl_1019675_roll3_max',
                         'wl_1019675_roll3_min', 'wl_1019675_roll6_mean', 'wl_1019675_roll6_median',
                         'wl_1019675_roll6_std', 'wl_1019675_roll6_max', 'wl_1019675_roll6_min',
                         'wl_1019675_absdiff_roll6_mean', 'wl_1019675_absdiff_roll6_max',
                         'wl_1019675_absdiff_roll6_min', 'wl_1019675_roll9_mean', 'wl_1019675_roll9_median',
                         'wl_1019675_roll9_std', 'wl_1019675_roll9_max', 'wl_1019675_roll9_min',
                         'wl_1019675_absdiff_roll9_mean', 'wl_1019675_diff_roll9_sqmean',
                         'wl_1019675_absdiff_roll9_max', 'wl_1019675_absdiff_roll9_min', 'wl_1019675_roll12_mean',
                         'wl_1019675_roll12_median', 'wl_1019675_roll12_std', 'wl_1019675_roll12_max',
                         'wl_1019675_roll12_min', 'wl_1019675_absdiff_roll12_mean', 'wl_1019675_diff_roll12_sqmean',
                         'wl_1019675_roll15_mean', 'wl_1019675_roll15_median', 'wl_1019675_roll15_std',
                         'wl_1019675_roll15_max', 'wl_1019675_roll15_min', 'wl_1019675_absdiff_roll15_mean',
                         'wl_1019675_roll18_mean', 'wl_1019675_roll18_median', 'wl_1019675_roll18_std',
                         'wl_1019675_roll18_max', 'wl_1019675_roll18_min', 'wl_1019675_absdiff_roll18_mean',
                         'wl_1019675_diff_roll18_sqmean', 'wl_1021650_s12', 'wl_1021650_diff2_s12',
                         'wl_1021650_roll3_std', 'wl_1021650_roll9_median', 'fw_1021650_s3', 'fw_1021650_roll3_std',
                         'fw_1021650_roll9_std', 'wl_1021670_diff1_s1', 'wl_1021670_diff2_s1', 'wl_1021670_s2',
                         'wl_1021670_diff2_s3', 'wl_1021670_diff2_s4', 'wl_1021670_diff1_s5', 'wl_1021670_diff1_s6',
                         'wl_1021670_diff2_s6', 'wl_1021670_diff1_s9', 'wl_1021670_diff2_s9', 'wl_1021670_roll6_std',
                         'wl_1021670_absdiff_roll6_max', 'wl_1021670_roll12_min', 'wl_1021670_absdiff_roll12_mean',
                         'wl_1021670_absdiff_roll12_max', 'wl_1021670_roll18_std', 'wl_1021680_diff1_s5',
                         'wl_1021680_diff1_s7', 'wl_1021680_roll3_max', 'wl_1021680_roll9_std',
                         'wl_1021680_diff_roll12_sqmean', 'wl_1021680_roll15_std', 'wl_1021680_roll18_std',
                         'wl_1022640_diff2_s3', 'wl_1022640_s9', 'wl_1022640_diff1_s11', 'wl_1022640_diff2_s12',
                         'wl_1022640_absdiff_roll6_mean', 'wl_1022640_absdiff_roll9_max',
                         'wl_1022640_diff_roll12_sqmean', 'wl_1022640_roll15_median', 'wl_1022640_absdiff_roll18_mean',
                         'fw_1022640_diff1_s1', 'fw_1022640_diff1_s2', 'fw_1022640_diff1_s4', 'fw_1022640_diff2_s9',
                         'fw_1022640_roll9_max', 'fw_1022640_absdiff_roll12_mean', 'fw_1022640_roll15_std',
                         'wl_1022648_roll3_std', 'wl_1022648_roll15_std', 'fw_1022648_diff2_s7', 'fw_1022648_diff1_s10',
                         'fw_1022648_roll3_std', 'fw_1022648_roll6_std', 'wl_1022650_s1', 'wl_1022650_s7',
                         'wl_1022650_diff1_s10', 'wl_1022650_roll3_std', 'wl_1022650_roll6_max', 'wl_1022650_roll9_std',
                         'wl_1022650_absdiff_roll12_max', 'wl_1022650_roll15_std', 'wl_1022650_roll18_mean',
                         'wl_1022650_roll18_min', 'fw_1022650_roll3_std', 'fw_1022650_absdiff_roll6_max',
                         'fw_1022650_roll9_std', 'fw_1022650_roll12_std', 'wl_1022655_diff2_s1', 'wl_1022655_diff2_s3',
                         'wl_1022655_diff2_s6', 'wl_1022655_diff2_s8', 'wl_1022655_roll9_max',
                         'wl_1022655_absdiff_roll18_mean', 'wl_1022670_diff1_s8', 'wl_1022670_diff2_s9',
                         'wl_1022670_roll9_std', 'wl_1022670_roll15_std', 'fw_1022670_diff2_s6',
                         'fw_1022670_absdiff_roll12_max', 'wl_1022680_roll18_std', 'wl_1022680_diff_roll18_sqmean',
                         'fw_1022680_diff1_s8', 'fw_1022680_absdiff_roll3_min', 'fw_1022680_absdiff_roll12_max',
                         'wl_1023640_diff1_s1', 'wl_1023640_diff1_s4', 'wl_1023640_diff2_s7', 'wl_1023640_s11',
                         'wl_1023640_diff2_s12', 'wl_1023640_roll9_mean', 'wl_1023640_absdiff_roll18_mean',
                         'wl_1023660_roll12_min', 'wl_1023660_roll18_min', 'fw_1023660_s2', 'fw_1023660_diff2_s5',
                         'fw_1023660_roll3_std', 'fw_1023660_roll15_std', 'wl_1023662_s2', 'wl_1023662_diff1_s2',
                         'wl_1023662_diff2_s2', 'wl_1023662_diff1_s3', 'wl_1023662_diff2_s5', 'wl_1023662_s8',
                         'wl_1023662_diff2_s10', 'wl_1023662_absdiff_roll3_mean', 'wl_1023662_absdiff_roll3_max',
                         'wl_1023662_diff_roll6_sqmean', 'wl_1023662_roll12_mean', 'wl_1023662_absdiff_roll12_max',
                         'wl_1023662_roll18_min', 'wl_1023662_absdiff_roll18_max', 'wl_1023670_s1',
                         'wl_1023670_diff1_s1', 'wl_1023670_diff2_s1', 'wl_1023670_s2', 'wl_1023670_diff1_s2',
                         'wl_1023670_diff2_s2', 'wl_1023670_s3', 'wl_1023670_diff2_s3', 'wl_1023670_s4',
                         'wl_1023670_diff2_s4', 'wl_1023670_s5', 'wl_1023670_diff1_s5', 'wl_1023670_diff1_s6',
                         'wl_1023670_diff2_s6', 'wl_1023670_s7', 'wl_1023670_diff1_s7', 'wl_1023670_diff2_s7',
                         'wl_1023670_s8', 'wl_1023670_diff1_s8', 'wl_1023670_diff2_s8', 'wl_1023670_s9',
                         'wl_1023670_s10', 'wl_1023670_s12', 'wl_1023670_diff2_s12', 'wl_1023670_roll3_mean',
                         'wl_1023670_roll3_std', 'wl_1023670_roll3_max', 'wl_1023670_absdiff_roll3_mean',
                         'wl_1023670_diff_roll3_sqmean', 'wl_1023670_absdiff_roll3_max', 'wl_1023670_absdiff_roll3_min',
                         'wl_1023670_roll6_mean', 'wl_1023670_roll6_std', 'wl_1023670_roll6_max',
                         'wl_1023670_absdiff_roll6_mean', 'wl_1023670_diff_roll6_sqmean',
                         'wl_1023670_absdiff_roll6_max', 'wl_1023670_absdiff_roll6_min', 'wl_1023670_roll9_mean',
                         'wl_1023670_roll9_median', 'wl_1023670_roll9_std', 'wl_1023670_roll9_max',
                         'wl_1023670_absdiff_roll9_mean', 'wl_1023670_absdiff_roll9_max', 'wl_1023670_roll12_std',
                         'wl_1023670_absdiff_roll12_mean', 'wl_1023670_absdiff_roll12_max', 'wl_1023670_roll15_mean',
                         'wl_1023670_roll15_std', 'wl_1023670_roll15_min', 'wl_1023670_absdiff_roll15_mean',
                         'wl_1023670_diff_roll15_sqmean', 'wl_1023670_roll18_std', 'wl_1023670_roll18_min',
                         'wl_1023670_diff_roll18_sqmean', 'wl_1023670_absdiff_roll18_max', 'fw_1023670_s2',
                         'fw_1023670_s3', 'fw_1023670_diff2_s4', 'fw_1023670_diff2_s6', 'fw_1023670_s12',
                         'fw_1023670_roll6_std', 'fw_1023670_roll9_std', 'fw_1023670_roll15_std',
                         'fw_1023670_roll18_max', 'wl_1023680_s1', 'wl_1023680_diff1_s2', 'wl_1023680_diff2_s2',
                         'wl_1023680_diff1_s4', 'wl_1023680_diff2_s4', 'wl_1023680_s5', 'wl_1023680_s6',
                         'wl_1023680_diff2_s6', 'wl_1023680_diff1_s8', 'wl_1023680_diff1_s10', 'wl_1023680_diff2_s10',
                         'wl_1023680_diff1_s11', 'wl_1023680_diff2_s11', 'wl_1023680_diff2_s12', 'wl_1023680_roll3_std',
                         'wl_1023680_absdiff_roll3_min', 'wl_1023680_roll6_min', 'wl_1023680_diff_roll6_sqmean',
                         'wl_1023680_roll9_max', 'wl_1023680_diff_roll9_sqmean', 'wl_1023680_roll12_min',
                         'wl_1023680_absdiff_roll12_min', 'wl_1023680_absdiff_roll15_mean',
                         'wl_1023680_diff_roll15_sqmean', 'wl_1023680_roll18_mean', 'wl_1023680_absdiff_roll18_mean',
                         'wl_1101605_roll6_std', 'wl_1101605_roll15_max', 'fw_1101605_roll6_std', 'wl_1101610_s1',
                         'wl_1101610_s6', 'wl_1101610_roll3_mean', 'wl_1101610_roll12_mean', 'wl_1101610_roll18_max',
                         'fw_1101610_s10', 'fw_1101610_absdiff_roll12_max', 'wl_1101620_roll15_min',
                         'fw_1101620_diff2_s2', 'fw_1101620_diff2_s8', 'fw_1101620_roll3_std',
                         'fw_1101620_roll18_median', 'wl_1101635_diff1_s2', 'wl_1101635_diff1_s3', 'wl_1101635_s12',
                         'wl_1101635_roll3_min', 'wl_1101635_roll6_std', 'wl_1101635_roll6_max',
                         'wl_1101635_roll12_std', 'wl_1101635_roll15_median', 'wl_1101635_absdiff_roll15_mean',
                         'wl_1101635_roll18_std', 'wl_1101635_roll18_max', 'fw_1101635_s1', 'fw_1101635_s2',
                         'fw_1101635_diff2_s2', 'fw_1101635_diff2_s3', 'fw_1101635_diff1_s4', 'fw_1101635_diff2_s5',
                         'fw_1101635_s6', 'fw_1101635_diff1_s6', 'fw_1101635_s7', 'fw_1101635_s8',
                         'fw_1101635_diff1_s8', 'fw_1101635_diff2_s9', 'fw_1101635_s10', 'fw_1101635_diff1_s10',
                         'fw_1101635_diff2_s10', 'fw_1101635_diff2_s11', 'fw_1101635_roll6_mean',
                         'fw_1101635_roll9_median', 'fw_1101635_absdiff_roll9_min', 'fw_1101635_roll12_mean',
                         'fw_1101635_roll12_std', 'fw_1101635_absdiff_roll12_max', 'fw_1101635_roll15_max',
                         'fw_1101635_absdiff_roll15_max', 'fw_1101635_roll18_median', 'fw_1101635_roll18_std',
                         'fw_1101635_absdiff_roll18_mean', 'wl_1101645_s1', 'wl_1101645_diff2_s6',
                         'wl_1101645_diff2_s8', 'wl_1101645_roll3_std', 'wl_1101645_roll12_mean',
                         'wl_1101645_roll12_std', 'wl_1101645_roll12_min', 'wl_1101645_roll18_max',
                         'fw_1101645_absdiff_roll9_min', 'wl_1101650_s1', 'wl_1101650_diff2_s1', 'wl_1101650_diff2_s6',
                         'wl_1101650_roll9_median', 'wl_1101650_roll9_std', 'wl_1101650_roll15_std',
                         'wl_1101650_roll18_std', 'fw_1101650_diff1_s1', 'fw_1101650_diff2_s6', 'fw_1101650_diff2_s9',
                         'fw_1101650_roll6_median', 'fw_1101650_roll6_std', 'fw_1101650_roll9_std',
                         'fw_1101650_roll12_std', 'fw_1101650_roll12_min', 'fw_1101650_roll18_std',
                         'fw_1101650_absdiff_roll18_mean', 'wl_1101663_diff2_s11', 'wl_1101663_roll15_max',
                         'wl_1101665_diff2_s1', 'wl_1101665_roll6_min', 'fw_1101665_diff1_s1', 'wl_1101670_s1',
                         'wl_1101670_diff2_s1', 'wl_1101670_s12', 'wl_1101670_roll6_max', 'wl_1101670_roll9_std',
                         'wl_1101670_roll12_max', 'wl_1101670_roll18_std', 'fw_1101670_diff1_s1', 'fw_1101670_diff1_s2',
                         'fw_1101670_diff1_s3', 'fw_1101670_diff2_s3', 'fw_1101670_s4', 'fw_1101670_diff1_s5',
                         'fw_1101670_diff1_s6', 'fw_1101670_diff2_s6', 'fw_1101670_s7', 'fw_1101670_diff1_s7',
                         'fw_1101670_diff2_s8', 'fw_1101670_diff1_s9', 'fw_1101670_diff2_s9', 'fw_1101670_diff2_s11',
                         'fw_1101670_roll3_mean', 'fw_1101670_roll3_std', 'fw_1101670_roll3_max',
                         'fw_1101670_absdiff_roll3_min', 'fw_1101670_absdiff_roll9_mean',
                         'fw_1101670_absdiff_roll9_min', 'fw_1101670_roll12_median', 'fw_1101670_roll12_std',
                         'fw_1101670_diff_roll12_sqmean', 'fw_1101670_absdiff_roll12_max',
                         'fw_1101670_absdiff_roll12_min', 'fw_1101670_roll18_std', 'fw_1101670_roll18_max',
                         'fw_1101670_absdiff_roll18_mean', 'fw_1101670_diff_roll18_sqmean', 'wl_1101680_s11',
                         'wl_1101680_roll9_std', 'fw_1101680_diff1_s1', 'fw_1101680_s3', 'fw_1101680_diff1_s3',
                         'fw_1101680_diff2_s3', 'fw_1101680_s4', 'fw_1101680_diff1_s4', 'fw_1101680_diff1_s5',
                         'fw_1101680_diff2_s5', 'fw_1101680_s6', 'fw_1101680_diff1_s6', 'fw_1101680_diff2_s6',
                         'fw_1101680_s7', 'fw_1101680_diff1_s7', 'fw_1101680_diff2_s7', 'fw_1101680_diff1_s8',
                         'fw_1101680_s9', 'fw_1101680_s10', 'fw_1101680_diff1_s10', 'fw_1101680_diff1_s11',
                         'fw_1101680_diff2_s11', 'fw_1101680_diff1_s12', 'fw_1101680_diff2_s12', 'fw_1101680_roll3_std',
                         'fw_1101680_absdiff_roll3_min', 'fw_1101680_roll6_std', 'fw_1101680_roll6_min',
                         'fw_1101680_roll9_std', 'fw_1101680_absdiff_roll9_mean', 'fw_1101680_roll12_max',
                         'fw_1101680_roll15_std', 'fw_1101680_roll15_max', 'fw_1101680_diff_roll15_sqmean',
                         'wl_1101695_diff2_s7', 'wl_1101695_diff_roll3_sqmean', 'wl_1101695_roll9_std',
                         'wl_1101695_roll15_std', 'wl_1101695_absdiff_roll15_mean', 'wl_1101695_diff_roll15_sqmean',
                         'wl_1101696_diff2_s2', 'wl_1101696_s4', 'wl_1101696_diff1_s7', 'wl_1101696_s10',
                         'wl_1101696_diff2_s10', 'wl_1101696_diff2_s12', 'wl_1101696_roll3_std',
                         'wl_1101696_absdiff_roll3_mean', 'wl_1101696_roll18_median', 'wl_1101696_roll18_max',
                         'wl_1101696_absdiff_roll18_min', 'tide_level_DT_0032_s1', 'tide_level_DT_0032_diff1_s1',
                         'tide_level_DT_0032_diff1_s2', 'tide_level_DT_0032_diff2_s2', 'tide_level_DT_0032_diff1_s3',
                         'tide_level_DT_0032_diff2_s3', 'tide_level_DT_0032_s4', 'tide_level_DT_0032_diff1_s4',
                         'tide_level_DT_0032_diff2_s5', 'tide_level_DT_0032_s7', 'tide_level_DT_0032_diff1_s7',
                         'tide_level_DT_0032_diff2_s7', 'tide_level_DT_0032_s8', 'tide_level_DT_0032_s9',
                         'tide_level_DT_0032_diff1_s9', 'tide_level_DT_0032_diff2_s9', 'tide_level_DT_0032_s10',
                         'tide_level_DT_0032_diff2_s10', 'tide_level_DT_0032_s11', 'tide_level_DT_0032_diff1_s11',
                         'tide_level_DT_0032_diff2_s11', 'tide_level_DT_0032_s12', 'tide_level_DT_0032_diff1_s12',
                         'tide_level_DT_0032_diff2_s12', 'tide_level_DT_0032_diff_roll3_sqmean',
                         'tide_level_DT_0032_absdiff_roll3_max', 'tide_level_DT_0032_roll6_min',
                         'tide_level_DT_0032_roll9_min', 'tide_level_DT_0032_absdiff_roll9_mean',
                         'tide_level_DT_0032_roll12_std', 'tide_level_DT_0032_roll12_min',
                         'tide_level_DT_0032_diff_roll12_sqmean', 'tide_level_DT_0032_absdiff_roll12_max',
                         'tide_level_DT_0032_absdiff_roll12_min', 'tide_level_DT_0032_roll15_mean',
                         'tide_level_DT_0032_roll15_median', 'tide_level_DT_0032_roll15_std',
                         'tide_level_DT_0032_roll15_max', 'tide_level_DT_0032_roll15_min',
                         'tide_level_DT_0032_absdiff_roll15_mean', 'tide_level_DT_0032_diff_roll15_sqmean',
                         'tide_level_DT_0032_roll18_mean', 'tide_level_DT_0032_roll18_median',
                         'tide_level_DT_0032_roll18_std', 'tide_level_DT_0032_roll18_max',
                         'tide_level_DT_0032_roll18_min', 'tide_level_DT_0032_diff_roll18_sqmean',
                         'tide_level_DT_0032_absdiff_roll18_max', 'tide_level_DT_0044_s1',
                         'tide_level_DT_0044_diff1_s1', 'tide_level_DT_0044_diff2_s1', 'tide_level_DT_0044_s2',
                         'tide_level_DT_0044_diff1_s2', 'tide_level_DT_0044_diff2_s2', 'tide_level_DT_0044_diff1_s3',
                         'tide_level_DT_0044_diff2_s3', 'tide_level_DT_0044_diff2_s5', 'tide_level_DT_0044_s7',
                         'tide_level_DT_0044_diff1_s7', 'tide_level_DT_0044_s9', 'tide_level_DT_0044_diff2_s9',
                         'tide_level_DT_0044_s11', 'tide_level_DT_0044_s12', 'tide_level_DT_0044_roll6_mean',
                         'tide_level_DT_0044_roll6_std', 'tide_level_DT_0044_roll9_max',
                         'tide_level_DT_0044_roll12_max', 'tide_level_DT_0044_absdiff_roll12_min',
                         'tide_level_DT_0044_roll15_max', 'tide_level_DT_0044_diff_roll15_sqmean',
                         'tide_level_DT_0044_roll18_max', 'tide_level_DT_0044_roll18_min', 'tide_level_DT_0058_s1',
                         'tide_level_DT_0058_diff1_s1', 'tide_level_DT_0058_diff2_s1', 'tide_level_DT_0058_diff1_s2',
                         'tide_level_DT_0058_diff2_s2', 'tide_level_DT_0058_diff1_s4', 'tide_level_DT_0058_diff1_s5',
                         'tide_level_DT_0058_diff2_s5', 'tide_level_DT_0058_s6', 'tide_level_DT_0058_diff1_s6',
                         'tide_level_DT_0058_diff2_s9', 'tide_level_DT_0058_diff1_s10', 'tide_level_DT_0058_s11',
                         'tide_level_DT_0058_diff2_s11', 'tide_level_DT_0058_s12', 'tide_level_DT_0058_roll6_max',
                         'tide_level_DT_0058_absdiff_roll6_mean', 'tide_level_DT_0058_roll9_min',
                         'tide_level_DT_0058_roll12_min', 'tide_level_DT_0058_absdiff_roll12_mean',
                         'tide_level_DT_0058_roll15_median', 'tide_level_DT_0058_roll15_std',
                         'tide_level_DT_0058_roll15_max', 'tide_level_DT_0058_absdiff_roll15_min',
                         'tide_level_DT_0058_roll18_max', 'tide_level_DT_0058_roll18_min',
                         'tide_level_DT_0058_absdiff_roll18_mean', 'rf_10184100_roll3_std', 'rf_10184100_roll12_std',
                         'rf_10184110_roll3_std', 'rf_10184110_roll6_std', 'rf_10184110_roll9_std', 'rf_10184140_s1',
                         'rf_10184140_roll6_mean', 'rf_10184140_roll9_median', 'rf_10184140_roll9_std',
                         'rf_10184140_roll15_std', 'rf_10184140_roll18_mean', 'rf_10184080_roll6_mean',
                         'rf_10184080_roll12_mean', 'rf_10184080_roll12_std', 'rf_10184080_roll18_std',
                         'rf_10184080_absdiff_roll18_mean', 'rf_10184190_roll6_std', 'rf_10184190_roll15_std',
                         'rf_10184200_roll3_std', 'rf_10184200_roll9_std', 'rf_10184200_roll12_mean',
                         'rf_10184200_roll12_std', 'rf_10184200_roll15_mean', 'rf_10194030_roll3_std',
                         'rf_10194030_roll6_std', 'rf_10194030_roll12_median', 'rf_10194030_roll15_std',
                         'rf_10194030_roll18_std', 'rf_10064030_roll3_std', 'rf_10074010_roll6_std',
                         'rf_10074010_roll15_std', 'rf_10074030_roll9_std', 'rf_10074040_roll6_std',
                         'rf_10074040_roll9_std', 'rf_10074040_roll12_std', 'rf_10074040_roll15_std',
                         'rf_10074060_roll18_std', 'rf_10074070_roll9_std', 'rf_10074090_roll3_std',
                         'rf_10074100_roll3_std', 'rf_10074120_roll12_std', 'rf_10074120_roll15_std',
                         'rf_10074170_roll3_std', 'rf_10134020_roll3_std', 'rf_10134020_roll18_std',
                         'rf_10134030_roll3_std', 'rf_10134030_roll9_std', 'rf_10134030_roll12_std',
                         'rf_10134045_roll12_std', 'rf_10134140_roll18_std', 'rf_10154010_roll3_std',
                         'rf_10154010_roll12_std', 'rf_10154010_roll15_std', 'rf_10154020_roll6_std',
                         'rf_10154020_roll12_std', 'rf_10154030_roll9_std', 'rf_10154030_roll12_std',
                         'rf_10154030_roll15_std', 'rf_10154035_roll3_std', 'rf_10154035_roll9_std',
                         'rf_10154035_roll12_std', 'rf_10154035_roll18_std', 'rf_10164010_roll3_std',
                         'rf_10164010_roll6_std', 'rf_10164010_roll12_std', 'rf_10164030_roll6_std',
                         'rf_10164040_roll3_std', 'rf_10164040_roll12_std', 'rf_10164070_roll3_std',
                         'rf_10164070_roll12_std', 'rf_10164075_roll6_std', 'rf_10164080_roll6_std',
                         'rf_10164080_roll12_std', 'rf_10184010_roll6_std', 'rf_10184020_roll9_std',
                         'rf_10184020_roll18_std', 'rf_10184040_roll3_std', 'rf_10184060_roll6_std',
                         'rf_10184060_roll9_mean', 'rf_10184090_roll3_std', 'rf_10184090_roll9_std',
                         'rf_10184090_roll18_mean', 'rf_10184120_roll3_std', 'rf_10184120_roll15_std',
                         'rf_10184125_roll3_std', 'rf_10184125_roll15_std', 'rf_10184130_roll3_std',
                         'rf_10184130_roll6_std', 'rf_10184150_roll3_std', 'rf_10184160_roll6_std',
                         'rf_10184160_roll12_std', 'rf_10184160_absdiff_roll18_mean', 'rf_10184170_roll9_std',
                         'rf_10184170_roll12_std', 'rf_10184180_roll3_std', 'rf_10184180_diff_roll18_sqmean',
                         'rf_10184210_roll9_std', 'rf_10184220_diff_roll9_sqmean', 'rf_10184220_roll12_median',
                         'rf_10184220_roll12_std', 'rf_10184220_roll15_std', 'rf_10184230_roll3_std',
                         'rf_10184230_roll6_std', 'rf_10194010_roll6_median', 'rf_10194010_roll6_std',
                         'rf_10194010_roll9_mean', 'rf_10194010_roll12_median', 'rf_10194010_roll18_mean',
                         'rf_10204010_roll3_std', 'rf_10214010_roll15_std', 'rf_10214030_roll3_std',
                         'rf_10214030_roll15_std', 'rf_10224010_roll12_std', 'rf_10224020_roll3_std',
                         'rf_10224020_roll6_std', 'rf_10224040_roll6_std', 'rf_10224040_roll12_std',
                         'rf_10224040_absdiff_roll15_mean', 'rf_10224060_roll3_median', 'rf_10224060_roll12_std',
                         'rf_10224060_roll15_min', 'rf_10224070_roll15_std', 'rf_10224090_diff2_s4',
                         'rf_10224090_roll12_std', 'rf_10234020_roll6_std', 'rf_10234020_roll18_std',
                         'rf_10234030_roll3_std', 'rf_10234030_roll6_std', 'rf_10234040_roll6_std',
                         'rf_10234040_roll9_std', 'rf_11014010_roll6_std', 'rf_11014010_roll12_std',
                         'rf_11014030_roll12_std', 'rf_11014030_roll18_std', 'rf_11014040_roll3_std',
                         'rf_11014070_roll3_std', 'rf_11014070_roll12_std', 'rf_11014090_roll15_std',
                         'rf_11014100_roll3_std', 'rf_11014100_roll9_std', 'rf_11014120_roll3_std',
                         'rf_11014120_roll12_std', 'yr', 'lunar_period_cos', 'lunar_period_sin']

# In[2]:


_input_path = '../data'
# _input_path = '/data'

import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt


def load_data(data_type):
    dataset_path = f'{_input_path}/{data_type}_data'
    dfs = []
    for file_name in sorted(os.listdir(f'{dataset_path}/')):
        if not file_name.endswith('.csv'):
            continue
        df = pd.read_csv(f'{dataset_path}/{file_name}', parse_dates=['ymdhm'])
        dfs.append(df)
    return pd.concat(dfs, axis=0, ignore_index=True)


def submit(Y_pred):
    '''
    Renders .csv file for submission.
    '''
    df = pd.read_csv(f'{_input_path}/sample_submission.csv')
    df['wl_1018662'] = Y_pred[:, 0]
    df['wl_1018680'] = Y_pred[:, 1]
    df['wl_1018683'] = Y_pred[:, 2]
    df['wl_1019630'] = Y_pred[:, 3]
    df.to_csv(f'../output/submission.csv', index=False)


def competition_metric(Y_true, Y_pred):
    '''
    Returns score for the current competition.
    '''
    l2_mean = np.mean(np.square(Y_true - Y_pred), axis=0)
    r_sq = 1 - (l2_mean / np.var(Y_true, axis=0))
    if np.isnan(r_sq).any() or (r_sq <= 0).any():
        return 999.
    return np.mean(np.sqrt(l2_mean) / r_sq)


# In[3]:


def load_extended_data():
    wlobscds = ['1018662', '1018680', '1018683', '1019630']
    rfobscds = ['10184100', '10184110', '10184140']

    wlobscds += ['1018640', '1018645', '1018655', '1018658', '1018660',
                 '1018664', '1018669', '1018670', '1018675', '1018685',
                 '1018695', '1018697']
    rfobscds += ['10184070', '10184080', '10184190', '10184200', '10194030']

    wlobscds += ['1007604', '1007605', '1007615', '1007617', '1007620',
                 '1007625', '1007630', '1007633', '1007634', '1007635',
                 '1007639', '1007640', '1007641', '1007642', '1007645',
                 '1007649', '1007650', '1007653', '1007655', '1007656',
                 '1007660', '1007662', '1007664', '1007672', '1007680',
                 '1007685', '1007690', '1007697', '1013620', '1013652',
                 '1013655', '1015630', '1015639', '1015640', '1015644',
                 '1015645', '1015680', '1016607', '1016650', '1016655',
                 '1016660', '1016670', '1016695', '1017678', '1017690',
                 '1018605', '1018610', '1018611', '1018620', '1018623',
                 '1018625', '1018628', '1018630', '1018635', '1018638',
                 '1018650', '1018665', '1018690', '1018693', '1019620',
                 '1019635', '1019636', '1019637', '1019667',
                 '1019675', '1019680', '1021650', '1021660', '1021670',
                 '1021680', '1022640', '1022642', '1022643', '1022644',
                 '1022645', '1022648', '1022650', '1022655', '1022659',
                 '1022662', '1022664', '1022665', '1022666', '1022668',
                 '1022670', '1022680', '1023640', '1023660', '1023662',
                 '1023670', '1023680', '1101605', '1101609', '1101610',
                 '1101615', '1101620', '1101625', '1101635', '1101645',
                 '1101650', '1101663', '1101665', '1101670', '1101675',
                 '1101680', '1101685', '1101690', '1101695', '1101696',
                 '1202630', '1202660', '1202670']
    rfobscds += ['10064030', '10074010', '10074020', '10074030', '10074040',
                 '10074060', '10074070', '10074080', '10074090', '10074100',
                 '10074110', '10074120', '10074170', '10074175', '10134020',
                 '10134030', '10134045', '10134140', '10154010', '10154020',
                 '10154030', '10154032', '10154035', '10164010', '10164020',
                 '10164030', '10164040', '10164050', '10164060', '10164070',
                 '10164075', '10164080', '10174020', '10184010', '10184020',
                 '10184030', '10184040', '10184050', '10184060', '10184090',
                 '10184120', '10184125', '10184130', '10184150',
                 '10184160', '10184170', '10184180', '10184210', '10184220',
                 '10184230', '10184232', '10194010', '10204010', '10204020',
                 '10214010', '10214020', '10214030', '10224010', '10224020',
                 '10224040', '10224050', '10224060', '10224070', '10224090',
                 '10234010', '10234020', '10234030', '10234040', '11014010',
                 '11014020', '11014030', '11014040', '11014060', '11014070',
                 '11014080', '11014090', '11014100', '11014120', '11014130',
                 '11014140', '12024010', '12024020', ]

    obs_post_ids = ['DT_0032']
    obs_post_ids += ['DT_0044', 'DT_0058']

    date = 20220822
    df_dm = pd.read_csv(
        f'{_input_path}/OpenAPI_merged/dm_{date}.csv',
        parse_dates=['ymdhm'],
        na_values=[' ', '##########'])

    df_wl = []
    for wlobscd in wlobscds:
        if f'wl_{wlobscd}' in _useless_feature_names + _unimportant_feature_names and f'fw_{wlobscd}' in _useless_feature_names + _unimportant_feature_names:
            continue
        df_wl.append(pd.read_csv(
            f'{_input_path}/OpenAPI_merged/wl_{wlobscd}_{date}.csv',
            na_values=[' ', '##########'])
        )
    df_wl = pd.concat(df_wl, axis=1).drop(columns=['ymdhm'])

    df_rf = []
    for rfobscd in rfobscds:
        if f'rf_{rfobscd}' in _useless_feature_names + _unimportant_feature_names:
            continue
        df_rf.append(pd.read_csv(
            f'{_input_path}/OpenAPI_merged/rf_{rfobscd}_{date}.csv',
            na_values=[' ', '##########'])
        )
    df_rf = pd.concat(df_rf, axis=1).drop(columns=['ymdhm'])

    df_tide = []
    for obs_post_id in obs_post_ids:
        df = pd.read_csv(f'{_input_path}/OpenAPI_merged/tide_level_{obs_post_id}_{date}.csv', parse_dates=['ymdhm'])
        df = df.drop_duplicates()
        df = df.set_index('ymdhm', drop=True)
        df = df.reindex(df.index.ceil('10min').drop_duplicates(), method='ffill')
        df = df.reindex(pd.date_range(pd.Timestamp(2012, 1, 1), pd.Timestamp(2022, 7, 31, 23, 50), freq='10min'))
        df = df.reset_index(drop=True)
        df_tide.append(df)
    df_tide = pd.concat(df_tide, axis=1)

    df = pd.concat([df_dm, df_wl, df_tide, df_rf], axis=1)
    df = df.drop(columns=list(set(_useless_feature_names + _unimportant_feature_names) & set(df.columns)))
    for name in df.columns:
        if name == 'ymdhm':
            continue
        df[name] = df[name].astype(np.float32)
    return df


# In[4]:


def make_eraser(time, ser, bounds):
    eraser = (time < time.min())
    for (t0, t1, v0, v1) in bounds:
        if t0 is None: t0 = pd.Timestamp(2012, 5, 1)
        if t1 is None: t1 = pd.Timestamp(2022, 11, 1)
        if v0 is None: v0 = -np.inf
        if v1 is None: v1 = np.inf
        eraser[(time >= t0) & (time < t1) & (ser >= v0) & (ser < v1)] = True
    return eraser


_eraser_params = {
    'swl': [(None, None, None, 5)],
    'inf': [(None, None, 20000, None),
            (pd.Timestamp(2016, 5, 1), pd.Timestamp(2016, 6, 1), 17500, None),
            (pd.Timestamp(2018, 10, 1), pd.Timestamp(2018, 11, 1), 3000, None)],
    'sfw': [(None, None, None, 50)],
    'ecpc': [(None, None, 200, None)],
    'tototf': [(None, None, 20000, None),
               (pd.Timestamp(2016, 5, 1), pd.Timestamp(2016, 6, 1), 17500, None)],
    #     'wl_1018683': [(pd.Timestamp(2022, 5, 1), None, None, 50)]
}


def rectify_sfw_ecpc(time, swl, sfw, ecpc):
    swl, sfw, ecpc = swl.copy(), sfw.copy(), ecpc.copy()
    mask_before_plunge = (time < pd.Timestamp(2015, 9, 1, 9, 30)) | (time == pd.Timestamp(2015, 9, 1, 10, 20)) | (
                (time > pd.Timestamp(2015, 9, 1, 11, 10)) & (time < pd.Timestamp(2015, 9, 1, 12))) | (
                                     (time > pd.Timestamp(2015, 9, 1, 12)) & (time < pd.Timestamp(2015, 9, 1, 13))) | (
                                     (time > pd.Timestamp(2015, 9, 1, 13)) & (time < pd.Timestamp(2015, 9, 1, 13, 50)))
    A = np.stack([np.ones_like(swl), swl, mask_before_plunge.astype(float)], axis=1)
    B = np.stack([sfw, ecpc], axis=1)
    mask_not_na = ~(np.isnan(A).any(axis=1) | np.isnan(B).any(axis=1))
    drops = np.linalg.lstsq(A[mask_not_na], B[mask_not_na], rcond=None)[0][-1]
    sfw[mask_before_plunge] -= drops[0]
    ecpc[mask_before_plunge] -= drops[1]
    return sfw, ecpc


_tide_period = 12 + 25 / 60
_lunar_period = 29.53 * 24 / 2


def get_na_interval(ser, time=None):
    if time is None:
        time = ser.index
    begins = time[ser.isna().astype(int).diff() == 1]
    ends = time[ser.isna().astype(int).diff() == -1]
    return begins, ends


def interpolate_linearly(ser, width=None):
    if width is None:
        width = np.inf
    values = np.sort(ser[ser.notna()].unique())
    begins, ends = get_na_interval(ser)
    for bi, ei in zip(begins, ends):
        print(bi, ei)
        if ei - bi > width:
            continue
        bv, ev = ser.loc[bi - 1], ser.loc[ei]
        mvs = np.linspace(bv, ev, ei - bi + 2)[1:-1]
        idx_l = np.searchsorted(values, mvs)
        idx_r = np.minimum(idx_l + 1, len(values) - 1)
        l_is_closer = ((mvs - values[idx_l]) <= (values[idx_r] - mvs))
        mvs[l_is_closer] = values[idx_l[l_is_closer]]
        mvs[~l_is_closer] = values[idx_r[~l_is_closer]]
        ser.loc[bi:ei - 1] = mvs
    return ser


def cleanup(df):
    time = df['ymdhm']

    for col_name in df.columns:
        if col_name.startswith('rf_'):
            df[col_name] = np.clip(df[col_name], 0, None)

    #     for col_name, params in _eraser_params.items():
    #         eraser = make_eraser(time, df[col_name], params)
    #         df.loc[eraser, col_name] = np.nan

    #     mask_unusual_spikes = (time >= pd.Timestamp(2017, 6, 20, 7)) & (time <= pd.Timestamp(2017, 6, 27, 17)) & (time.dt.minute == 0)
    #     df.loc[mask_unusual_spikes, ['swl', 'inf', 'sfw', 'ecpc', 'tototf']] = np.nan
    #     for col_name in df.columns:
    #         df[col_name] = interpolate_linearly(df[col_name].copy())
    #     mask_unusual_plateau = (time >= pd.Timestamp(2021, 10, 17)) & (time <= pd.Timestamp(2021, 10, 19, 15))
    #     df.loc[mask_unusual_plateau, ['swl', 'inf', 'sfw', 'ecpc', 'tototf']] = np.nan

    #     sfw, ecpc = rectify_sfw_ecpc(time, df['swl'], df['sfw'], df['ecpc'])
    #     df['sfw'] = sfw
    #     df['ecpc'] = ecpc
    return df


# In[17]:


def features_for_learning(df):
    removed_features = ['ymdhm', 'fw_1018680']
    usable_features = [name for name in df.columns if name not in removed_features]
    time = df['ymdhm']
    result = dict()
    for name in usable_features:
        for i in range(1, 12 + 1):
            # for i in range(1, 6+1):
            result[f'{name}_s{i}'] = df[name].shift(i)
            result[f'{name}_diff1_s{i}'] = df[name].diff(1).shift(i)
            result[f'{name}_diff2_s{i}'] = df[name].diff(2).shift(i)
        for i in [3, 6, 9, 12, 15, 18]:
            # for i in [6, 12]:
            result[f'{name}_roll{i}_mean'] = df[name].rolling(i).agg('mean').shift(1)
            result[f'{name}_roll{i}_median'] = df[name].rolling(i).agg('median').shift(1)
            result[f'{name}_roll{i}_std'] = df[name].rolling(i).agg('std').shift(1)
            result[f'{name}_roll{i}_max'] = df[name].rolling(i).agg('max').shift(1)
            result[f'{name}_roll{i}_min'] = df[name].rolling(i).agg('min').shift(1)
            result[f'{name}_absdiff_roll{i}_mean'] = np.abs(df[name].diff()).rolling(i).agg('mean').shift(1)
            result[f'{name}_diff_roll{i}_sqmean'] = np.square(df[name].diff()).rolling(i).agg('mean').shift(1)
            result[f'{name}_absdiff_roll{i}_max'] = np.abs(df[name].diff()).rolling(i).agg('max').shift(1)
            result[f'{name}_absdiff_roll{i}_min'] = np.abs(df[name].diff()).rolling(i).agg('min').shift(1)

    result['yr'] = time.dt.year
    #     result['month'] = time.dt.month
    #     result['dow'] = time.dt.day_of_week

    elapsed_index = (time - time.iloc[0]).dt.total_seconds() // 600
    pi = np.pi
    result['tide_period_cos'] = np.cos((2 * pi / _tide_period) * elapsed_index)
    result['tide_period_sin'] = np.sin((2 * pi / _tide_period) * elapsed_index)
    #     result['tide_2period_cos'] = np.cos((pi/_tide_period)*elapsed_index)
    #     result['tide_2period_sin'] = np.sin((pi/_tide_period)*elapsed_index)
    result['lunar_period_cos'] = np.cos((2 * pi / _lunar_period) * elapsed_index)
    result['lunar_period_sin'] = np.sin((2 * pi / _lunar_period) * elapsed_index)

    result = pd.DataFrame(result)[_positive_importances]
    for name in result.columns:
        result[name] = result[name].astype(np.float32)
    return result


def labels_for_learning(df):
    return df[['wl_1018662', 'wl_1018680', 'wl_1018683', 'wl_1019630']]


# In[6]:


df = load_extended_data()
df_old = pd.merge(load_data('water'), load_data('rf'), on='ymdhm')
df_old = df_old.set_index('ymdhm', drop=True)
df_old = df_old.reindex(pd.date_range(pd.Timestamp(2012, 1, 1), pd.Timestamp(2022, 7, 31, 23, 50), freq='10min'))
df_old = df_old.reset_index().rename(columns={'index': 'ymdhm'})
df = cleanup(df)

# In[18]:


df_features = features_for_learning(df)
df_labels = labels_for_learning(df_old)
df_interms = labels_for_learning(df)

# In[19]:


mask_train = (df['ymdhm'] < pd.Timestamp(2021, 6, 1))
mask_test = (df['ymdhm'] >= pd.Timestamp(2021, 6, 1)) & (df['ymdhm'] < pd.Timestamp(2021, 7, 19))
mask_train_final = (df['ymdhm'] < pd.Timestamp(2022, 6, 1))
mask_test_final = (df['ymdhm'] >= pd.Timestamp(2022, 6, 1)) & (df['ymdhm'] < pd.Timestamp(2022, 7, 19))

X_train, Y_train = df_features[mask_train], df_labels[mask_train]
X_test, Y_test = df_features[mask_test], df_labels[mask_test]

X_train_final, Y_train_final = df_features[mask_train_final], df_labels[mask_train_final]
X_test_final = df_features[mask_test_final]

I_train, I_test = df_interms[mask_train], df_interms[mask_test]
I_train_final = df_interms[mask_train_final]

# In[20]:


import lightgbm as lgbm


class MyLGBM():
    def __init__(self, params):
        self.params = params

    def fit(self, X, Y):
        self.boosters = []
        for _, y in Y.iteritems():
            booster = lgbm.train(
                self.params,
                lgbm.Dataset(X, y),
            )
            self.boosters.append(booster)
        return self

    def predict(self, X):
        return np.stack([booster.predict(X) for booster in self.boosters], axis=1)


class Adapter():
    def __init__(self):
        pass

    def fit(self, X, Y):
        self.xs, self.ys = [], []
        for i in range(X.shape[1]):
            x, y = X.iloc[:, i], Y.iloc[:, i]
            x, y = x[~x.duplicated()], y[~x.duplicated()]
            mask_notna = ~np.isnan(x) & ~np.isnan(y)
            x, y = x[mask_notna], y[mask_notna]
            self.xs.append(x.iloc[x.argsort()])
            self.ys.append(y.iloc[y.argsort()])
        return self

    def transform(self, X):
        result = np.empty_like(X)
        for i in range(X.shape[1]):
            result[:, i] = np.interp(X[:, i], self.xs[i], self.ys[i])
        return result

import optuna

def objective(trial):
    params = {
        'max_depth': -1,
        'num_leaves': trial.suggest_int('num_leaves', 10, 50) ,
        'num_iterations': trial.suggest_int('num_iterations', 25, 400),
        'learning_rate': trial.suggest_float('learning_rate', 1e-3, 5e-1, log=True),
        'force_row_wise': True,
        'random_state': 42,
        'deterministic': True,

        'verbosity': -1,
    }
    lower_params = {
        'max_depth': -1,
        'num_leaves': trial.suggest_int('num_leaves_lower', 10, 50) ,
        'num_iterations': trial.suggest_int('num_iterations_lower', 25, 400),
        'learning_rate': trial.suggest_float('learning_rate_lower', 1e-3, 5e-1, log=True),
        'force_row_wise': True,
        'random_state': 42,
        'deterministic': True,

        'verbosity': -1,
    }

    model = MyLGBM(params)
    model.fit(X_train, I_train)

    adapter = Adapter().fit(I_train, Y_train)
    I_recon, I_pred = model.predict(X_train), model.predict(X_test)
    Y_recon, Y_pred = adapter.transform(I_recon), adapter.transform(I_pred)
    print(competition_metric(Y_train, Y_recon))
    print(competition_metric(Y_test, Y_pred))

    # 1.0774547811719222
    # 0.9509602612761965

    _lower_features = []
    for col_name in df_features.columns:
        use = False
        for name in df_old.columns:
            if name in col_name:
                use = True
        if use:
            _lower_features.append( col_name )

    XX_train = np.concatenate([X_train[_lower_features].values, Y_recon], axis=1)
    XX_test = np.concatenate([X_test[_lower_features].values, Y_pred], axis=1)

    lower_model = MyLGBM(lower_params)
    lower_model.fit(XX_train, pd.DataFrame(Y_train.values - Y_recon))
    print(competition_metric(Y_train, Y_recon + lower_model.predict(XX_train)))
    print(competition_metric(Y_test, Y_pred + lower_model.predict(XX_test)))
    return competition_metric(Y_test, Y_pred + lower_model.predict(XX_test))


##

study = optuna.create_study()
study.optimize(objective, n_trials=1000)
print(study.best_params)

##