CREATE TABLE Types (
    nomtype VARCHAR(20),
    typeLP VARCHAR(9),
    PRIMARY KEY (typeLP)
);

CREATE TABLE Segment (
    indIP VARCHAR(11),
    nomSegment VARCHAR(20) NOT NULL,
    etage TINYINT(1),
    nbposte TINYINT(2),
    PRIMARY KEY (indIP) 
);  

CREATE TABLE Slle (
    nsalle VARCHAR(9),
    indIP VARCHAR(11) NOT NULL,
    nomsalle VARCHAR(30) NOT NULL,
    nbposte TINYINT(2),
    PRIMARY KEY (nsalle)
);

CREATE TABLE Poste (
    typeLP VARCHAR(9) NOT NULL,
    nposte VARCHAR(7),
    nomposte VARCHAR(20) NOT NULL,
    indIP VARCHAR(11),
    ad INT CHECK (ad >= 0 AND ad <= 255),
    nsalle VARCHAR(7),
    FOREIGN KEY (nsalle) REFERENCES Slle(nsalle),
    FOREIGN KEY (indIP) REFERENCES Segment(indIP),
    FOREIGN KEY (typeLP) REFERENCES Types(typeLP),
    nblog TINYINT(2),
    PRIMARY KEY (nposte)
);

CREATE TABLE Logiciel (
    nlog VARCHAR(5),
    nomlog VARCHAR(20),
    dateach DATETIME,
    version VARCHAR(7),
    typelog VARCHAR(9) NOT NULL,
    prix DECIMAL(6,2) NOT NULL,
    PRIMARY KEY (nlog)
);

CREATE TABLE Installer (
    nposte VARCHAR(7) UNIQUE,
    nlog VARCHAR(5),
    numIns INTEGER(5),
    dateIns TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    delai SMALLINT,
    FOREIGN KEY (nlog) REFERENCES Logiciel(nlog),
    FOREIGN KEY (nposte) REFERENCES Poste(nposte),
    PRIMARY KEY (numIns)
);
