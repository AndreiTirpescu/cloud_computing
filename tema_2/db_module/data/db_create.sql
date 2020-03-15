CREATE TABLE aliment (id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(20), price INTEGER, code VARCHAR(20) NOT NULL UNIQUE);
INSERT INTO aliment(name, price, code)  VALUES("product0", 3, "PRDCT00");
INSERT INTO aliment(name, price, code)  VALUES("product1", 4, "PRDCT01");
INSERT INTO aliment(name, price, code)  VALUES("product2", 5, "PRDCT02");
INSERT INTO aliment(name, price, code)  VALUES("product3", 6, "PRDCT03");