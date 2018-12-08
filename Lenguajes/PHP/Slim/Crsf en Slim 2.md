### Crsf en Slim Framework 2 con Middleware

```
--Proyecto
  |--app
    |--views
        form.twig
    |--middleware
        CrsfMiddleware.php
    routes.php
  start.php
```

CrsfMiddleware.php
```php
<?php

namespace App\Middleare;

class CrsfMiddleware extends \Slim\Middlesware
{
    protected $key = ''crsf_token;
    
    public function call()
    {
        $this->app->hook('slim.before', [$this, 'check']);
        $this->next->call();
    }
    
    public function check()
    {
        if (!isset($_SESSION[$this->key])) {
            $_SESSION[$this->key] = sha1(microtime(true) . rand(10000, 99999));
        }
        
        $token = $_SESSION[$this->key];
        
        if (in_aaray($this->app->request()->getMethod(), ['POST', 'PUT', 'DELETE' ])) {
            $submittedToken = $this->app->request()->post($this->key);
            
            if ($token != $submittedToken) {
                throw new \Exception('CSRF token mismatch');
            }
        }
        
        $this->app->view()->appenData([
            'crsf_key' => $this->key,
            'crsf_token' => $token,
        ]);
    }
}
```

start.php
```php
<?php

session_start();

require '../vendor/autoload.php';

$app = new \Slim\Slim([
    'view' => new \Slim\Views\Twig()
]);

$app->add(new App\Middleware\CsrfMiddleware);

$view = $app->view();
$view->setTemplatesDirectory('app/views');
$view->parserExtension = [
    new \Slim\Views\TwigExtension(),
];

require 'app/routes.php';
```

form.twig
```html
<form>
    <input type="text" name="a" />
    <input type="hidden" name="" value="{{ cresf_key }}" value="{{ crsf_token}}" />
    <input type="submit" value="Enviar" />
</form>
```
