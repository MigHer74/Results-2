DELETE FROM games WHERE idtype = 2 AND gameweek = 'W6';

UPDATE games SET gameweek = 'W6' WHERE idtype = 2 AND gameweek = 'W5';
UPDATE games SET gameweek = 'W5' WHERE idtype = 2 AND gameweek = 'W4';
UPDATE games SET gameweek = 'W4' WHERE idtype = 2 AND gameweek = 'W3';
UPDATE games SET gameweek = 'W3' WHERE idtype = 2 AND gameweek = 'W2';
UPDATE games SET gameweek = 'W2' WHERE idtype = 2 AND gameweek = 'W1';
