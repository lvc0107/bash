CREATE TABLE tags
( id numeric(10) not null,
  name varchar2(50) not null,
  weight  varchar2(50) not null,
  CONSTRAINT tag_pk PRIMARY KEY (id)
);


INSERT INTO tags (id, NAME, weight) VALUES (1, 'A', 'A'); 
INSERT INTO tags (id, NAME, weight) VALUES (2, 'B', 'B'); 
INSERT INTO tags (id, NAME, weight) VALUES (3, 'C', 'C'); 
INSERT INTO tags (id, NAME, weight) VALUES (4, 'D', 'D'); 
INSERT INTO tags (id, NAME, weight) VALUES (5, 'E', 'E'); 
INSERT INTO tags (id, NAME, weight) VALUES (6, 'F', 'F'); 

CREATE TABLE tracks
( id numeric(10) not null,
  title varchar2(50) not null,
  duration numeric(10) not null,
  mbid varchar2(50) not null,
  CONSTRAINT track_pk PRIMARY KEY (id)
);


INSERT INTO tracks (id, title, duration, mbid) VALUES (1, 'Acancion1', 310, 'AA'); 
INSERT INTO tracks (id, title, duration, mbid) VALUES (2, 'Acancion2', 410, 'AA'); 
INSERT INTO tracks (id, title, duration, mbid) VALUES (3, 'cancion3', 210, 'AA'); 
INSERT INTO tracks (id, title, duration, mbid) VALUES (4, 'cancion4', 510, 'AA'); 
INSERT INTO tracks (id, title, duration, mbid) VALUES (5, 'cancion5', 110, 'AA'); 
INSERT INTO tracks (id, title, duration, mbid) VALUES (6, 'cancion6', 110, 'AA'); 

CREATE TABLE Tags_tracks
( tag_id numeric(10) not null,
  track_id numeric(10) not null,
  CONSTRAINT tags_tracks_pk PRIMARY KEY (tag_id, track_id),
  CONSTRAINT fk_tracks FOREIGN KEY (track_id)  REFERENCES tracks(id),
  CONSTRAINT fk_tags FOREIGN KEY (tag_id)  REFERENCES tags(id)
);


INSERT INTO Tags_tracks (tag_id, track_id) VALUES (1, 1); 
INSERT INTO Tags_tracks (tag_id, track_id) VALUES (1, 2); 
INSERT INTO Tags_tracks (tag_id, track_id) VALUES (1, 3); 
INSERT INTO Tags_tracks (tag_id, track_id) VALUES (1, 4); 
INSERT INTO Tags_tracks (tag_id, track_id) VALUES (1, 5); 
INSERT INTO Tags_tracks (tag_id, track_id) VALUES (1, 6); 
INSERT INTO Tags_tracks (tag_id, track_id) VALUES (2, 1); 
INSERT INTO Tags_tracks (tag_id, track_id) VALUES (2, 2); 
INSERT INTO Tags_tracks (tag_id, track_id) VALUES (2, 3); 
INSERT INTO Tags_tracks (tag_id, track_id) VALUES (2, 4); 
INSERT INTO Tags_tracks (tag_id, track_id) VALUES (2, 5); 
INSERT INTO Tags_tracks (tag_id, track_id) VALUES (2, 6); 
INSERT INTO Tags_tracks (tag_id, track_id) VALUES (3, 1); 
INSERT INTO Tags_tracks (tag_id, track_id) VALUES (3, 2); 
INSERT INTO Tags_tracks (tag_id, track_id) VALUES (3, 3); 
INSERT INTO Tags_tracks (tag_id, track_id) VALUES (3, 4); 
INSERT INTO Tags_tracks (tag_id, track_id) VALUES (3, 5); 
INSERT INTO Tags_tracks (tag_id, track_id) VALUES (3, 6); 
INSERT INTO Tags_tracks (tag_id, track_id) VALUES (4, 1); 
INSERT INTO Tags_tracks (tag_id, track_id) VALUES (4, 2); 
INSERT INTO Tags_tracks (tag_id, track_id) VALUES (4, 3); 
INSERT INTO Tags_tracks (tag_id, track_id) VALUES (4, 4); 
INSERT INTO Tags_tracks (tag_id, track_id) VALUES (4, 5); 
INSERT INTO Tags_tracks (tag_id, track_id) VALUES (4, 6); 
INSERT INTO Tags_tracks (tag_id, track_id) VALUES (5, 1); 
INSERT INTO Tags_tracks (tag_id, track_id) VALUES (5, 2); 
INSERT INTO Tags_tracks (tag_id, track_id) VALUES (5, 3); 
INSERT INTO Tags_tracks (tag_id, track_id) VALUES (5, 4); 
INSERT INTO Tags_tracks (tag_id, track_id) VALUES (5, 5); 
INSERT INTO Tags_tracks (tag_id, track_id) VALUES (5, 6); 
INSERT INTO Tags_tracks (tag_id, track_id) VALUES (6, 1); 
INSERT INTO Tags_tracks (tag_id, track_id) VALUES (6, 2); 
INSERT INTO Tags_tracks (tag_id, track_id) VALUES (6, 3); 
INSERT INTO Tags_tracks (tag_id, track_id) VALUES (6, 4); 
INSERT INTO Tags_tracks (tag_id, track_id) VALUES (6, 5); 
INSERT INTO Tags_tracks (tag_id, track_id) VALUES (6, 6); 

SELECT * FROM tracks WHERE duration >= 300 and title LIKE 'A%';


/*SELECT t.name FROM Tags_tracks tt JOIN tracks t ON t.id = tt.tag_id and tt.tag_id = Null; */
SELECT t.name FROM tracks;
/*SELECT t.name FROM tracks t left outer join Tags_tracks tt ON t.id = tt.tag_id where tt.tag_id is null;*/

/*SELECT t.name FROM tracks t left outer join Tags_tracks tt ON t.id = tt.tag_id where tt.tag_id is null; */