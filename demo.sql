CREATE TABLE 'users' (
  id serial,
  name varchar(255),
  bio,
  website,
  profile_picture_path,
  access_level
);

-- Get all mods or admins
select * from users where access_level >= 2;
