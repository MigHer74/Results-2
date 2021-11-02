DELETE FROM games WHERE idtype = 'B' AND gameweek = 'W6';

UPDATE games SET gameweek = 'W6' WHERE idtype = 'B' AND gameweek = 'W5';
UPDATE games SET gameweek = 'W5' WHERE idtype = 'B' AND gameweek = 'W4';
UPDATE games SET gameweek = 'W4' WHERE idtype = 'B' AND gameweek = 'W3';
UPDATE games SET gameweek = 'W3' WHERE idtype = 'B' AND gameweek = 'W2';
UPDATE games SET gameweek = 'W2' WHERE idtype = 'B' AND gameweek = 'W1';
