use mercado_libre;

create table productos
(
    id          int auto_increment,
    marca       varchar(500) null,
    referencia  varchar(500) null,
    modelo      varchar(500) null,
    memoria_int varchar(500) null,
    memoria_ram varchar(500) null,
    precio      varchar(500) null,
    pagina      decimal      null,
    constraint productos_id_uindex
        unique (id)
);

alter table productos
    add primary key (id);


