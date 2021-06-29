
​use homeschooldb
create table student(
    name_ VARCHAR(25) PRIMARY KEY,
    class VARCHAR(10),
    email VARCHAR(35),
    phone VARCHAR(10),
    FOREIGN KEY (class) REFERENCES class(name_)
);
​
create table teacher(
    name_ VARCHAR(25) PRIMARY KEY,
    email VARCHAR(35),
    phone VARCHAR(10)
);
​
create table subject_(
    id SMALLINT PRIMARY KEY,
    teacher VARCHAR(25),
    name_ VARCHAR(15),
    zoom_link VARCHAR(50),
    FOREIGN KEY (teacher) REFERENCES teacher(name_)
);
​
create table week_schedule(
    class VARCHAR(10),
    day_ TINYINT,
    hour TIME,
    subject_id SMALLINT,
    PRIMARY KEY (class, day_, hour),
    FOREIGN KEY (subject_id) REFERENCES subject_(id),
    FOREIGN KEY (class) REFERENCES class(name_)
);
​
create table lesson(
    id VARCHAR(15) PRIMARY KEY,
    class VARCHAR(10),
    day_ TINYINT,
    hour TIME,
    date_ DATETIME,
    descr VARCHAR(50),
    homework VARCHAR(100),
    FOREIGN KEY (class, day_, hour) REFERENCES week_schedule(class, day_, hour)
);

drop table lesson;
create table task(
    id SMALLINT PRIMARY KEY AUTO_INCREMENT,
    class VARCHAR(10),
    day_ TINYINT,
    hour TIME,
    date_ DATETIME,
    homework VARCHAR(100),
    FOREIGN KEY (class, day_, hour) REFERENCES week_schedule(class, day_, hour)
);

create table student_task(
    name_ VARCHAR(25),
    task_id SMALLINT,
    is_done boolean,
    PRIMARY KEY(name_, task_id),
    FOREIGN KEY (name_) REFERENCES student(name_),
    FOREIGN KEY (task_id) REFERENCES task(id)
);

create table fun_task(   
    class VARCHAR(10),
    descr VARCHAR(100),
    link VARCHAR(200),
    PRIMARY KEY(descr, link)
);