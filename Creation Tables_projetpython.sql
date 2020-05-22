use `projetpython`;

drop table if exists SousCommande;
drop table if exists Commande;
drop table if exists Demandeur;
drop table if exists Admin;
drop table if exists produit;


create table `projetpython`.`Demandeur`(
`id` int not null auto_increment,
`nom` varchar(25) not null,
`email` varchar (35) not null,
`mdp` varchar(40) not null,
`telephone` varchar(10) not null,
`nbprochesfoyer` int not null,
`nomsproches` varchar(150) not null,
`adresse` varchar(60) not null,
primary key (`id`));

create table `projetpython`.`Admin`(
`id` int not null auto_increment,
`nom` varchar(25) not null,
`email` varchar(35) not null,
`mdp` varchar(40) not null,
primary key (`id`));

create table `projetpython`.`Produit`(
`id` int not null auto_increment,
`nom` varchar(25) not null,
`categorie` varchar(25) not null,
`unite` varchar(5) not null,
`prix` double not null, 
primary key (`id`));

CREATE TABLE `projetpython`.`Commande`(
`id` int not null auto_increment,
`idDemandeur` int not null,
`dateCommande` datetime not null,
foreign key(idDemandeur)
references Demandeur(id),
primary key (`id`));

create table `projetpython`.`SousCommande`(
`id` int not null auto_increment,
`idCommande` int not null,
`idProduit` int not null,
`quantiteDemandee`int not null,
foreign key(idCommande)
references Commande(id),
foreign key(idProduit)
references Produit(id),
primary key (`id`));