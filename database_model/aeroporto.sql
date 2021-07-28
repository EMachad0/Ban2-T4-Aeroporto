-- create database aeroporto;

create table funcionario
(
    id_fun      serial,
    n_matricula int not null,
    n_membro    int not null,
    primary key (id_fun)
);

create table controlador
(
    id_fun     int primary key,
    data_exame date,
    foreign key (id_fun) references funcionario
);

create table tecnico
(
    id_fun   int primary key,
    endereco varchar(50),
    telefone int,
    salario  float not null,
    foreign key (id_fun) references funcionario
);

create table modelo
(
    id_mod     serial primary key,
    cod        int,
    capacidade int,
    peso       int
);

create table pericia
(
    id_mod int,
    id_fun int,
    primary key (id_mod, id_fun),
    foreign key (id_mod) references modelo on delete cascade,
    foreign key (id_fun) references tecnico on delete cascade
);

create table aviao
(
    id_avi     serial primary key,
    id_mod     int,
    n_registro int not null,
    foreign key (id_mod) references modelo
);

create table tipo_teste
(
    id_tit           serial primary key,
    n_anac           int,
    nome             varchar(50) not null,
    pontuacao_maxima int         not null
);

create table teste
(
    id_tes       serial,
    id_avi       int,
    id_fun       int,
    id_tit       int,
    data_teste   date not null,
    horas_gastas int  not null,
    pontuacao    int  not null,
    primary key (id_tes),
    foreign key (id_avi) references aviao,
    foreign key (id_fun) references tecnico,
    foreign key (id_tit) references tipo_teste
);

create or replace function insert_controlador(n_mat int, n_mem int, data date,
                                              id int default nextval('funcionario_id_fun_seq')) returns void as
$$
begin
    insert into funcionario
    values (id, n_mat, n_mem)
    on conflict(id_fun) do update set n_matricula=n_mat, n_membro=n_mem;

    insert into controlador
    values (id, data)
    on conflict(id_fun) do update set data_exame=data;
end;
$$ language plpgsql;

create or replace function insert_tecnico(n_mat int, n_mem int, ende varchar(50), tel int, sal float,
                                          id int default nextval('funcionario_id_fun_seq')) returns void as
$$
begin
    insert into funcionario
    values (id, n_mat, n_mem)
    on conflict(id_fun) do update set n_matricula=n_mat, n_membro=n_mem;

    insert into tecnico
    values (id, ende, tel, sal)
    on conflict(id_fun) do update set endereco=ende, telefone=tel, salario=sal;
end;
$$ language plpgsql;

create or replace function tri_pericia() returns trigger as
$$
declare
    per int;
begin
    per := (select id_mod from pericia where id_fun = old.id_fun);
    if (select count(*) from pericia where id_mod = per) = 1 then
        raise 'Impossivel deletar o ultimo tecnico com esta pericia';
    end if;
    return old;
end;
$$ language plpgsql;

create trigger tri_pericia
    before delete
    on tecnico
    for each row
execute function tri_pericia();

create or replace function tri_score() returns trigger as
$$
declare
    max_score int;
begin
    max_score = (select pontuacao_maxima from tipo_teste where id_tit = new.id_tit);
    if (new.pontuacao < 0 or new.pontuacao > max_score) then
        raise 'Pontuacao invalida!';
    end if;
    return new;
end;
$$ language plpgsql;

create trigger tri_score
    before insert
    on teste
    for each row
execute function tri_score();

