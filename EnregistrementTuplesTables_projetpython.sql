use `projetpython`;

#Demandeur
INSERT INTO `projetpython`.`Demandeur` (`nom`,`email`,`mdp`,`telephone`,`nbprochesfoyer`,`nomsproches`,`adresse`)
VALUES ('Jean','jean@gmail.com','jean123','0645879865',2,'sophie;emma','3 rue du Collysée');

INSERT INTO `projetpython`.`Demandeur` (`nom`,`email`,`mdp`,`telephone`,`nbprochesfoyer`,`nomsproches`,`adresse`)
VALUES ('Lilia','lilia@gmail.com','lila0','0685859865',2,'benoit;emile','10 rue de laPlace');

#Admin
INSERT INTO `projetpython`.`Admin` (`nom`,`email`,`mdp`) VALUES ('Equipe4','equipe4@gmail.com','20/20');

#Produits
#1
INSERT INTO `projetpython`.`Produit` (`nom`,`categorie`,`unite`,`prix`) 
VALUES ('sucre','sucres/sales','kg',1);

#2
INSERT INTO `projetpython`.`Produit` (`nom`,`categorie`,`unite`,`prix`) 
VALUES ('pates','féculents','kg',1.2);

#3
INSERT INTO `projetpython`.`Produit` (`nom`,`categorie`,`unite`,`prix`) 
VALUES ('riz','féculents','kg',1.3);

#4
INSERT INTO `projetpython`.`Produit` (`nom`,`categorie`,`unite`,`prix`) 
VALUES ('semoule','féculents','kg',1.1);

#5
INSERT INTO `projetpython`.`Produit` (`nom`,`categorie`,`unite`,`prix`) 
VALUES ('légumes secs','fruits et légumes','kg',1);

#6
INSERT INTO `projetpython`.`Produit` (`nom`,`categorie`,`unite`,`prix`) 
VALUES ('farine','féculents','kg',1.5);

#7
INSERT INTO `projetpython`.`Produit` (`nom`,`categorie`,`unite`,`prix`) 
VALUES ('conserve de poissons','viandes/poissons/oeuf',' ',1.1);

#8
INSERT INTO `projetpython`.`Produit` (`nom`,`categorie`,`unite`,`prix`) 
VALUES ('sel','sucres/sales','kg',1.1);

#9
INSERT INTO `projetpython`.`Produit` (`nom`,`categorie`,`unite`,`prix`) 
VALUES ('eau','boisson','l',1.1);

#10
INSERT INTO `projetpython`.`Produit` (`nom`,`categorie`,`unite`,`prix`) 
VALUES ('huile','matieres grasses','kg',1.6);

#11
INSERT INTO `projetpython`.`Produit` (`nom`,`categorie`,`unite`,`prix`) 
VALUES ('mouchoirs','hygiene',' ',0.3);

#12
INSERT INTO `projetpython`.`Produit` (`nom`,`categorie`,`unite`,`prix`) 
VALUES ('savon','hygiene',' ',1.2);

#13
INSERT INTO `projetpython`.`Produit` (`nom`,`categorie`,`unite`,`prix`) 
VALUES ('oeuf','viande/poisson/oeuf','cg',1.3);

#14
INSERT INTO `projetpython`.`Produit` (`nom`,`categorie`,`unite`,`prix`) 
VALUES ('gants','hygiene',' ',1.1);

#15
INSERT INTO `projetpython`.`Produit` (`nom`,`categorie`,`unite`,`prix`) 
VALUES ('gel hydro','hygiene',' ',1);

#16
INSERT INTO `projetpython`.`Produit` (`nom`,`categorie`,`unite`,`prix`) 
VALUES ('Papier toilette','hygiene','cg',1.5);

#17
INSERT INTO `projetpython`.`Produit` (`nom`,`categorie`,`unite`,`prix`) 
VALUES ('Lait','Boissons','l',1.1);

#18
INSERT INTO `projetpython`.`Produit` (`nom`,`categorie`,`unite`,`prix`) 
VALUES ('Pain','feculents','cg',1.1);

#19
INSERT INTO `projetpython`.`Produit` (`nom`,`categorie`,`unite`,`prix`) 
VALUES ('viande','viande/poisson/oeuf','kg',1.1);

#20
INSERT INTO `projetpython`.`Produit` (`nom`,`categorie`,`unite`,`prix`) 
VALUES ('Blé','féculent','kg',1.6);