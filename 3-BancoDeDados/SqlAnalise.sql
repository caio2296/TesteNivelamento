/*Quais as 10 operadoras com maiores despesas em "EVENTOS/ SINISTROS CONHECIDOS OU 
AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR" no último trimestre? */ 
SELECT 
    es.registro_ans,
    es.razao_social,
    SUM(c.vl_saldo_final) AS total_despesa
FROM 
    contabilidade c
JOIN 
    empresas_saude es ON c.reg_ans = es.registro_ans
WHERE 
    c.data >= DATE_SUB((SELECT MAX(data) FROM contabilidade), INTERVAL 3 MONTH)
GROUP BY 
    es.registro_ans, es.razao_social
HAVING 
    total_despesa > 0
ORDER BY 
    total_despesa DESC
LIMIT 10;


/*Quais as 10 operadoras com maiores despesas nessa categoria no último ano?*/
SELECT 
    es.registro_ans,
    es.razao_social,
    SUM(c.vl_saldo_final) AS total_despesa
FROM 
    contabilidade c
JOIN 
    empresas_saude es ON c.reg_ans = es.registro_ans
WHERE 
    c.data >= CURDATE() - INTERVAL 1 YEAR
GROUP BY 
    es.registro_ans, es.razao_social
ORDER BY 
    total_despesa DESC
LIMIT 10;

 

