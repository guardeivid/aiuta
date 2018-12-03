#### Como utilizar PostGIS con Laravel

###### Con Eloquent
```php
Trail::create([
    'name' => 'test',
    'description' => 'test',
    'user_id' => 1,
    'location' => 1,
    'source_file' => 'uploads/myfile',
    'geom' => \DB::raw("public.ST_GeomFromText('$wkt'::text, 4326)")
]);

```

###### Con Fluent

```php
$last_id = DB::table('table.geom')->insertGetId(
    [
      'geom' => \DB::raw("ST_GeomFromText('$data->geom', 4326)"),
      'id_layer' => $data->id_layer,
      'object_type' => $data->object_type
    ]
  );
```