DROP TABLE IF EXISTS notifications;
DROP TABLE IF EXISTS applications;
DROP TABLE IF EXISTS projects_roles;
DROP TABLE IF EXISTS projects_pictures;
DROP TABLE IF EXISTS posts;
DROP TABLE IF EXISTS messages;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS projects;
DROP TABLE IF EXISTS themes;


DROP TRIGGER IF EXISTS validate_percentage;
DROP TRIGGER IF EXISTS send_notification_on_application;
DROP PROCEDURE IF EXISTS accept_application;
DROP PROCEDURE IF EXISTS reject_application;

CREATE TABLE IF NOT EXISTS users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255),
  email VARCHAR(255) UNIQUE,
  role VARCHAR(255),
  password VARCHAR(255),
  picture VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS themes (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255),
  color VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS projects (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255),
  theme_id INT,
  description TEXT,
  status VARCHAR(255),
  progress INT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (theme_id) REFERENCES themes(id)
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

CREATE TABLE IF NOT EXISTS notifications (
  id INT AUTO_INCREMENT PRIMARY KEY,
  user_id INT,
  message TEXT,
  application_id INT,
  sent_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (user_id) REFERENCES users(id),
  FOREIGN KEY (application_id) REFERENCES applications(id)
);


INSERT INTO users (name, email, role, password, picture) VALUES ('John Doe', 'johndoe@hotmail.com', 'Développer', '$2b$12$pgfA4t4v8Lk7Ok9UvAlVCuhz2M1oDabz9ImA6sVlhGarpzQZxDC9a', '/avatar2.png');
INSERT INTO users (name, email, role, password, picture) VALUES ('Jane Doe', 'janedoe@hotmail.com', 'Designer', '$2b$12$pgfA4t4v8Lk7Ok9UvAlVCuhz2M1oDabz9ImA6sVlhGarpzQZxDC9a', '/avatar.png');


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

DELIMITER //
CREATE TRIGGER send_notification_on_application
AFTER INSERT ON applications
FOR EACH ROW
BEGIN
  DECLARE proid INT;
  SET proid = (SELECT project_id FROM projects_roles WHERE id = NEW.role_id LIMIT 1);

  INSERT INTO notifications (user_id, message, application_id)
  SELECT pr.user_id, CONCAT('A new application has been submitted for ', p.name), NEW.id
  FROM projects_roles pr
  INNER JOIN projects p ON pr.project_id = p.id
  WHERE pr.project_id = proid AND pr.user_id IS NOT NULL;
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE accept_application(IN app_id INT)
BEGIN
  UPDATE projects_roles pr SET user_id = (SELECT user_id FROM applications WHERE id = app_id LIMIT 1)
  WHERE pr.id = (SELECT role_id FROM applications WHERE id = app_id LIMIT 1);
  
  DELETE FROM notifications WHERE application_id = app_id;
  DELETE FROM applications WHERE id = app_id;
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE reject_application(IN app_id INT)
BEGIN
  DELETE FROM notifications WHERE application_id = app_id;
  DELETE FROM applications WHERE id = app_id;
END //
DELIMITER ;
