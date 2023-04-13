DROP TABLE IF EXISTS applications;
DROP TABLE IF EXISTS projects_roles;
DROP TABLE IF EXISTS projects_pictures;
DROP TABLE IF EXISTS posts;
DROP TABLE IF EXISTS messages;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS projects;

DROP TRIGGER IF EXISTS validate_percentage;

CREATE TABLE IF NOT EXISTS users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255),
  email VARCHAR(255),
  role VARCHAR(255),
  password VARCHAR(255),
  picture VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS projects (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255),
  description TEXT,
  status VARCHAR(255),
  progress INT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS projects_pictures (
  project_id INT,
  path VARCHAR(255),
  FOREIGN KEY (project_id) REFERENCES projects(id)
);

-- Lien entre les rôles disponibles dans un projet et les utilisateurs qui les occupent.
-- Si le user_id est NULL, alors le rôle est vacant.
CREATE TABLE IF NOT EXISTS projects_roles (
  id INT AUTO_INCREMENT PRIMARY KEY,
  project_id INT,
  user_id INT,
  name VARCHAR(255),
  FOREIGN KEY (project_id) REFERENCES projects(id),
  FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE IF NOT EXISTS posts (
  id INT AUTO_INCREMENT PRIMARY KEY,
  author_id INT,
  project_id INT,
  content TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (author_id) REFERENCES users(id),
  FOREIGN KEY (project_id) REFERENCES projects(id)
);

CREATE TABLE IF NOT EXISTS messages (
  id INT AUTO_INCREMENT PRIMARY KEY,
  sender_id INT,
  receiver_id INT,
  content TEXT,
  sent_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (sender_id) REFERENCES users(id),
  FOREIGN KEY (receiver_id) REFERENCES users(id)
);

CREATE TABLE IF NOT EXISTS applications (
  id INT AUTO_INCREMENT PRIMARY KEY,
  user_id INT,
  role_id INT,
  motivation TEXT,
  sent_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (user_id) REFERENCES users(id),
  FOREIGN KEY (role_id) REFERENCES projects_roles(id)
);


INSERT INTO users (name, email, role, password, picture) VALUES ('John Doe', 'johndoe@hotmail.com', 'Développer', '$2b$12$pgfA4t4v8Lk7Ok9UvAlVCuhz2M1oDabz9ImA6sVlhGarpzQZxDC9a', '/avatar2.png');
INSERT INTO users (name, email, role, password, picture) VALUES ('Jane Doe', 'janedoe@hotmail.com', 'Designer', '$2b$12$pgfA4t4v8Lk7Ok9UvAlVCuhz2M1oDabz9ImA6sVlhGarpzQZxDC9a', '/avatar.png');

INSERT INTO projects (name, description, status, progress) VALUES ('Project 1', 'Lorem ipsum dolor sit amet.', 'IN_PROGRESS', 0);
INSERT INTO projects (name, description, status, progress) VALUES ('Project 2', 'Lorem ipsum dolor sit amet.', 'DONE', 100);
INSERT INTO projects (name, description, status, progress) VALUES ('Project 3', 'Lorem ipsum dolor sit amet.', 'IN_PROGRESS', 25);

INSERT INTO posts (author_id, project_id, content) VALUES (1, 1, 'Lorem ipsum dolor sit amet.');
INSERT INTO posts (author_id, project_id, content) VALUES (1, 3, 'Lorem ipsum dolor sit amet.');
INSERT INTO posts (author_id, project_id, content) VALUES (2, 2, 'Lorem ipsum dolor sit amet.');
INSERT INTO posts (author_id, project_id, content) VALUES (2, 3, 'Lorem ipsum dolor sit amet.');

INSERT INTO projects_pictures (project_id, path) VALUES (1, '/project-background.png');
INSERT INTO projects_pictures (project_id, path) VALUES (1, '/project-background.png');
INSERT INTO projects_pictures (project_id, path) VALUES (1, '/project-background.png');

INSERT INTO projects_roles (project_id, user_id, name) VALUES (1, 1, 'Développeur');
INSERT INTO projects_roles (project_id, user_id, name) VALUES (2, 2, 'Designer');
INSERT INTO projects_roles (project_id, user_id, name) VALUES (3, 1, 'Développeur');
INSERT INTO projects_roles (project_id, user_id, name) VALUES (3, 2, 'Designer');
INSERT INTO projects_roles (project_id, user_id, name) VALUES (3, NULL, 'Artiste 3D');

DELIMITER //
CREATE TRIGGER validate_percentage
BEFORE INSERT ON projects
FOR EACH ROW
BEGIN
  IF NEW.progress < 0 OR NEW.progress > 100 THEN
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Progress must be between 0 and 100';
  END IF;
END //
DELIMITER ;



