
-- our dataset
DROP TABLE IF EXISTS original_features CASCADE;
CREATE TABLE original_features (
  dateid text,
  turnnum integer,
  gender text,
  tnstart double precision,
  tnend double precision,
  tndur double precision,
  pmin double precision,
  ptmin double precision,
  pmax double precision,
  ptmax double precision,
  pquan double precision,
  pmean double precision,
  psd double precision,
  pslope double precision,
  pslnjmp double precision,
  imin double precision,
  itmin double precision,
  imax double precision,
  itmax double precision,
  iquan double precision,
  imean double precision,
  transcript text
);

DROP TABLE IF EXISTS person_meta_features;
CREATE TABLE person_meta_features (
  person_id text,
  female double precision,
  race double precision,
  evntgoal double precision,
  frqdates double precision,
  frqsocl double precision,
  sdbefore double precision,
  height double precision,
  weight double precision,
  hairclr double precision,
  plysprt double precision,
  wtchsprt double precision,
  bdybuild double precision,
  dining double precision,
  museum double precision,
  art double precision,
  hiking double precision,
  videogam double precision,
  dancing double precision,
  reading double precision,
  tv double precision,
  theatre double precision,
  movies double precision,
  concerts double precision,
  music double precision,
  shopping double precision,
  yoga double precision,
  samerace double precision,
  ss1atrct double precision,
  ss1sincr double precision,
  ss1intel double precision,
  ss1funny double precision,
  ss1ambit double precision,
  ss1wlthy double precision,
  ss1court double precision,
  os1atrct double precision,
  os1sincr double precision,
  os1intel double precision,
  os1funny double precision,
  os1ambit double precision,
  os1wlthy double precision,
  os1court double precision,
  sd1atrct double precision,
  sd1sincr double precision,
  sd1intel double precision,
  sd1funny double precision,
  sd1ambit double precision,
  sd1shrd double precision,
  sd1wlthy double precision,
  sd1court double precision,
  od1atrct double precision,
  od1sincr double precision,
  od1intel double precision,
  od1funny double precision,
  od1ambit double precision,
  od1shrd double precision,
  od1wlthy double precision,
  od1court double precision,
  fd1atrct double precision,
  fd1sincr double precision,
  fd1intel double precision,
  fd1funny double precision,
  fd1ambit double precision,
  fd1shrd double precision,
  fd1wlthy double precision,
  fd1court double precision,
  Subject double precision,
  UnderStat double precision,
  ForeignBorn double precision
);

DROP TABLE IF EXISTS prosodic_features;
CREATE TABLE prosodic_features (
  dateid text,
  self_id text,
  other_id text,
  talked_first integer,
  turn_duration double precision,
  turn_duration_sd double precision,
  f0_min double precision,
  f0_min_sd double precision,
  f0_max double precision,
  f0_max_sd double precision,
  f0_mean double precision,
  f0_mean_sd double precision,
  f0_sd double precision,
  f0_sd_sd double precision,
  pitch_range double precision,
  pitch_range_sd double precision,
  rms_min double precision,
  rms_min_sd double precision,
  rms_max double precision,
  rms_max_sd double precision,
  rms_mean double precision,
  rms_mean_sd double precision
);

DROP TABLE IF EXISTS textual_features;
CREATE TABLE textual_features (
  dateid text,
  self_id text,
  other_id text,
  tot_words double precision,
  love double precision,
  i_mean_discourse double precision,
  sex double precision,
  meta double precision,
  negate double precision,
  um_discourse double precision,
  negemo double precision,
  appreciation double precision,
  tot_question_words double precision,
  you_know_discourse double precision,
  hate double precision,
  food double precision,
  uh_discourse double precision,
  you double precision,
  I double precision,
  drink double precision,
  like_discourse double precision,
  hedge double precision,
  academics double precision,
  laughter double precision,
  agree double precision
);

DROP TABLE IF EXISTS outut_labels;
CREATE TABLE output_labels (
  dateid text,
  self_id text,
  other_id text,
  label text,
  type text -- TRAIN or TEST
);

-- the features for each date
DROP TABLE IF EXISTS date_feature CASCADE;
CREATE TABLE date_feature (
  dateid text,
  feature text
);

-- contains the variable we want to predict
DROP TABLE IF EXISTS output CASCADE;
CREATE TABLE output (
  dateid text,
  is_enjoyable boolean,
  id bigint
);
