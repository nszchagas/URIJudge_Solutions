DROP TABLE departamento;

DROP TABLE dependente;

DROP TABLE divisao;

DROP TABLE emp_desc;

DROP TABLE emp_venc;

DROP TABLE empregado;

DROP TABLE vencimento;

CREATE TABLE IF NOT EXISTS departamento (
    cod_dep integer,
    nome varchar (50),
    endereco varchar (50)
);

CREATE TABLE IF NOT EXISTS dependente (
    matr integer,
    nome varchar (50),
    endereco varchar (50)
);

CREATE TABLE IF NOT EXISTS desconto (
    cod_desc integer,
    nome varchar (50),
    tipo varchar (10),
    valor numeric
);

CREATE TABLE IF NOT EXISTS divisao (
    cod_divisao integer,
    nome varchar (50),
    endereco varchar (50),
    cod_dep numeric
);

CREATE TABLE IF NOT EXISTS emp_desc (cod_desc integer, matr integer);

CREATE TABLE IF NOT EXISTS emp_venc (cod_venc integer, matr integer);

CREATE TABLE IF NOT EXISTS empregado (
    matr integer,
    nome varchar (50),
    endereco varchar (50),
    data_lotacao timestamp,
    lotacao integer,
    gerencia_cod_dep integer,
    lotacao_div integer,
    gerencia_div integer
);

CREATE TABLE IF NOT EXISTS vencimento (
    cod_venc integer,
    nome varchar (50),
    tipo varchar (10),
    valor numeric
);

INSERT INTO
    departamento (cod_dep, nome, endereco)
VALUES
    (1, 'Contabilidade', 'R.X'),
    (2, 'TI', 'R.Y'),
    (3, 'Engenharia', 'R.Y');

INSERT INTO
    dependente(matr, nome, endereco)
VALUES
    (9999, 'Francisco Jose', 'R.Z'),
    (88, 'MARIA da Silva', 'R.T'),
    (55, 'Virgulino da Silva', 'R.31');

INSERT INTO
    desconto (cod_desc, nome, tipo, valor)
VALUES
    (91, 'IR', 'V', 400),
    (92, 'Plano de saude', 'V', 300),
    (93, NULL, NULL);

INSERT INTO
    divisao (cod_divisao, nome, endereco, cod_dep)
VALUES
    (11, 'Ativo', 'R.X', 1),
    (12, 'Passivo', 'R.X', 1),
    (
        21,
        'Desenvoilvimento de Projetos',
        'R.Y',
        2
    ),
    (22, 'Analise de Sistemas', ' R.Y', 2),
    (23, 'Programacao', 'R.W', 2),
    (31, 'Concreto', 'R.Y', 3),
    (32, 'Calculo Estrutural', 'R.Y', 3);

INSERT INTO
    emp_desc (cod_desc, matr)
VALUES
    (91, 3),
    (91, 27),
    (91, 9999),
    (92, 27),
    (92, 71),
    (92, 88),
    (92, 9999);

INSERT INTO
    emp_venc(cod_venc, matr)
VALUES
    (1, 27),
    (1, 88),
    (1, 135),
    (1, 254),
    (1, 431),
    (2, 1),
    (2, 5),
    (2, 7),
    (2, 13),
    (2, 33),
    (2, 9999),
    (3, 3),
    (3, 55),
    (3, 71),
    (3, 222),
    (4, 25),
    (4, 476),
    (5, 371),
    (6, 3),
    (6, 27),
    (6, 9999),
    (7, 5),
    (7, 33),
    (7, 55),
    (7, 71),
    (7, 88),
    (7, 254),
    (7, 476),
    (8, 25),
    (8, 91),
    (9, 1),
    (9, 27),
    (9, 91),
    (9, 135),
    (9, 371),
    (9, 9999),
    (10, 371),
    (10, 9999),
    (11, 91),
    (12, 3),
    (12, 27),
    (12, 254),
    (12, 9999),
    (13, 3),
    (13, 5),
    (13, 7),
    (13, 25),
    (13, 33),
    (13, 88),
    (13, 135);

INSERT INTO
    empregado (
        matr,
        nome,
        endereco,
        data_lotacao,
        lotacao,
        gerencia_cod_dep,
        lotacao_div,
        gerencia_div
    )
VALUES
    (
        9999,
        'Jose Sampaio',
        'R.Z',
        '2006-06-06T00:00:00Z',
        1,
        1,
        12,
        NULL
    ),
    (
        33,
        'Jose MARIA',
        'R.21',
        '2006-03-01T00:00:00Z',
        1,
        NULL,
        11,
        11
    ),
    (
        1,
        'MARIA Jose',
        'R.52',
        '2003-03-01T00:00:00Z',
        1,
        NULL,
        11,
        NULL
    ),
    (
        7,
        'Yasmim',
        'R.13',
        '2010-07-02T00:00:00Z',
        1,
        NULL,
        11,
        NULL
    ),
    (
        5,
        'Rebeca',
        'R.1',
        '2011-04-01T00:00:00Z',
        1,
        NULL,
        12,
        12
    ),
    (
        13,
        'Sofia',
        'R.28',
        '2010-09-09T00:00:00Z',
        1,
        NULL,
        12,
        NULL
    ),
    (
        27,
        'Andre',
        'R.Z',
        '2005-05-01T00:00:00Z',
        2,
        2,
        22,
        NULL
    ),
    (
        88,
        'Yami',
        'R.T',
        '2014-02-01T00:00:00Z',
        2,
        NULL,
        21,
        21
    ),
    (
        431,
        'Joao da Silva',
        'R.Y',
        '2011-07-03T00:00:00Z',
        2,
        NULL,
        21,
        NULL
    ),
    (
        135,
        'Ricardo Reis',
        'R.33',
        '2009-08-01T00:00:00Z',
        2,
        NULL,
        21,
        NULL
    ),
    (
        254,
        'Barbara',
        'R.Z',
        '2008-01-03T00:00:00Z',
        2,
        NULL,
        22,
        22
    ),
    (
        371,
        'Ines',
        'R.Y',
        '2005-01-01T00:00:00Z',
        2,
        NULL,
        22,
        NULL
    ),
    (
        476,
        'Flor',
        'R.Z',
        '2015-10-28T00:00:00Z',
        2,
        NULL,
        23,
        23
    ),
    (
        25,
        'Lina',
        'R.67',
        '2014-09-01T00:00:00Z',
        2,
        NULL,
        23,
        NULL
    ),
    (
        3,
        'Jose da Silva',
        'R.8',
        '2011-01-02T00:00:00Z',
        3,
        3,
        31,
        NULL
    ),
    (
        71,
        'Silverio dos Reis',
        'R.C',
        '2009-01-05T00:00:00Z',
        3,
        NULL,
        31,
        31
    ),
    (
        91,
        'Reis da Silva',
        'R.Z',
        '2011-11-05T00:00:00Z',
        3,
        NULL,
        31,
        NULL
    ),
    (
        55,
        'Lucas',
        'R.31',
        '2013-07-01T00:00:00Z',
        3,
        NULL,
        32,
        32
    ),
    (
        222,
        'Marina',
        'R.31',
        '2015-01-07T00:00:00Z',
        3,
        NULL,
        32,
        NULL
    ),
    (
        725,
        'Angelo',
        'R.X',
        '2001-03-01T00:00:00Z',
        2,
        NULL,
        21,
        NULL
    );