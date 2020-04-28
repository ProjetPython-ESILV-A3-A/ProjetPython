use `projetpython`;

#Demandeur
INSERT INTO `projetpython`.`Demandeur` (`nom`,`email`,`mdp`,`telephone`,`nbprochesfoyer`,`nomsproches`,`adresse`,`argent`)
VALUES ('Jean','jean@gmail.com','jean123','0645879865',2,'sophie;emma','3 rue du Collysée',50);

INSERT INTO `projetpython`.`Demandeur` (`nom`,`email`,`mdp`,`telephone`,`nbprochesfoyer`,`nomsproches`,`adresse`,`argent`)
VALUES ('Lilia','lilia@gmail.com','lila0','0685859865',2,'benoit;emile','10 rue de laPlace',60);

#Admin
INSERT INTO `projetpython`.`Admin` (`nom`,`email`,`mdp`) VALUES ('Equipe4','equipe4@gmail.com','20/20');

#Produits
#1
INSERT INTO `projetpython`.`Produit` (`nom`,`categorie`,`unite`,`stock`,`prix`) 
VALUES ('sucre','sucres/sales','kg',10000,1);

#2
INSERT INTO `projetpython`.`Produit` (`nom`,`categorie`,`unite`,`stock`,`prix`) 
VALUES ('pates','féculents','kg',10000,1.2);

#3
INSERT INTO `projetpython`.`Produit` (`nom`,`categorie`,`unite`,`stock`,`prix`) 
VALUES ('riz','féculents','kg',10000,1.3);

#4
INSERT INTO `projetpython`.`Produit` (`nom`,`categorie`,`unite`,`stock`,`prix`) 
VALUES ('semoule','féculents','kg',10000,1.1);

#5
INSERT INTO `projetpython`.`Produit` (`nom`,`categorie`,`unite`,`stock`,`prix`) 
VALUES ('légumes secs','fruits et légumes','kg',10000,1);

#6
INSERT INTO `projetpython`.`Produit` (`nom`,`categorie`,`unite`,`stock`,`prix`) 
VALUES ('farine','féculents','kg',10000,1.5);

#7
INSERT INTO `projetpython`.`Produit` (`nom`,`categorie`,`unite`,`stock`,`prix`) 
VALUES ('conserve de poissons','viandes/poissons/oeuf',' ',10000,1.1);

#8
INSERT INTO `projetpython`.`Produit` (`nom`,`categorie`,`unite`,`stock`,`prix`) 
VALUES ('sel','sucres/sales','kg',10000,1.1);

#9
INSERT INTO `projetpython`.`Produit` (`nom`,`categorie`,`unite`,`stock`,`prix`) 
VALUES ('eau','boisson','l',10000,1.1);

#10
INSERT INTO `projetpython`.`Produit` (`nom`,`categorie`,`unite`,`stock`,`prix`) 
VALUES ('huile','matieres grasses','kg',10000,1.6);

#11
INSERT INTO `projetpython`.`Produit` (`nom`,`categorie`,`unite`,`stock`,`prix`) 
VALUES ('mouchoirs','hygiene',' ',10000,0.3);

#12
INSERT INTO `projetpython`.`Produit` (`nom`,`categorie`,`unite`,`stock`,`prix`) 
VALUES ('savon','hygiene',' ',10000,1.2);

#13
INSERT INTO `projetpython`.`Produit` (`nom`,`categorie`,`unite`,`stock`,`prix`) 
VALUES ('oeuf','viande/poisson/oeuf','cg',10000,1.3);

#14
INSERT INTO `projetpython`.`Produit` (`nom`,`categorie`,`unite`,`stock`,`prix`) 
VALUES ('gants','hygiene',' ',10000,1.1);

#15
INSERT INTO `projetpython`.`Produit` (`nom`,`categorie`,`unite`,`stock`,`prix`) 
VALUES ('gel hydro','hygiene',' ',10000,1);

#16
INSERT INTO `projetpython`.`Produit` (`nom`,`categorie`,`unite`,`stock`,`prix`) 
VALUES ('Papier toilette','hygiene','cg',10000,1.5);

#17
INSERT INTO `projetpython`.`Produit` (`nom`,`categorie`,`unite`,`stock`,`prix`) 
VALUES ('Lait','Boissons','l',10000,1.1);

#18
INSERT INTO `projetpython`.`Produit` (`nom`,`categorie`,`unite`,`stock`,`prix`) 
VALUES ('Pain','feculents','cg',10000,1.1);

#19
INSERT INTO `projetpython`.`Produit` (`nom`,`categorie`,`unite`,`stock`,`prix`) 
VALUES ('viande','viande/poisson/oeuf','kg',10000,1.1);

#20
INSERT INTO `projetpython`.`Produit` (`nom`,`categorie`,`unite`,`stock`,`prix`) 
VALUES ('Blé','féculent','kg',10000,1.6);

#Entreprise
INSERT INTO `projetpython`.`Entreprise` (`nom`,`argent`) VALUES ('Groupe4',1000);