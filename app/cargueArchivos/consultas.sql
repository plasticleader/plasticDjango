SELECT 
	p.`portafolio_nombre`, i.`interaccionpersona_fechainteraccion`, per.persona_identificacion, per.`persona_nombre`, d.`tipointeraccion_descripcion`, i.nota 
FROM 
	data_interaccionpersona i 
	inner join data_personaportafoliotoken t on t.`personaportafoliotoken_token` = i.interaccionpersona_personaportafoliotoken 
	inner join data_portafolio p on p.`portafolio_id`=t.`personaportafoliotoken_portafolio` 
	inner join data_persona per on per.`persona_id`=t.`personaportafoliotoken_persona` 
	inner join data_tipointeraccion d on d.`tipointeraccion_id`=i.`interaccionpersona_tipointeraccion` 
WHERE 
	DATE(i.`interaccionpersona_fechainteraccion`) BETWEEN '2018-04-01' AND '2018-05-07' AND i.`interaccionpersonallamada` is null 


----- Imagenes Comprobantes
SELECT * FROM `data_comprabantepersona` WHERE `comprabantePersona_token` = 'Hhr5WcXQSpuWtz3o'

--  Consula de registros duplicados

SELECT `persona_identificacion`, COUNT(*) Total FROM `data_persona` GROUP BY `persona_identificacion` HAVING COUNT(*) > 1


--  Crezcamos


SELECT 
	per.persona_identificacion,`personaportafoliotoken_token` 
FROM 
	`data_personaportafoliotoken` 
	inner join data_persona per on per.`persona_id`=`personaportafoliotoken_persona` 
WHERE 
	`personaportafoliotoken_portafolio` = 7



--  Crezcamos Julio 

SELECT 
	per.persona_identificacion,`personaportafoliotoken_token` 
FROM 
	`data_personaportafoliotoken` 
	inner join data_persona per on per.`persona_id`=`personaportafoliotoken_persona` 
WHERE 
	`personaportafoliotoken_portafolio` = 21



---Movilidad Cundinamarca Junio


SELECT 
	per.persona_identificacion,`personaportafoliotoken_token` 
FROM 
	`data_personaportafoliotoken` 
	inner join data_persona per on per.`persona_id`=`personaportafoliotoken_persona` 
WHERE 
	`personaportafoliotoken_portafolio` = 20



-- Movilidad

SELECT 
	per.persona_identificacion,`personaportafoliotoken_token` 
FROM `data_personaportafoliotoken` 
	  inner join data_persona per on per.`persona_id`=`personaportafoliotoken_persona` 
WHERE `personaportafoliotoken_portafolio` = 3


-- Contactxentro

SELECT 
	per.persona_identificacion,`personaportafoliotoken_token` 
FROM `data_personaportafoliotoken` 
	  inner join data_persona per on per.`persona_id`=`personaportafoliotoken_persona` 
WHERE `personaportafoliotoken_portafolio` = 8


DELETE FROM `data_obligacionoferta` WHERE `obligacionoferta_obligacion` >= 54604



SELECT per.persona_identificacion,`personaportafoliotoken_token` FROM `data_personaportafoliotoken` inner join data_persona per on per.`persona_id`=`personaportafoliotoken_persona` WHERE `personaportafoliotoken_portafolio` = 6 and `personaportafoliotoken_estado` = 'A'	








INSERT INTO `tuacuerdo`.`data_tipointeraccion` (`tipointeraccion_descripcion`, `tipointeraccion_fechacreacion`, `tipointeraccion_id`, `tipointeraccion_orden`) VALUES ('Envio de comprobante de pago', '2018-05-18 00:00:00', '10115', '1');



--- Descargar comprobantes desde el servidor a local

scp intelibpo@tuacuerdo.com:/opt/intelbpo/tuacuerdo/static/upload/static/upload/(Nom-Imgen)  /ruta destino
