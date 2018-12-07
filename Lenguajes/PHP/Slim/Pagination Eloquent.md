#### Utilizar Pagination de Eloquent en Slim Framwork

Para usar primero instalar Eloquent
```sh
composer require illuminate/database
```

Instalar Pagination
```sh
composer require illuminate/pagination
```

El Paginator necesita como resolver la página actual. En la configuración de las dependencias
```php
// $container is application's DIC container.
// Setup Paginator resolvers
Illuminate\Pagination\Paginator::currentPageResolver(function ($pageName = 'page') use ($container) {

    $page = $container->request->getParam($pageName);

    if (filter_var($page, FILTER_VALIDATE_INT) !== false && (int) $page >= 1) {
        return $page;
    }
    return 1;
});
```

En las plantillas twig, luego se pueden generar los enlaces de paginación sin escapar el contenido HTML.
```twig
{{ items.links | raw }}
```
