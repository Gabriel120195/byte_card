CREATE DATABASE bytecard;

use bytecard;

CREATE TABLE `cartoes` (
`id` bigint unsigned NOT NULL AUTO_INCREMENT,
`numero` varchar(30) NOT NULL,
`cvv` varchar(3) NOT NULL,
`limite` double(15,2) NOT NULL,
`validade` date NOT NULL,
`cliente` varchar(255) NOT NULL,
`status` varchar(100) NOT NULL,
PRIMARY KEY (`id`)
);


CREATE TABLE `compras` (
`id` bigint unsigned NOT NULL AUTO_INCREMENT,
`valor` double(15,2) NOT NULL,
`data` datetime NOT NULL,
`estabelecimento` varchar(1000) NOT NULL,
`categoria` varchar(255) NOT NULL,
`cartao_id` bigint unsigned NOT NULL,
PRIMARY KEY (`id`),
KEY `cartao_fk` (`cartao_id`),
CONSTRAINT `cartao_fk` FOREIGN KEY (`cartao_id`)
REFERENCES `cartoes` (`id`)
);

INSERT INTO cartoes (numero, cvv, limite, validade, cliente, status)
VALUES ('8888 2222 3333 4444', '564', 9999, '2023-08-26', 'Gal Costa', 'ATIVO');
INSERT INTO cartoes (numero, cvv, limite, validade, cliente, status)
VALUES ('7777 2222 3333 4444', '564', 6750, '2022-10-08', 'Luiz Gonzaga','INATIVO');
INSERT INTO cartoes (numero, cvv, limite, validade, cliente, status)
VALUES ('5555 6666 3333 4444', '014', 22500, '2025-10-14', 'Pixinguinha','ATIVO');
INSERT INTO cartoes (numero, cvv, limite, validade, cliente, status)
VALUES ('5555 2222 3333 4444', '312', 5000, '2024-10-16', 'Tom Jobim', 'ATIVO');
INSERT INTO cartoes (numero, cvv, limite, validade, cliente, status)
VALUES ('1111 2222 3333 4444', '564', 10000, '2024-10-01', 'Elis Regina','ATIVO');

SELECT * FROM cartoes WHERE validade < '2023-10-01';

UPDATE bytecard.cartoes t SET t.status = 'INATIVO' WHERE t.id = 1;

INSERT INTO compras (valor, data, estabelecimento, categoria, cartao_id)
VALUES (100, '2023-09-15 09:42:03', 'Padaria', 'Alimentação', 1);
INSERT INTO compras (valor, data, estabelecimento, categoria, cartao_id)
VALUES (500, '2023-06-18 17:42:03', 'Salão de Beleza Belezura', 'Serviços', 1);
INSERT INTO compras (valor, data, estabelecimento, categoria, cartao_id)
VALUES (1010.78, '2023-08-11 17:42:03', 'Mario & Luigi Ltda', 'Serviços', 1);
INSERT INTO compras (valor, data, estabelecimento, categoria, cartao_id)
VALUES (3723.32, '2023-09-13 18:42:03', 'Bossa Instrumentos', 'Serviços', 2);

SELECT * FROM compras WHERE valor > 1000;

SELECT * FROM compras WHERE valor > 1000 AND categoria = 'Serviços' AND data BETWEEN '2023-08-01' AND '2023-10-01'