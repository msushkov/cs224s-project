#! /usr/bin/env python

import json, sys
import fileinput
import string

def midpoint(min_val, max_val):
    return min_val + (max_val - min_val) / 2.0

# Return the bucket id (lowest, mid_low, mid_high, or highest) based on the value of the feature.
def get_bucket(min_val, max_val, val):
    min_val = float(min_val)
    max_val = float(max_val)
    val = float(val)

    mid = midpoint(min_val, max_val)
    lower_mid = midpoint(min_val, mid)
    higher_mid = midpoint(mid, max_val)

    result = None

    if val >= min_val and val < lower_mid:
        result = "lowest"
    elif val >= lower_mid and val < mid:
        result = "mid_low"
    elif val >= mid and val < higher_mid:
        result = "mid_high"
    else:
        result = "highest"

    return result


# For each input row
for row in fileinput.input():
    (dateid, self_talked_first, other_talked_first, \
        self_turn_duration, other_turn_duration, \
        min_turn_duration, \
        max_turn_duration, \
        self_turn_duration_sd, other_turn_duration_sd, \
        min_turn_duration_sd, \
        max_turn_duration_sd, \
        self_f0_min, other_f0_min, \
        min_f0_min, \
        max_f0_min, \
        self_f0_min_sd, other_f0_min_sd, \
        min_f0_min_sd, \
        max_f0_min_sd, \
        self_f0_max, other_f0_max, \
        min_f0_max, \
        max_f0_max, \
        self_f0_max_sd, other_f0_max_sd, \
        min_f0_max_sd, \
        max_f0_max_sd, \
        self_f0_mean, other_f0_mean, \
        min_f0_mean, \
        max_f0_mean, \
        self_f0_mean_sd, other_f0_mean_sd, \
        min_f0_mean_sd, \
        max_f0_mean_sd, \
        self_f0_sd, other_f0_sd, \
        min_f0_sd, \
        max_f0_sd, \
        self_f0_sd_sd, other_f0_sd_sd, \
        min_f0_sd_sd, \
        max_f0_sd_sd, \
        self_pitch_range, other_pitch_range, \
        min_pitch_range, \
        max_pitch_range, \
        self_pitch_range_sd, other_pitch_range_sd, \
        min_pitch_range_sd, \
        max_pitch_range_sd, \
        self_rms_min, other_rms_min, \
        min_rms_min, \
        max_rms_min, \
        self_rms_min_sd, other_rms_min_sd, \
        min_rms_min_sd, \
        max_rms_min_sd, \
        self_rms_max, other_rms_max, \
        min_rms_max, \
        max_rms_max, \
        self_rms_max_sd, other_rms_max_sd, \
        min_rms_max_sd, \
        max_rms_max_sd, \
        self_rms_mean, other_rms_mean, \
        min_rms_mean, \
        max_rms_mean, \
        self_rms_mean_sd, other_rms_mean_sd, \
        min_rms_mean_sd, \
        max_rms_mean_sd, \

        self_female, other_female, min_female, max_female, \
        self_race, other_race, min_race, max_race, \
        self_evntgoal, other_evntgoal, min_evntgoal, max_evntgoal, \
        self_frqdates, other_frqdates, min_frqdates, max_frqdates, \
        self_frqsocl, other_frqsocl, min_frqsocl, max_frqsocl, \
        self_sdbefore, other_sdbefore, min_sdbefore, max_sdbefore, \
        self_height, other_height, min_height, max_height, \
        self_weight, other_weight, min_weight, max_weight, \
        self_hairclr, other_hairclr, min_hairclr, max_hairclr, \
        self_plysprt, other_plysprt, min_plysprt, max_plysprt, \
        self_wtchsprt, other_wtchsprt, min_wtchsprt, max_wtchsprt, \
        self_bdybuild, other_bdybuild, min_bdybuild, max_bdybuild, \
        self_dining, other_dining, min_dining, max_dining, \
        self_museum, other_museum, min_museum, max_museum, \
        self_art, other_art, min_art, max_art, \
        self_hiking, other_hiking, min_hiking, max_hiking, \
        self_videogam, other_videogam, min_videogam, max_videogam, \
        self_dancing, other_dancing, min_dancing, max_dancing, \
        self_reading, other_reading, min_reading, max_reading, \
        self_tv, other_tv, min_tv, max_tv, \
        self_theatre, other_theatre, min_theatre, max_theatre, \
        self_movies, other_movies, min_movies, max_movies, \
        self_concerts, other_concerts, min_concerts, max_concerts, \
        self_music, other_music, min_music, max_music, \
        self_shopping, other_shopping, min_shopping, max_shopping, \
        self_yoga, other_yoga, min_yoga, max_yoga, \
        self_samerace, other_samerace, min_samerace, max_samerace, \
        self_ss1atrct, other_ss1atrct, min_ss1atrct, max_ss1atrct, \
        self_ss1sincr, other_ss1sincr, min_ss1sincr, max_ss1sincr, \
        self_ss1intel, other_ss1intel, min_ss1intel, max_ss1intel, \
        self_ss1funny, other_ss1funny, min_ss1funny, max_ss1funny, \
        self_ss1ambit, other_ss1ambit, min_ss1ambit, max_ss1ambit, \
        self_ss1wlthy, other_ss1wlthy, min_ss1wlthy, max_ss1wlthy, \
        self_ss1court, other_ss1court, min_ss1court, max_ss1court, \
        self_os1atrct, other_os1atrct, min_os1atrct, max_os1atrct, \
        self_os1sincr, other_os1sincr, min_os1sincr, max_os1sincr, \
        self_os1intel, other_os1intel, min_os1intel, max_os1intel, \
        self_os1funny, other_os1funny, min_os1funny, max_os1funny, \
        self_os1ambit, other_os1ambit, min_os1ambit, max_os1ambit, \
        self_os1wlthy, other_os1wlthy, min_os1wlthy, max_os1wlthy, \
        self_os1court, other_os1court, min_os1court, max_os1court, \
        self_sd1atrct, other_sd1atrct, min_sd1atrct, max_sd1atrct, \
        self_sd1sincr, other_sd1sincr, min_sd1sincr, max_sd1sincr, \
        self_sd1intel, other_sd1intel, min_sd1intel, max_sd1intel, \
        self_sd1funny, other_sd1funny, min_sd1funny, max_sd1funny, \
        self_sd1ambit, other_sd1ambit, min_sd1ambit, max_sd1ambit, \
        self_sd1shrd, other_sd1shrd, min_sd1shrd, max_sd1shrd, \
        self_sd1wlthy, other_sd1wlthy, min_sd1wlthy, max_sd1wlthy, \
        self_sd1court, other_sd1court, min_sd1court, max_sd1court, \
        self_od1atrct, other_od1atrct, min_od1atrct, max_od1atrct, \
        self_od1sincr, other_od1sincr, min_od1sincr, max_od1sincr, \
        self_od1intel, other_od1intel, min_od1intel, max_od1intel, \
        self_od1funny, other_od1funny, min_od1funny, max_od1funny, \
        self_od1ambit, other_od1ambit, min_od1ambit, max_od1ambit, \
        self_od1shrd, other_od1shrd, min_od1shrd, max_od1shrd, \
        self_od1wlthy, other_od1wlthy, min_od1wlthy, max_od1wlthy, \
        self_od1court, other_od1court, min_od1court, max_od1court, \
        self_fd1atrct, other_fd1atrct, min_fd1atrct, max_fd1atrct, \
        self_fd1sincr, other_fd1sincr, min_fd1sincr, max_fd1sincr, \
        self_fd1intel, other_fd1intel, min_fd1intel, max_fd1intel, \
        self_fd1funny, other_fd1funny, min_fd1funny, max_fd1funny, \
        self_fd1ambit, other_fd1ambit, min_fd1ambit, max_fd1ambit, \
        self_fd1shrd, other_fd1shrd, min_fd1shrd, max_fd1shrd, \
        self_fd1wlthy, other_fd1wlthy, min_fd1wlthy, max_fd1wlthy, \
        self_fd1court, other_fd1court, min_fd1court, max_fd1court, \
        self_Subject, other_Subject, min_Subject, max_Subject, \
        self_UnderStat, other_UnderStat, min_UnderStat, max_UnderStat, \
        self_ForeignBorn, other_ForeignBorn, min_ForeignBorn, max_ForeignBorn) = row.strip().split("\t")

    features = []

    if self_talked_first == '1':
        features.append('SELF_TALKED_FIRST')
    else:
        features.append('OTHER_TALKED_FIRST')

    features.append("SELF_TURN_DURATION_" + get_bucket(min_turn_duration, max_turn_duration, self_turn_duration))
    features.append("OTHER_TURN_DURATION_" + get_bucket(min_turn_duration, max_turn_duration, other_turn_duration))
    features.append("SELF_TURN_DURATION_SD_" + get_bucket(min_turn_duration_sd, max_turn_duration_sd, self_turn_duration_sd))
    features.append("OTHER_TURN_DURATION_SD_" + get_bucket(min_turn_duration_sd, max_turn_duration_sd, other_turn_duration_sd))
    features.append("SELF_F0_MIN_" + get_bucket(min_f0_min, max_f0_min, self_f0_min))
    features.append("OTHER_F0_MIN_" + get_bucket(min_f0_min, max_f0_min, other_f0_min))
    features.append("SELF_F0_MIN_SD_" + get_bucket(min_f0_min_sd, max_f0_min_sd, self_f0_min_sd))
    features.append("OTHER_F0_MIN_SD_" + get_bucket(min_f0_min_sd, max_f0_min_sd, other_f0_min_sd))
    features.append("SELF_F0_MAX_" + get_bucket(min_f0_max, max_f0_max, self_f0_max))
    features.append("OTHER_F0_MAX_" + get_bucket(min_f0_max, max_f0_max, other_f0_max))
    features.append("SELF_F0_MAX_SD_" + get_bucket(min_f0_max_sd, max_f0_max_sd, self_f0_max_sd))
    features.append("OTHER_F0_MAX_SD_" + get_bucket(min_f0_max_sd, max_f0_max_sd, other_f0_max_sd))
    features.append("SELF_F0_MEAN_" + get_bucket(min_f0_mean, max_f0_mean, self_f0_mean))
    features.append("OTHER_F0_MEAN_" + get_bucket(min_f0_mean, max_f0_mean, other_f0_mean))
    features.append("SELF_F0_MEAN_SD_" + get_bucket(min_f0_mean_sd, max_f0_mean_sd, self_f0_mean_sd))
    features.append("OTHER_F0_MEAN_SD_" + get_bucket(min_f0_mean_sd, max_f0_mean_sd, other_f0_mean_sd))
    features.append("SELF_F0_SD_" + get_bucket(min_f0_sd, max_f0_sd, self_f0_sd))
    features.append("OTHER_F0_SD_" + get_bucket(min_f0_sd, max_f0_sd, other_f0_sd))
    features.append("SELF_F0_SD_SD_" + get_bucket(min_f0_sd_sd, max_f0_sd_sd, self_f0_sd_sd))
    features.append("OTHER_F0_SD_SD_" + get_bucket(min_f0_sd_sd, max_f0_sd_sd, other_f0_sd_sd))
    features.append("SELF_PITCH_RANGE_" + get_bucket(min_pitch_range, max_pitch_range, self_pitch_range))
    features.append("OTHER_PITCH_RANGE_" + get_bucket(min_pitch_range, max_pitch_range, other_pitch_range))
    features.append("SELF_PITCH_RANGE_SD_" + get_bucket(min_pitch_range_sd, max_pitch_range_sd, self_pitch_range_sd))
    features.append("OTHER_PITCH_RANGE_SD_" + get_bucket(min_pitch_range_sd, max_pitch_range_sd, other_pitch_range_sd))
    features.append("SELF_RMS_MIN_" + get_bucket(min_rms_min, max_rms_min, self_rms_min))
    features.append("OTHER_RMS_MIN_" + get_bucket(min_rms_min, max_rms_min, other_rms_min))
    features.append("SELF_RMS_MIN_SD_" + get_bucket(min_rms_min_sd, max_rms_min_sd, self_rms_min_sd))
    features.append("OTHER_RMS_MIN_SD_" + get_bucket(min_rms_min_sd, max_rms_min_sd, other_rms_min_sd))
    features.append("SELF_RMS_MAX_" + get_bucket(min_rms_max, max_rms_max, self_rms_max))
    features.append("OTHER_RMS_MAX_" + get_bucket(min_rms_max, max_rms_max, other_rms_max))
    features.append("SELF_RMS_MAX_SD_" + get_bucket(min_rms_max_sd, max_rms_max_sd, self_rms_max_sd))
    features.append("OTHER_RMS_MAX_SD_" + get_bucket(min_rms_max_sd, max_rms_max_sd, other_rms_max_sd))
    features.append("SELF_RMS_MEAN_" + get_bucket(min_rms_mean, max_rms_mean, self_rms_mean))
    features.append("OTHER_RMS_MEAN_" + get_bucket(min_rms_mean, max_rms_mean, other_rms_mean))
    features.append("SELF_RMS_MEAN_SD_" + get_bucket(min_rms_mean_sd, max_rms_mean_sd, self_rms_mean_sd))
    features.append("OTHER_RMS_MEAN_SD_" + get_bucket(min_rms_mean_sd, max_rms_mean_sd, other_rms_mean_sd))

    features.append("SELF_FEMALE_" + str(self_female))
    features.append("OTHER_FEMALE_" + str(other_female))
    features.append("SELF_RACE_" + str(self_race))
    features.append("OTHER_RACE_" + str(other_race))
    features.append("SELF_SAME_RACE_" + str(self_samerace))
    features.append("OTHER_SAME_RACE_" + str(other_samerace))

    for feat in features:
        print "%s\t%s" % (dateid, feat)

    
