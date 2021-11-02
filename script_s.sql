DELETE FROM games WHERE idtype = 'A' AND gameweek = 'W6';

UPDATE games SET gameweek = 'W6' WHERE idtype = 'A' AND gameweek = 'W5';
UPDATE games SET gameweek = 'W5' WHERE idtype = 'A' AND gameweek = 'W4';
UPDATE games SET gameweek = 'W4' WHERE idtype = 'A' AND gameweek = 'W3';
UPDATE games SET gameweek = 'W3' WHERE idtype = 'A' AND gameweek = 'W2';
UPDATE games SET gameweek = 'W2' WHERE idtype = 'A' AND gameweek = 'W1';
