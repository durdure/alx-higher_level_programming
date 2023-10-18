--creates the table unique_id on your MySQL server.
  -- unique_id description:
     -- id INT - default 1, must be unique.
     -- name VARCHAR(256).
  -- The databace name will be passed as an argument of the mysql command.
  -- If the table unique_id already exists, your script should fail.
CREATE TABLE IF NOT EXISTS unique_id(id INT DEFAULT 1, UNIQUE(ID), name VARCHAR(256));
