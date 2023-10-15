DROP TABLE IF EXISTS compras;

DROP TABLE IF EXISTS cartoes;


CREATE TABLE IF NOT EXISTS `cartoes`(
`id` bigint unsigned NOT NULL AUTO_INCREMENT,
`numero` varchar(30) NOT NULL,
`cvv` varchar(3) NOT NULL,
`limite` double(15, 2) NOT NULL,
`validade` date NOT NULL,
`cliente` varchar(255) NOT NULL,
`status` varchar(100) NOT NULL,
PRIMARY KEY (`id`)
);


CREATE TABLE IF NOT EXISTS `compras`(
`id` bigint unsigned NOT NULL AUTO_INCREMENT,
`valor` double(15, 2) NOT NULL,
`data` datetime NOT NULL,
`estabelecimento` varchar(1000) NOT NULL,
`categoria` varchar(255) NOT NULL,
`cartao_id` bigint unsigned NOT NULL,
PRIMARY KEY (`id`),
KEY `cartao_fk` (`cartao_id`),
CONSTRAINT `cartao_fk` FOREIGN KEY (`cartao_id`) REFERENCES cartoes (`id`)
);


INSERT INTO cartoes (id, numero, cvv, limite, validade, cliente, status)
VALUES (1, '8888 2222 3333 4444', '564', 9999, '2023-08-26', 'Gal Costa', 'ATIVO');
INSERT INTO cartoes (id, numero, cvv, limite, validade, cliente, status)
VALUES (2, '7777 2222 3333 4444', '564', 6750, '2022-10-08', 'Luiz Gonzaga', 'INATIVO');
INSERT INTO cartoes (id, numero, cvv, limite, validade, cliente, status)
VALUES (3, '5555 6666 3333 4444', '014', 22500, '2025-10-14', 'Pixinguinha','ATIVO');
INSERT INTO cartoes (id, numero, cvv, limite, validade, cliente, status)
VALUES (4, '5555 2222 3333 4444', '312', 5000, '2024-10-16', 'Tom Jobim','ATIVO');
INSERT INTO cartoes (id, numero, cvv, limite, validade, cliente, status)
VALUES (5, '1111 2222 3333 4444', '564', 10000, '2024-10-01', 'Elis Regina','ATIVO');
INSERT INTO cartoes (id, numero, cvv, limite, validade, cliente, status)
VALUES (6, '3333 4444 5555 6666', '123', 12000, '2026-12-11', 'Leny Andrade','ATIVO');


INSERT INTO compras (id, valor, data, estabelecimento, categoria, cartao_id)
VALUES (1, 100, '2023-09-15 09:42:03', 'Padaria', 'Alimentação', 1);
INSERT INTO compras (id, valor, data, estabelecimento, categoria, cartao_id)
VALUES (2, 500, '2023-06-18 17:42:03', 'Salão de Beleza Belezura', 'Serviços', 1);
INSERT INTO compras (id, valor, data, estabelecimento, categoria, cartao_id)
VALUES (3, 1010.78, '2023-08-11 17:42:03', 'Mario & Luigi Ltda', 'Serviços', 1);
INSERT INTO compras (id, valor, data, estabelecimento, categoria, cartao_id)
VALUES (4, 3723.32, '2023-09-13 18:42:03', 'Bossa Instrumentos', 'Serviços', 2);
INSERT INTO compras (id, valor, data, estabelecimento, categoria, cartao_id)
VALUES (5, 3000, '2023-09-17 18:42:03', 'Hospital Música da Alma', 'Saúde', 6);
INSERT INTO compras (id, valor, data, estabelecimento, categoria, cartao_id)
VALUES (6, 400, '2023-07-09 09:19:19', 'Samba Laboatório', 'Saúde', 1);
INSERT INTO compras (id, valor, data, estabelecimento, categoria, cartao_id)
VALUES (7, 500, '2023-07-18 17:42:03', 'Salão de Beleza Belezura', 'Serviços', 1);
INSERT INTO compras (id, valor, data, estabelecimento, categoria, cartao_id)
VALUES (8, 800, '2023-09-09 09:23:16', 'Restaurante Água do Mar', 'Restaurantes', 2);


SELECT id, valor, estabelecimento, categoria 
FROM compras 
WHERE categoria IN ('Serviços', 'Saúde');


SELECT id, valor, estabelecimento, categoria
FROM compras
WHERE categoria IN ('Serviços', 'Saúde')
ORDER BY data DESC
LIMIT 4;


SELECT categoria, COUNT(*) AS quantidade
FROM compras
GROUP BY categoria;


SELECT categoria, SUM(valor) AS total
FROM compras
GROUP BY categoria
ORDER BY categoria;


SELECT c.cliente, SUM(cp.valor)
FROM compras cp JOIN cartoes c ON cp.cartao_id = c.id
GROUP BY c.id;