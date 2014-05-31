

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

DROP TABLE IF EXISTS unigram CASCADE;
CREATE TABLE unigram (
  dateid text,
  feature text
);