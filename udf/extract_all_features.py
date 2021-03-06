#! /usr/bin/env python

import json, sys
import fileinput
import string

# 0 is off, 1 is tuned, 2 is all on
meta = sys.argv[1]
prosodic = sys.argv[2]
textual = sys.argv[3]

sys.stderr.write(" ".join(sys.argv))

def midpoint(min_val, max_val):
    return min_val + (max_val - min_val) / 2.0

def third_1(min_val, max_val):
  return min_val + (max_val - min_val) / 3.0

def third_2(min_val, max_val):
  return min_val + 2.0 * (max_val - min_val) / 3.0

# Return the bucket id (lowest, mid_low, mid_high, or highest) based on the value of the feature.
def get_bucket(min_val, max_val, val):
    min_val = float(min_val)
    max_val = float(max_val)
    val = float(val)

    # mid = midpoint(min_val, max_val)
    # lower_mid = midpoint(min_val, mid)
    # higher_mid = midpoint(mid, max_val)

    third1 = third_1(min_val, max_val)
    third2 = third_2(min_val, max_val)

    result = None

    # if val >= min_val and val < lower_mid:
    #     result = "lowest"
    # elif val >= lower_mid and val < mid:
    #     result = "mid-low"
    # elif val >= mid and val < higher_mid:
    #     result = "mid-high"
    # else:
    #     result = "highest"

    if val >= min_val and val < third1:
      result = "low"
    elif val >= third1 and val < third2:
      result = "mid"
    else:
      result = "high"

    return result


