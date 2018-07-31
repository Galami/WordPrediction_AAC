-- Création des tables
CREATE TABLE _1_gram (word TEXT, count INTEGER, UNIQUE(word))
CREATE TABLE _2_gram (word_1 TEXT, word TEXT, count INTEGER, UNIQUE(word_1, word))
CREATE TABLE _3_gram (word_2 TEXT, word_1 TEXT, word TEXT, count INTEGER, UNIQUE(word_2, word_1, word))

-- Création des index
CREATE INDEX idx__1_gram ON _1_gram (word)
CREATE INDEX idx__2_gram ON _2_gram (word_1, word)
CREATE INDEX idx__3_gram ON _3_gram (word_2, word_1, word)

-- Google Books Ngram : statistiques (avant suppression)
SELECT AVG(count) FROM -- _1_gram : 3 846,589 _2_gram : 278,848 _3_gram : 67,832
SELECT SUM(count) FROM -- _1_gram; _2_gram; _3_gram;
-- 4 881 398 607; 3 599 520 908; 2 211 946 087;
SELECT word, max(count) FROM -- _1_gram; _2_gram; _3_gram;
-- 272 494 238 (de); 48 281 184 (de la); 1 928 766 (et de la);

-- Méthode empirique pour déterminer les seuils de suppression
SELECT * FROM -- _1_gram _2_gram _3_gram
WHERE count < -- 200 50 10
ORDER BY count DESC

-- Suppression des unigrammes < 200 (les mêmes dans les bigrammes et trigrammes)
CREATE TABLE under200 AS SELECT * from _1_gram WHERE count < 200
DELETE FROM _1_gram WHERE word IN (SELECT word FROM under200); -- 1 045 917 rows
DELETE FROM _2_gram WHERE word IN (SELECT word FROM under200); -- 491 286 rows
DELETE FROM _2_gram WHERE word_1 IN (SELECT word FROM under200); -- 305 284 rows
DELETE FROM _3_gram WHERE word IN (SELECT word FROM under200); -- 108 316 rows
DELETE FROM _3_gram WHERE word_1 IN (SELECT word FROM under200); -- 70 067 rows
DELETE FROM _3_gram WHERE word_2 IN (SELECT word FROM under200); -- 41 267 rows
CREATE TABLE under50 AS SELECT * from _2_gram WHERE count < 50
DELETE FROM _2_gram WHERE count < 50 -- 8 926 604 rows
CREATE TABLE under10 AS SELECT * from _3_gram WHERE count < 10
DELETE FROM _3_gram WHERE count < 10 -- 13 295 814 rows
DROP TABLE under200; DROP TABLE under50; DROP TABLE under10;