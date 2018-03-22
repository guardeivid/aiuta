### Crosstab

Activar funciones
```sh
CREATE extension tablefunc;
```

```sql
SELECT left(fecha, 4)::int as anio, right(fecha, 2)::int as dia, ene, feb, mar, abr, may, jun, jul, ago, sep, oct, nov, dic FROM (
	SELECT * FROM crosstab(
		'SELECT g.fecha, g.mes::int, e.cota FROM
			(SELECT extract(year from dd) || ''-'' || LPAD(extract(day from dd)::text, 2, ''0'') fecha, extract(month from dd) mes FROM 
			generate_series( ''' inicio '''::timestamp, ''' fin '''::timestamp, ''1 day''::interval) dd) g
		LEFT JOIN
			(SELECT extract(year from fecha) || ''-'' || LPAD(extract(day from fecha)::text, 2, ''0'') fecha, extract(month from fecha) mes, cota 
			FROM hidro.escalas WHERE estacion = ' estacion ') e
		ON g.fecha = e.fecha AND g.mes = e.mes
		GROUP BY 1, 2, 3 ORDER BY 1, 2',
		'SELECT * FROM generate_series(1, 12)'
	) AS (fecha text, ene numeric, feb numeric, mar numeric, abr numeric, may numeric, jun numeric, jul numeric, ago numeric, sep numeric, oct numeric, nov numeric, dic numeric)
) a;
```