# For each input row
for row in sys.stdin:
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
        self_ForeignBorn, other_ForeignBorn, min_ForeignBorn, max_ForeignBorn, \

        self_tot_words, other_tot_words, max_tot_words, min_tot_words, \
        self_love, other_love, max_love, min_love, \
        max_i_mean_discourse, min_i_mean_discourse, self_i_mean_discourse, other_i_mean_discourse, \
        max_sex, min_sex, self_sex, other_sex, \
        max_meta, min_meta, self_meta, other_meta, \
        max_negate, min_negate, self_negate, other_negate, \
        max_um_discourse, min_um_discourse, self_um_discourse, other_um_discourse, \
        max_negemo, min_negemo, self_negemo, other_negemo, \
        max_appreciation, min_appreciation, self_appreciation, other_appreciation, \
        max_tot_question_words, min_tot_question_words, self_tot_question_words, other_tot_question_words, \
        max_you_know_discourse, min_you_know_discourse, self_you_know_discourse, other_you_know_discourse, \
        max_hate, min_hate, self_hate, other_hate, \
        max_food, min_food, self_food, other_food, \
        max_uh_discourse, min_uh_discourse, self_uh_discourse, other_uh_discourse, \
        max_you, min_you, self_you, other_you, \
        max_I, min_I, self_I, other_I, \
        max_drink, min_drink, self_drink, other_drink, \
        max_like_discourse, min_like_discourse, self_like_discourse, other_like_discourse, \
        max_hedge, min_hedge, self_hedge, other_hedge, \
        max_academics, min_academics, self_academics, other_academics, \
        max_laughter, min_laughter, self_laughter, other_laughter, \
        max_agree, min_agree, self_agree, other_agree) = row.strip().split("\t")

    features = []


    if prosodic == '0':
      pass
    elif prosodic == '1':
      if self_talked_first == '1':
        features.append('PROSODIC_SELF_TALKED_FIRST')
      else:
        features.append('PROSODIC_OTHER_TALKED_FIRST')
      #features.append("PROSODIC_SELF_TURN_DURATION_" + get_bucket(min_turn_duration, max_turn_duration, self_turn_duration))
      #features.append("PROSODIC_OTHER_TURN_DURATION_" + get_bucket(min_turn_duration, max_turn_duration, other_turn_duration))
      features.append("PROSODIC_SELF_TURN_DURATION_SD_" + get_bucket(min_turn_duration_sd, max_turn_duration_sd, self_turn_duration_sd))
      features.append("PROSODIC_OTHER_TURN_DURATION_SD_" + get_bucket(min_turn_duration_sd, max_turn_duration_sd, other_turn_duration_sd))
      #features.append("PROSODIC_SELF_F0_MIN_" + get_bucket(min_f0_min, max_f0_min, self_f0_min))
      #features.append("PROSODIC_OTHER_F0_MIN_" + get_bucket(min_f0_min, max_f0_min, other_f0_min))
      features.append("PROSODIC_SELF_F0_MIN_SD_" + get_bucket(min_f0_min_sd, max_f0_min_sd, self_f0_min_sd))
      features.append("PROSODIC_OTHER_F0_MIN_SD_" + get_bucket(min_f0_min_sd, max_f0_min_sd, other_f0_min_sd))
      features.append("PROSODIC_SELF_F0_MAX_" + get_bucket(min_f0_max, max_f0_max, self_f0_max))
      features.append("PROSODIC_OTHER_F0_MAX_" + get_bucket(min_f0_max, max_f0_max, other_f0_max))
      features.append("PROSODIC_SELF_F0_MAX_SD_" + get_bucket(min_f0_max_sd, max_f0_max_sd, self_f0_max_sd))
      features.append("PROSODIC_OTHER_F0_MAX_SD_" + get_bucket(min_f0_max_sd, max_f0_max_sd, other_f0_max_sd))
      #features.append("PROSODIC_SELF_F0_MEAN_" + get_bucket(min_f0_mean, max_f0_mean, self_f0_mean))
      #features.append("PROSODIC_OTHER_F0_MEAN_" + get_bucket(min_f0_mean, max_f0_mean, other_f0_mean))
      features.append("PROSODIC_SELF_F0_MEAN_SD_" + get_bucket(min_f0_mean_sd, max_f0_mean_sd, self_f0_mean_sd))
      features.append("PROSODIC_OTHER_F0_MEAN_SD_" + get_bucket(min_f0_mean_sd, max_f0_mean_sd, other_f0_mean_sd))
      #features.append("PROSODIC_SELF_F0_SD_" + get_bucket(min_f0_sd, max_f0_sd, self_f0_sd))
      #features.append("PROSODIC_OTHER_F0_SD_" + get_bucket(min_f0_sd, max_f0_sd, other_f0_sd))
      #features.append("PROSODIC_SELF_F0_SD_SD_" + get_bucket(min_f0_sd_sd, max_f0_sd_sd, self_f0_sd_sd))
      #features.append("PROSODIC_OTHER_F0_SD_SD_" + get_bucket(min_f0_sd_sd, max_f0_sd_sd, other_f0_sd_sd))
      #features.append("PROSODIC_SELF_PITCH_RANGE_" + get_bucket(min_pitch_range, max_pitch_range, self_pitch_range))
      #features.append("PROSODIC_OTHER_PITCH_RANGE_" + get_bucket(min_pitch_range, max_pitch_range, other_pitch_range))
      #features.append("PROSODIC_SELF_PITCH_RANGE_SD_" + get_bucket(min_pitch_range_sd, max_pitch_range_sd, self_pitch_range_sd))
      #features.append("PROSODIC_OTHER_PITCH_RANGE_SD_" + get_bucket(min_pitch_range_sd, max_pitch_range_sd, other_pitch_range_sd))
      features.append("PROSODIC_SELF_RMS_MIN_" + get_bucket(min_rms_min, max_rms_min, self_rms_min))
      features.append("PROSODIC_OTHER_RMS_MIN_" + get_bucket(min_rms_min, max_rms_min, other_rms_min))
      features.append("PROSODIC_SELF_RMS_MIN_SD_" + get_bucket(min_rms_min_sd, max_rms_min_sd, self_rms_min_sd))
      features.append("PROSODIC_OTHER_RMS_MIN_SD_" + get_bucket(min_rms_min_sd, max_rms_min_sd, other_rms_min_sd))
      #features.append("PROSODIC_SELF_RMS_MAX_" + get_bucket(min_rms_max, max_rms_max, self_rms_max))
      #features.append("PROSODIC_OTHER_RMS_MAX_" + get_bucket(min_rms_max, max_rms_max, other_rms_max))
      #features.append("PROSODIC_SELF_RMS_MAX_SD_" + get_bucket(min_rms_max_sd, max_rms_max_sd, self_rms_max_sd))
      #features.append("PROSODIC_OTHER_RMS_MAX_SD_" + get_bucket(min_rms_max_sd, max_rms_max_sd, other_rms_max_sd))
      features.append("PROSODIC_SELF_RMS_MEAN_" + get_bucket(min_rms_mean, max_rms_mean, self_rms_mean))
      features.append("PROSODIC_OTHER_RMS_MEAN_" + get_bucket(min_rms_mean, max_rms_mean, other_rms_mean))
      #features.append("PROSODIC_SELF_RMS_MEAN_SD_" + get_bucket(min_rms_mean_sd, max_rms_mean_sd, self_rms_mean_sd))
      #features.append("PROSODIC_OTHER_RMS_MEAN_SD_" + get_bucket(min_rms_mean_sd, max_rms_mean_sd, other_rms_mean_sd))

    elif prosodic == '2':
      if self_talked_first == '1':
          features.append('PROSODIC_SELF_TALKED_FIRST')
      else:
          features.append('PROSODIC_OTHER_TALKED_FIRST')
      features.append("PROSODIC_SELF_TURN_DURATION_" + get_bucket(min_turn_duration, max_turn_duration, self_turn_duration))
      features.append("PROSODIC_OTHER_TURN_DURATION_" + get_bucket(min_turn_duration, max_turn_duration, other_turn_duration))
      features.append("PROSODIC_SELF_TURN_DURATION_SD_" + get_bucket(min_turn_duration_sd, max_turn_duration_sd, self_turn_duration_sd))
      features.append("PROSODIC_OTHER_TURN_DURATION_SD_" + get_bucket(min_turn_duration_sd, max_turn_duration_sd, other_turn_duration_sd))
      features.append("PROSODIC_SELF_F0_MIN_" + get_bucket(min_f0_min, max_f0_min, self_f0_min))
      features.append("PROSODIC_OTHER_F0_MIN_" + get_bucket(min_f0_min, max_f0_min, other_f0_min))
      features.append("PROSODIC_SELF_F0_MIN_SD_" + get_bucket(min_f0_min_sd, max_f0_min_sd, self_f0_min_sd))
      features.append("PROSODIC_OTHER_F0_MIN_SD_" + get_bucket(min_f0_min_sd, max_f0_min_sd, other_f0_min_sd))
      features.append("PROSODIC_SELF_F0_MAX_" + get_bucket(min_f0_max, max_f0_max, self_f0_max))
      features.append("PROSODIC_OTHER_F0_MAX_" + get_bucket(min_f0_max, max_f0_max, other_f0_max))
      features.append("PROSODIC_SELF_F0_MAX_SD_" + get_bucket(min_f0_max_sd, max_f0_max_sd, self_f0_max_sd))
      features.append("PROSODIC_OTHER_F0_MAX_SD_" + get_bucket(min_f0_max_sd, max_f0_max_sd, other_f0_max_sd))
      features.append("PROSODIC_SELF_F0_MEAN_" + get_bucket(min_f0_mean, max_f0_mean, self_f0_mean))
      features.append("PROSODIC_OTHER_F0_MEAN_" + get_bucket(min_f0_mean, max_f0_mean, other_f0_mean))
      features.append("PROSODIC_SELF_F0_MEAN_SD_" + get_bucket(min_f0_mean_sd, max_f0_mean_sd, self_f0_mean_sd))
      features.append("PROSODIC_OTHER_F0_MEAN_SD_" + get_bucket(min_f0_mean_sd, max_f0_mean_sd, other_f0_mean_sd))
      features.append("PROSODIC_SELF_F0_SD_" + get_bucket(min_f0_sd, max_f0_sd, self_f0_sd))
      features.append("PROSODIC_OTHER_F0_SD_" + get_bucket(min_f0_sd, max_f0_sd, other_f0_sd))
      features.append("PROSODIC_SELF_F0_SD_SD_" + get_bucket(min_f0_sd_sd, max_f0_sd_sd, self_f0_sd_sd))
      features.append("PROSODIC_OTHER_F0_SD_SD_" + get_bucket(min_f0_sd_sd, max_f0_sd_sd, other_f0_sd_sd))
      features.append("PROSODIC_SELF_PITCH_RANGE_" + get_bucket(min_pitch_range, max_pitch_range, self_pitch_range))
      features.append("PROSODIC_OTHER_PITCH_RANGE_" + get_bucket(min_pitch_range, max_pitch_range, other_pitch_range))
      features.append("PROSODIC_SELF_PITCH_RANGE_SD_" + get_bucket(min_pitch_range_sd, max_pitch_range_sd, self_pitch_range_sd))
      features.append("PROSODIC_OTHER_PITCH_RANGE_SD_" + get_bucket(min_pitch_range_sd, max_pitch_range_sd, other_pitch_range_sd))
      features.append("PROSODIC_SELF_RMS_MIN_" + get_bucket(min_rms_min, max_rms_min, self_rms_min))
      features.append("PROSODIC_OTHER_RMS_MIN_" + get_bucket(min_rms_min, max_rms_min, other_rms_min))
      features.append("PROSODIC_SELF_RMS_MIN_SD_" + get_bucket(min_rms_min_sd, max_rms_min_sd, self_rms_min_sd))
      features.append("PROSODIC_OTHER_RMS_MIN_SD_" + get_bucket(min_rms_min_sd, max_rms_min_sd, other_rms_min_sd))
      features.append("PROSODIC_SELF_RMS_MAX_" + get_bucket(min_rms_max, max_rms_max, self_rms_max))
      features.append("PROSODIC_OTHER_RMS_MAX_" + get_bucket(min_rms_max, max_rms_max, other_rms_max))
      features.append("PROSODIC_SELF_RMS_MAX_SD_" + get_bucket(min_rms_max_sd, max_rms_max_sd, self_rms_max_sd))
      features.append("PROSODIC_OTHER_RMS_MAX_SD_" + get_bucket(min_rms_max_sd, max_rms_max_sd, other_rms_max_sd))
      features.append("PROSODIC_SELF_RMS_MEAN_" + get_bucket(min_rms_mean, max_rms_mean, self_rms_mean))
      features.append("PROSODIC_OTHER_RMS_MEAN_" + get_bucket(min_rms_mean, max_rms_mean, other_rms_mean))
      features.append("PROSODIC_SELF_RMS_MEAN_SD_" + get_bucket(min_rms_mean_sd, max_rms_mean_sd, self_rms_mean_sd))
      features.append("PROSODIC_OTHER_RMS_MEAN_SD_" + get_bucket(min_rms_mean_sd, max_rms_mean_sd, other_rms_mean_sd))

    if meta == '0':
      pass
    elif meta == '1':
      features.append("META_self_female_" + get_bucket(min_female, max_female, self_female))
      features.append("META_other_female_" + get_bucket(min_female, max_female, other_female))
      features.append("META_self_race_" + get_bucket(min_race, max_race, self_race))
      features.append("META_other_race_" + get_bucket(min_race, max_race, other_race))
      features.append("META_self_entgoal_" + get_bucket(min_evntgoal, max_evntgoal, self_evntgoal))
      features.append("META_other_entgoal_" + get_bucket(min_evntgoal, max_evntgoal, other_evntgoal))
      features.append("META_self_frqdates_" + get_bucket(min_frqdates, max_frqdates, self_frqdates))
      features.append("META_other_frqdates_" + get_bucket(min_frqdates, max_frqdates, other_frqdates))
      features.append("META_self_frqsocl_" + get_bucket(min_frqsocl, max_frqsocl, self_frqsocl))
      features.append("META_other_frqsocl_" + get_bucket(min_frqsocl, max_frqsocl, other_frqsocl))
      features.append("META_self_sdbefore_" + get_bucket(min_sdbefore, max_sdbefore, self_sdbefore))
      features.append("META_other_sdbefore_" + get_bucket(min_sdbefore, max_sdbefore, other_sdbefore))
      #features.append("META_self_height_" + get_bucket(min_height, max_height, self_height))
      #features.append("META_other_height_" + get_bucket(min_height, max_height, other_height))
      features.append("META_self_weight_" + get_bucket(min_weight, max_weight, self_weight))
      features.append("META_other_weight_" + get_bucket(min_weight, max_weight, other_weight))
      features.append("META_self_hairclr_" + get_bucket(min_hairclr, max_hairclr, self_hairclr))
      features.append("META_other_hairclr_" + get_bucket(min_hairclr, max_hairclr, other_hairclr))
      features.append("META_self_plysprt_" + get_bucket(min_plysprt, max_plysprt, self_plysprt))
      features.append("META_other_plysprt_" + get_bucket(min_plysprt, max_plysprt, other_plysprt))
      features.append("META_self_wtchsprt_" + get_bucket(min_wtchsprt, max_wtchsprt, self_wtchsprt))
      features.append("META_other_wtchsprt_" + get_bucket(min_wtchsprt, max_wtchsprt, other_wtchsprt))
      features.append("META_self_bdybuild_" + get_bucket(min_bdybuild, max_bdybuild, self_bdybuild))
      features.append("META_other_bdybuild_" + get_bucket(min_bdybuild, max_bdybuild, other_bdybuild))
      features.append("META_self_dining_" + get_bucket(min_dining, max_dining, self_dining))
      features.append("META_other_dining_" + get_bucket(min_dining, max_dining, other_dining))
      features.append("META_self_museum_" + get_bucket(min_museum, max_museum, self_museum))
      features.append("META_other_museum_" + get_bucket(min_museum, max_museum, other_museum))
      #features.append("META_self_art_" + get_bucket(min_art, max_art, self_art))
      #features.append("META_other_art_" + get_bucket(min_art, max_art, other_art))
      features.append("META_self_hiking_" + get_bucket(min_hiking, max_hiking, self_hiking))
      features.append("META_other_hiking_" + get_bucket(min_hiking, max_hiking, other_hiking))
      features.append("META_self_videogam_" + get_bucket(min_videogam, max_videogam, self_videogam))
      features.append("META_other_videogam_" + get_bucket(min_videogam, max_videogam, other_videogam))
      features.append("META_self_dancing_" + get_bucket(min_dancing, max_dancing, self_dancing))
      features.append("META_other_dancing_" + get_bucket(min_dancing, max_dancing, other_dancing))
      features.append("META_self_reading_" + get_bucket(min_reading, max_reading, self_reading))
      features.append("META_other_reading_" + get_bucket(min_reading, max_reading, other_reading))
      features.append("META_self_tv_" + get_bucket(min_tv, max_tv, self_tv))
      features.append("META_other_tv_" + get_bucket(min_tv, max_tv, other_tv))
      features.append("META_self_theatre_" + get_bucket(min_theatre, max_theatre, self_theatre))
      features.append("META_other_theatre_" + get_bucket(min_theatre, max_theatre, other_theatre))
      features.append("META_self_movies_" + get_bucket(min_movies, max_movies, self_movies))
      features.append("META_other_movies_" + get_bucket(min_movies, max_movies, other_movies))
      #features.append("META_self_concerts_" + get_bucket(min_concerts, max_concerts, self_concerts))
      #features.append("META_other_concerts_" + get_bucket(min_concerts, max_concerts, other_concerts))
      features.append("META_self_music_" + get_bucket(min_music, max_music, self_music))
      features.append("META_other_music_" + get_bucket(min_music, max_music, other_music))
      features.append("META_self_shopping_" + get_bucket(min_shopping, max_shopping, self_shopping))
      features.append("META_other_shopping_" + get_bucket(min_shopping, max_shopping, other_shopping))
      features.append("META_self_yoga_" + get_bucket(min_yoga, max_yoga, self_yoga))
      features.append("META_other_yoga_" + get_bucket(min_yoga, max_yoga, other_yoga))
      features.append("META_self_samerace_" + get_bucket(min_samerace, max_samerace, self_samerace))
      features.append("META_other_samerace_" + get_bucket(min_samerace, max_samerace, other_samerace))
      #features.append("META_self_ss1atrct_" + get_bucket(min_ss1atrct, max_ss1atrct, self_ss1atrct))
      #features.append("META_other_ss1atrct_" + get_bucket(min_ss1atrct, max_ss1atrct, other_ss1atrct))
      #features.append("META_self_ss1sincr_" + get_bucket(min_ss1sincr, max_ss1sincr, self_ss1sincr))
      #features.append("META_other_ss1sincr_" + get_bucket(min_ss1sincr, max_ss1sincr, other_ss1sincr))
      #features.append("META_self_ss1intel_" + get_bucket(min_ss1intel, max_ss1intel, self_ss1intel))
      #features.append("META_other_ss1intel_" + get_bucket(min_ss1intel, max_ss1intel, other_ss1intel))
      features.append("META_self_ss1funny_" + get_bucket(min_ss1funny, max_ss1funny, self_ss1funny))
      features.append("META_other_ss1funny_" + get_bucket(min_ss1funny, max_ss1funny, other_ss1funny))
      features.append("META_self_ss1ambit_" + get_bucket(min_ss1ambit, max_ss1ambit, self_ss1ambit))
      features.append("META_other_ss1ambit_" + get_bucket(min_ss1ambit, max_ss1ambit, other_ss1ambit))
      #features.append("META_self_ss1wlthy_" + get_bucket(min_ss1wlthy, max_ss1wlthy, self_ss1wlthy))
      #features.append("META_other_ss1wlthy_" + get_bucket(min_ss1wlthy, max_ss1wlthy, other_ss1wlthy))
      features.append("META_self_ss1court_" + get_bucket(min_ss1court, max_ss1court, self_ss1court))
      features.append("META_other_ss1court_" + get_bucket(min_ss1court, max_ss1court, other_ss1court))
      features.append("META_self_os1atrct_" + get_bucket(min_os1atrct, max_os1atrct, self_os1atrct))
      features.append("META_other_os1atrct_" + get_bucket(min_os1atrct, max_os1atrct, other_os1atrct))
      features.append("META_self_os1sincr_" + get_bucket(min_os1sincr, max_os1sincr, self_os1sincr))
      features.append("META_other_os1sincr_" + get_bucket(min_os1sincr, max_os1sincr, other_os1sincr))
      features.append("META_self_os1intel_" + get_bucket(min_os1intel, max_os1intel, self_os1intel))
      features.append("META_other_os1intel_" + get_bucket(min_os1intel, max_os1intel, other_os1intel))
      #features.append("META_self_os1funny_" + get_bucket(min_os1funny, max_os1funny, self_os1funny))
      #features.append("META_other_os1funny_" + get_bucket(min_os1funny, max_os1funny, other_os1funny))
      features.append("META_self_os1ambit_" + get_bucket(min_os1ambit, max_os1ambit, self_os1ambit))
      features.append("META_other_os1ambit_" + get_bucket(min_os1ambit, max_os1ambit, other_os1ambit))
      features.append("META_self_os1wlthy_" + get_bucket(min_os1wlthy, max_os1wlthy, self_os1wlthy))
      features.append("META_other_os1wlthy_" + get_bucket(min_os1wlthy, max_os1wlthy, other_os1wlthy))
      #features.append("META_self_os1court_" + get_bucket(min_os1court, max_os1court, self_os1court))
      #features.append("META_other_os1court_" + get_bucket(min_os1court, max_os1court, other_os1court))
      features.append("META_self_sd1atrct_" + get_bucket(min_sd1atrct, max_sd1atrct, self_sd1atrct))
      features.append("META_other_sd1atrct_" + get_bucket(min_sd1atrct, max_sd1atrct, other_sd1atrct))
      features.append("META_self_sd1sincr_" + get_bucket(min_sd1sincr, max_sd1sincr, self_sd1sincr))
      features.append("META_other_sd1sincr_" + get_bucket(min_sd1sincr, max_sd1sincr, other_sd1sincr))
      features.append("META_self_sd1intel_" + get_bucket(min_sd1intel, max_sd1intel, self_sd1intel))
      features.append("META_other_sd1intel_" + get_bucket(min_sd1intel, max_sd1intel, other_sd1intel))
      features.append("META_self_sd1funny_" + get_bucket(min_sd1funny, max_sd1funny, self_sd1funny))
      features.append("META_other_sd1funny_" + get_bucket(min_sd1funny, max_sd1funny, other_sd1funny))
      features.append("META_self_sd1ambit_" + get_bucket(min_sd1ambit, max_sd1ambit, self_sd1ambit))
      features.append("META_other_sd1ambit_" + get_bucket(min_sd1ambit, max_sd1ambit, other_sd1ambit))
      features.append("META_self_sd1shrd_" + get_bucket(min_sd1shrd, max_sd1shrd, self_sd1shrd))
      features.append("META_other_sd1shrd_" + get_bucket(min_sd1shrd, max_sd1shrd, other_sd1shrd))
      features.append("META_self_sd1wlthy_" + get_bucket(min_sd1wlthy, max_sd1wlthy, self_sd1wlthy))
      features.append("META_other_sd1wlthy_" + get_bucket(min_sd1wlthy, max_sd1wlthy, other_sd1wlthy))
      features.append("META_self_sd1court_" + get_bucket(min_sd1court, max_sd1court, self_sd1court))
      features.append("META_other_sd1court_" + get_bucket(min_sd1court, max_sd1court, other_sd1court))
      features.append("META_self_od1atrct_" + get_bucket(min_od1atrct, max_od1atrct, self_od1atrct))
      features.append("META_other_od1atrct_" + get_bucket(min_od1atrct, max_od1atrct, other_od1atrct))
      features.append("META_self_od1sincr_" + get_bucket(min_od1sincr, max_od1sincr, self_od1sincr))
      features.append("META_other_od1sincr_" + get_bucket(min_od1sincr, max_od1sincr, other_od1sincr))
      features.append("META_self_od1intel_" + get_bucket(min_od1intel, max_od1intel, self_od1intel))
      features.append("META_other_od1intel_" + get_bucket(min_od1intel, max_od1intel, other_od1intel))
      features.append("META_self_od1funny_" + get_bucket(min_od1funny, max_od1funny, self_od1funny))
      features.append("META_other_od1funny_" + get_bucket(min_od1funny, max_od1funny, other_od1funny))
      features.append("META_self_od1ambit_" + get_bucket(min_od1ambit, max_od1ambit, self_od1ambit))
      features.append("META_other_od1ambit_" + get_bucket(min_od1ambit, max_od1ambit, other_od1ambit))
      features.append("META_self_od1shrd_" + get_bucket(min_od1shrd, max_od1shrd, self_od1shrd))
      features.append("META_other_od1shrd_" + get_bucket(min_od1shrd, max_od1shrd, other_od1shrd))
      features.append("META_self_od1wlthy_" + get_bucket(min_od1wlthy, max_od1wlthy, self_od1wlthy))
      features.append("META_other_od1wlthy_" + get_bucket(min_od1wlthy, max_od1wlthy, other_od1wlthy))
      features.append("META_self_od1court_" + get_bucket(min_od1court, max_od1court, self_od1court))
      features.append("META_other_od1court_" + get_bucket(min_od1court, max_od1court, other_od1court))
      #features.append("META_self_fd1atrct_" + get_bucket(min_fd1atrct, max_fd1atrct, self_fd1atrct))
      #features.append("META_other_fd1atrct_" + get_bucket(min_fd1atrct, max_fd1atrct, other_fd1atrct))
      features.append("META_self_fd1sincr_" + get_bucket(min_fd1sincr, max_fd1sincr, self_fd1sincr))
      features.append("META_other_fd1sincr_" + get_bucket(min_fd1sincr, max_fd1sincr, other_fd1sincr))
      features.append("META_self_fd1intel_" + get_bucket(min_fd1intel, max_fd1intel, self_fd1intel))
      features.append("META_other_fd1intel_" + get_bucket(min_fd1intel, max_fd1intel, other_fd1intel))
      features.append("META_self_fd1funny_" + get_bucket(min_fd1funny, max_fd1funny, self_fd1funny))
      features.append("META_other_fd1funny_" + get_bucket(min_fd1funny, max_fd1funny, other_fd1funny))
      features.append("META_self_fd1ambit_" + get_bucket(min_fd1ambit, max_fd1ambit, self_fd1ambit))
      features.append("META_other_fd1ambit_" + get_bucket(min_fd1ambit, max_fd1ambit, other_fd1ambit))
      features.append("META_self_fd1shrd_" + get_bucket(min_fd1shrd, max_fd1shrd, self_fd1shrd))
      features.append("META_other_fd1shrd_" + get_bucket(min_fd1shrd, max_fd1shrd, other_fd1shrd))
      features.append("META_self_fd1wlthy_" + get_bucket(min_fd1wlthy, max_fd1wlthy, self_fd1wlthy))
      features.append("META_other_fd1wlthy_" + get_bucket(min_fd1wlthy, max_fd1wlthy, other_fd1wlthy))
      features.append("META_self_fd1court_" + get_bucket(min_fd1court, max_fd1court, self_fd1court))
      features.append("META_other_fd1court_" + get_bucket(min_fd1court, max_fd1court, other_fd1court))
      features.append("META_self_Subject_" + get_bucket(min_Subject, max_Subject, self_Subject))
      features.append("META_other_Subject_" + get_bucket(min_Subject, max_Subject, other_Subject))
      features.append("META_self_UnderStat_" + get_bucket(min_UnderStat, max_UnderStat, self_UnderStat))
      features.append("META_other_UnderStat_" + get_bucket(min_UnderStat, max_UnderStat, other_UnderStat))
      features.append("META_self_ForeignBorn_" + get_bucket(min_ForeignBorn, max_ForeignBorn, self_ForeignBorn))
      features.append("META_other_ForeignBorn_" + get_bucket(min_ForeignBorn, max_ForeignBorn, other_ForeignBorn))

    elif meta == '2':
      features.append("META_self_female_" + get_bucket(min_female, max_female, self_female))
      features.append("META_other_female_" + get_bucket(min_female, max_female, other_female))
      features.append("META_self_race_" + get_bucket(min_race, max_race, self_race))
      features.append("META_other_race_" + get_bucket(min_race, max_race, other_race))
      features.append("META_self_entgoal_" + get_bucket(min_evntgoal, max_evntgoal, self_evntgoal))
      features.append("META_other_entgoal_" + get_bucket(min_evntgoal, max_evntgoal, other_evntgoal))
      features.append("META_self_frqdates_" + get_bucket(min_frqdates, max_frqdates, self_frqdates))
      features.append("META_other_frqdates_" + get_bucket(min_frqdates, max_frqdates, other_frqdates))
      features.append("META_self_frqsocl_" + get_bucket(min_frqsocl, max_frqsocl, self_frqsocl))
      features.append("META_other_frqsocl_" + get_bucket(min_frqsocl, max_frqsocl, other_frqsocl))
      features.append("META_self_sdbefore_" + get_bucket(min_sdbefore, max_sdbefore, self_sdbefore))
      features.append("META_other_sdbefore_" + get_bucket(min_sdbefore, max_sdbefore, other_sdbefore))
      features.append("META_self_height_" + get_bucket(min_height, max_height, self_height))
      features.append("META_other_height_" + get_bucket(min_height, max_height, other_height))
      features.append("META_self_weight_" + get_bucket(min_weight, max_weight, self_weight))
      features.append("META_other_weight_" + get_bucket(min_weight, max_weight, other_weight))
      features.append("META_self_hairclr_" + get_bucket(min_hairclr, max_hairclr, self_hairclr))
      features.append("META_other_hairclr_" + get_bucket(min_hairclr, max_hairclr, other_hairclr))
      features.append("META_self_plysprt_" + get_bucket(min_plysprt, max_plysprt, self_plysprt))
      features.append("META_other_plysprt_" + get_bucket(min_plysprt, max_plysprt, other_plysprt))
      features.append("META_self_wtchsprt_" + get_bucket(min_wtchsprt, max_wtchsprt, self_wtchsprt))
      features.append("META_other_wtchsprt_" + get_bucket(min_wtchsprt, max_wtchsprt, other_wtchsprt))
      features.append("META_self_bdybuild_" + get_bucket(min_bdybuild, max_bdybuild, self_bdybuild))
      features.append("META_other_bdybuild_" + get_bucket(min_bdybuild, max_bdybuild, other_bdybuild))
      features.append("META_self_dining_" + get_bucket(min_dining, max_dining, self_dining))
      features.append("META_other_dining_" + get_bucket(min_dining, max_dining, other_dining))
      features.append("META_self_museum_" + get_bucket(min_museum, max_museum, self_museum))
      features.append("META_other_museum_" + get_bucket(min_museum, max_museum, other_museum))
      features.append("META_self_art_" + get_bucket(min_art, max_art, self_art))
      features.append("META_other_art_" + get_bucket(min_art, max_art, other_art))
      features.append("META_self_hiking_" + get_bucket(min_hiking, max_hiking, self_hiking))
      features.append("META_other_hiking_" + get_bucket(min_hiking, max_hiking, other_hiking))
      features.append("META_self_videogam_" + get_bucket(min_videogam, max_videogam, self_videogam))
      features.append("META_other_videogam_" + get_bucket(min_videogam, max_videogam, other_videogam))
      features.append("META_self_dancing_" + get_bucket(min_dancing, max_dancing, self_dancing))
      features.append("META_other_dancing_" + get_bucket(min_dancing, max_dancing, other_dancing))
      features.append("META_self_reading_" + get_bucket(min_reading, max_reading, self_reading))
      features.append("META_other_reading_" + get_bucket(min_reading, max_reading, other_reading))
      features.append("META_self_tv_" + get_bucket(min_tv, max_tv, self_tv))
      features.append("META_other_tv_" + get_bucket(min_tv, max_tv, other_tv))
      features.append("META_self_theatre_" + get_bucket(min_theatre, max_theatre, self_theatre))
      features.append("META_other_theatre_" + get_bucket(min_theatre, max_theatre, other_theatre))
      features.append("META_self_movies_" + get_bucket(min_movies, max_movies, self_movies))
      features.append("META_other_movies_" + get_bucket(min_movies, max_movies, other_movies))
      features.append("META_self_concerts_" + get_bucket(min_concerts, max_concerts, self_concerts))
      features.append("META_other_concerts_" + get_bucket(min_concerts, max_concerts, other_concerts))
      features.append("META_self_music_" + get_bucket(min_music, max_music, self_music))
      features.append("META_other_music_" + get_bucket(min_music, max_music, other_music))
      features.append("META_self_shopping_" + get_bucket(min_shopping, max_shopping, self_shopping))
      features.append("META_other_shopping_" + get_bucket(min_shopping, max_shopping, other_shopping))
      features.append("META_self_yoga_" + get_bucket(min_yoga, max_yoga, self_yoga))
      features.append("META_other_yoga_" + get_bucket(min_yoga, max_yoga, other_yoga))
      features.append("META_self_samerace_" + get_bucket(min_samerace, max_samerace, self_samerace))
      features.append("META_other_samerace_" + get_bucket(min_samerace, max_samerace, other_samerace))
      features.append("META_self_ss1atrct_" + get_bucket(min_ss1atrct, max_ss1atrct, self_ss1atrct))
      features.append("META_other_ss1atrct_" + get_bucket(min_ss1atrct, max_ss1atrct, other_ss1atrct))
      features.append("META_self_ss1sincr_" + get_bucket(min_ss1sincr, max_ss1sincr, self_ss1sincr))
      features.append("META_other_ss1sincr_" + get_bucket(min_ss1sincr, max_ss1sincr, other_ss1sincr))
      features.append("META_self_ss1intel_" + get_bucket(min_ss1intel, max_ss1intel, self_ss1intel))
      features.append("META_other_ss1intel_" + get_bucket(min_ss1intel, max_ss1intel, other_ss1intel))
      features.append("META_self_ss1funny_" + get_bucket(min_ss1funny, max_ss1funny, self_ss1funny))
      features.append("META_other_ss1funny_" + get_bucket(min_ss1funny, max_ss1funny, other_ss1funny))
      features.append("META_self_ss1ambit_" + get_bucket(min_ss1ambit, max_ss1ambit, self_ss1ambit))
      features.append("META_other_ss1ambit_" + get_bucket(min_ss1ambit, max_ss1ambit, other_ss1ambit))
      features.append("META_self_ss1wlthy_" + get_bucket(min_ss1wlthy, max_ss1wlthy, self_ss1wlthy))
      features.append("META_other_ss1wlthy_" + get_bucket(min_ss1wlthy, max_ss1wlthy, other_ss1wlthy))
      features.append("META_self_ss1court_" + get_bucket(min_ss1court, max_ss1court, self_ss1court))
      features.append("META_other_ss1court_" + get_bucket(min_ss1court, max_ss1court, other_ss1court))
      features.append("META_self_os1atrct_" + get_bucket(min_os1atrct, max_os1atrct, self_os1atrct))
      features.append("META_other_os1atrct_" + get_bucket(min_os1atrct, max_os1atrct, other_os1atrct))
      features.append("META_self_os1sincr_" + get_bucket(min_os1sincr, max_os1sincr, self_os1sincr))
      features.append("META_other_os1sincr_" + get_bucket(min_os1sincr, max_os1sincr, other_os1sincr))
      features.append("META_self_os1intel_" + get_bucket(min_os1intel, max_os1intel, self_os1intel))
      features.append("META_other_os1intel_" + get_bucket(min_os1intel, max_os1intel, other_os1intel))
      features.append("META_self_os1funny_" + get_bucket(min_os1funny, max_os1funny, self_os1funny))
      features.append("META_other_os1funny_" + get_bucket(min_os1funny, max_os1funny, other_os1funny))
      features.append("META_self_os1ambit_" + get_bucket(min_os1ambit, max_os1ambit, self_os1ambit))
      features.append("META_other_os1ambit_" + get_bucket(min_os1ambit, max_os1ambit, other_os1ambit))
      features.append("META_self_os1wlthy_" + get_bucket(min_os1wlthy, max_os1wlthy, self_os1wlthy))
      features.append("META_other_os1wlthy_" + get_bucket(min_os1wlthy, max_os1wlthy, other_os1wlthy))
      features.append("META_self_os1court_" + get_bucket(min_os1court, max_os1court, self_os1court))
      features.append("META_other_os1court_" + get_bucket(min_os1court, max_os1court, other_os1court))
      features.append("META_self_sd1atrct_" + get_bucket(min_sd1atrct, max_sd1atrct, self_sd1atrct))
      features.append("META_other_sd1atrct_" + get_bucket(min_sd1atrct, max_sd1atrct, other_sd1atrct))
      features.append("META_self_sd1sincr_" + get_bucket(min_sd1sincr, max_sd1sincr, self_sd1sincr))
      features.append("META_other_sd1sincr_" + get_bucket(min_sd1sincr, max_sd1sincr, other_sd1sincr))
      features.append("META_self_sd1intel_" + get_bucket(min_sd1intel, max_sd1intel, self_sd1intel))
      features.append("META_other_sd1intel_" + get_bucket(min_sd1intel, max_sd1intel, other_sd1intel))
      features.append("META_self_sd1funny_" + get_bucket(min_sd1funny, max_sd1funny, self_sd1funny))
      features.append("META_other_sd1funny_" + get_bucket(min_sd1funny, max_sd1funny, other_sd1funny))
      features.append("META_self_sd1ambit_" + get_bucket(min_sd1ambit, max_sd1ambit, self_sd1ambit))
      features.append("META_other_sd1ambit_" + get_bucket(min_sd1ambit, max_sd1ambit, other_sd1ambit))
      features.append("META_self_sd1shrd_" + get_bucket(min_sd1shrd, max_sd1shrd, self_sd1shrd))
      features.append("META_other_sd1shrd_" + get_bucket(min_sd1shrd, max_sd1shrd, other_sd1shrd))
      features.append("META_self_sd1wlthy_" + get_bucket(min_sd1wlthy, max_sd1wlthy, self_sd1wlthy))
      features.append("META_other_sd1wlthy_" + get_bucket(min_sd1wlthy, max_sd1wlthy, other_sd1wlthy))
      features.append("META_self_sd1court_" + get_bucket(min_sd1court, max_sd1court, self_sd1court))
      features.append("META_other_sd1court_" + get_bucket(min_sd1court, max_sd1court, other_sd1court))
      features.append("META_self_od1atrct_" + get_bucket(min_od1atrct, max_od1atrct, self_od1atrct))
      features.append("META_other_od1atrct_" + get_bucket(min_od1atrct, max_od1atrct, other_od1atrct))
      features.append("META_self_od1sincr_" + get_bucket(min_od1sincr, max_od1sincr, self_od1sincr))
      features.append("META_other_od1sincr_" + get_bucket(min_od1sincr, max_od1sincr, other_od1sincr))
      features.append("META_self_od1intel_" + get_bucket(min_od1intel, max_od1intel, self_od1intel))
      features.append("META_other_od1intel_" + get_bucket(min_od1intel, max_od1intel, other_od1intel))
      features.append("META_self_od1funny_" + get_bucket(min_od1funny, max_od1funny, self_od1funny))
      features.append("META_other_od1funny_" + get_bucket(min_od1funny, max_od1funny, other_od1funny))
      features.append("META_self_od1ambit_" + get_bucket(min_od1ambit, max_od1ambit, self_od1ambit))
      features.append("META_other_od1ambit_" + get_bucket(min_od1ambit, max_od1ambit, other_od1ambit))
      features.append("META_self_od1shrd_" + get_bucket(min_od1shrd, max_od1shrd, self_od1shrd))
      features.append("META_other_od1shrd_" + get_bucket(min_od1shrd, max_od1shrd, other_od1shrd))
      features.append("META_self_od1wlthy_" + get_bucket(min_od1wlthy, max_od1wlthy, self_od1wlthy))
      features.append("META_other_od1wlthy_" + get_bucket(min_od1wlthy, max_od1wlthy, other_od1wlthy))
      features.append("META_self_od1court_" + get_bucket(min_od1court, max_od1court, self_od1court))
      features.append("META_other_od1court_" + get_bucket(min_od1court, max_od1court, other_od1court))
      features.append("META_self_fd1atrct_" + get_bucket(min_fd1atrct, max_fd1atrct, self_fd1atrct))
      features.append("META_other_fd1atrct_" + get_bucket(min_fd1atrct, max_fd1atrct, other_fd1atrct))
      features.append("META_self_fd1sincr_" + get_bucket(min_fd1sincr, max_fd1sincr, self_fd1sincr))
      features.append("META_other_fd1sincr_" + get_bucket(min_fd1sincr, max_fd1sincr, other_fd1sincr))
      features.append("META_self_fd1intel_" + get_bucket(min_fd1intel, max_fd1intel, self_fd1intel))
      features.append("META_other_fd1intel_" + get_bucket(min_fd1intel, max_fd1intel, other_fd1intel))
      features.append("META_self_fd1funny_" + get_bucket(min_fd1funny, max_fd1funny, self_fd1funny))
      features.append("META_other_fd1funny_" + get_bucket(min_fd1funny, max_fd1funny, other_fd1funny))
      features.append("META_self_fd1ambit_" + get_bucket(min_fd1ambit, max_fd1ambit, self_fd1ambit))
      features.append("META_other_fd1ambit_" + get_bucket(min_fd1ambit, max_fd1ambit, other_fd1ambit))
      features.append("META_self_fd1shrd_" + get_bucket(min_fd1shrd, max_fd1shrd, self_fd1shrd))
      features.append("META_other_fd1shrd_" + get_bucket(min_fd1shrd, max_fd1shrd, other_fd1shrd))
      features.append("META_self_fd1wlthy_" + get_bucket(min_fd1wlthy, max_fd1wlthy, self_fd1wlthy))
      features.append("META_other_fd1wlthy_" + get_bucket(min_fd1wlthy, max_fd1wlthy, other_fd1wlthy))
      features.append("META_self_fd1court_" + get_bucket(min_fd1court, max_fd1court, self_fd1court))
      features.append("META_other_fd1court_" + get_bucket(min_fd1court, max_fd1court, other_fd1court))
      features.append("META_self_Subject_" + get_bucket(min_Subject, max_Subject, self_Subject))
      features.append("META_other_Subject_" + get_bucket(min_Subject, max_Subject, other_Subject))
      features.append("META_self_UnderStat_" + get_bucket(min_UnderStat, max_UnderStat, self_UnderStat))
      features.append("META_other_UnderStat_" + get_bucket(min_UnderStat, max_UnderStat, other_UnderStat))
      features.append("META_self_ForeignBorn_" + get_bucket(min_ForeignBorn, max_ForeignBorn, self_ForeignBorn))
      features.append("META_other_ForeignBorn_" + get_bucket(min_ForeignBorn, max_ForeignBorn, other_ForeignBorn))

    if textual == '0':
      pass
    elif textual == '2':
      features.append("TEXTUAL_self_tot_words_" + get_bucket(min_tot_words, max_tot_words, self_tot_words))
      features.append("TEXTUAL_other_tot_words_" + get_bucket(min_tot_words, max_tot_words, other_tot_words))
      features.append("TEXTUAL_self_love_" + get_bucket(min_love, max_love, self_love))
      features.append("TEXTUAL_other_love_" + get_bucket(min_love, max_love, other_love))
      features.append("TEXTUAL_self_i_mean_discourse_" + get_bucket(min_i_mean_discourse, max_i_mean_discourse, self_i_mean_discourse))
      features.append("TEXTUAL_other_i_mean_discourse_" + get_bucket(min_i_mean_discourse, max_i_mean_discourse, other_i_mean_discourse))
      features.append("TEXTUAL_self_sex_" + get_bucket(min_sex, max_sex, self_sex))
      features.append("TEXTUAL_other_sex_" + get_bucket(min_sex, max_sex, other_sex))
      features.append("TEXTUAL_self_meta_" + get_bucket(min_meta, max_meta, self_meta))
      features.append("TEXTUAL_other_meta_" + get_bucket(min_meta, max_meta, other_meta))
      features.append("TEXTUAL_self_negate_" + get_bucket(min_negate, max_negate, self_negate))
      features.append("TEXTUAL_other_negate_" + get_bucket(min_negate, max_negate, other_negate))
      features.append("TEXTUAL_self_um_discourse_" + get_bucket(min_um_discourse, max_um_discourse, self_um_discourse))
      features.append("TEXTUAL_other_um_discourse_" + get_bucket(min_um_discourse, max_um_discourse, other_um_discourse))
      features.append("TEXTUAL_self_negemo_" + get_bucket(min_negemo, max_negemo, self_negemo))
      features.append("TEXTUAL_other_negemo_" + get_bucket(min_negemo, max_negemo, other_negemo))
      features.append("TEXTUAL_self_appreciation_" + get_bucket(min_appreciation, max_appreciation, self_appreciation))
      features.append("TEXTUAL_other_appreciation_" + get_bucket(min_appreciation, max_appreciation, other_appreciation))
      features.append("TEXTUAL_self_tot_question_words_" + get_bucket(min_tot_question_words, max_tot_question_words, self_tot_question_words))
      features.append("TEXTUAL_other_tot_question_words_" + get_bucket(min_tot_question_words, max_tot_question_words, other_tot_question_words))
      features.append("TEXTUAL_self_you_know_discourse_" + get_bucket(min_you_know_discourse, max_you_know_discourse, self_you_know_discourse))
      features.append("TEXTUAL_other_you_know_discourse_" + get_bucket(min_you_know_discourse, max_you_know_discourse, other_you_know_discourse))
      features.append("TEXTUAL_self_hate_" + get_bucket(min_hate, max_hate, self_hate))
      features.append("TEXTUAL_other_hate_" + get_bucket(min_hate, max_hate, other_hate))
      features.append("TEXTUAL_self_food_" + get_bucket(min_food, max_food, self_food))
      features.append("TEXTUAL_other_food_" + get_bucket(min_food, max_food, other_food))
      features.append("TEXTUAL_self_uh_discourse_" + get_bucket(min_uh_discourse, max_uh_discourse, self_uh_discourse))
      features.append("TEXTUAL_other_uh_discourse_" + get_bucket(min_uh_discourse, max_uh_discourse, other_uh_discourse))
      features.append("TEXTUAL_self_you_" + get_bucket(min_you, max_you, self_you))
      features.append("TEXTUAL_other_you_" + get_bucket(min_you, max_you, other_you))
      features.append("TEXTUAL_self_I_" + get_bucket(min_I, max_I, self_I))
      features.append("TEXTUAL_other_I_" + get_bucket(min_I, max_I, other_I))
      features.append("TEXTUAL_self_drink_" + get_bucket(min_drink, max_drink, self_drink))
      features.append("TEXTUAL_other_drink_" + get_bucket(min_drink, max_drink, other_drink))
      features.append("TEXTUAL_self_like_discourse_" + get_bucket(min_like_discourse, max_like_discourse, self_like_discourse))
      features.append("TEXTUAL_other_like_discourse_" + get_bucket(min_like_discourse, max_like_discourse, other_like_discourse))
      features.append("TEXTUAL_self_hedge_" + get_bucket(min_hedge, max_hedge, self_hedge))
      features.append("TEXTUAL_other_hedge_" + get_bucket(min_hedge, max_hedge, other_hedge))
      features.append("TEXTUAL_self_academics_" + get_bucket(min_academics, max_academics, self_academics))
      features.append("TEXTUAL_other_academics_" + get_bucket(min_academics, max_academics, other_academics))
      features.append("TEXTUAL_self_laughter_" + get_bucket(min_laughter, max_laughter, self_laughter))
      features.append("TEXTUAL_other_laughter_" + get_bucket(min_laughter, max_laughter, other_laughter))
      features.append("TEXTUAL_self_agree_" + get_bucket(min_agree, max_agree, self_agree))
      features.append("TEXTUAL_other_agree_" + get_bucket(min_agree, max_agree, other_agree))


    for feat in features:
        print "%s\t%s" % (dateid, feat)

    
