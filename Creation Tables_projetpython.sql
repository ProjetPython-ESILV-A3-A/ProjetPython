use `projetpython`;

create table `projetpython`.`Demandeur`(
`id` int not null auto_increment,
`nom` varchar(25) not null,
`email` varchar (35) not null,
`mdp` varchar(15) not null,
`telephone` varchar(10) not null,
`nbprochesfoyer` int not null,
`nomsproches` varchar(150) not null,
`adresse` varchar(60) not null,
`argent` double not null,
primary key (`id`));

create table `projetpython`.`Admin`(
`id` int not null auto_increment,
`nom` varchar(25) not null,
`email` varchar(35) not null,
`mdp` varchar(15) not null,
primary key (`id`));

create table `projetpython`.`Produit`(
`id` int not null auto_increment,
`nom` varchar(25) not null,
`categorie` varchar(25) not null,
`unite` varchar(5) not null,
`stock` int not null,
`prix` double not null, 
primary key (`id`));

create table `projetpython`.`Entreprise`(
`nom` varchar(25) not null,
`argent` double not null );