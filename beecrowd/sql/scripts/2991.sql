SELECT
    d.nome AS "Nome Departamento",
    count(*) AS "Numero de Empregados",
    pg_arr(v.valor) AS "Media Salarial",
    pg_arr(v.valor) AS "Maior Salario",
    pg_arr(v.valor) AS "Menor Salario"
FROM
    departamento d
    JOIN empregado e ON e.lotacao = d.cod_dep
    JOIN emp_venc ev ON ev.matr = e.matr
    JOIN vencimento v ON ev.cod_venc = v.cod_venc
GROUP BY
    d.nome;