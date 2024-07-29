-- SQLite
SELECT e.nombre AS Nombre, p.nombre AS pais_nombre
FROM myapp_empleado e
JOIN myapp_pais p ON e.pais_id = p.idpais
WHERE e.pais_id = 1;