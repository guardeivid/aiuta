<?php

namespace \Qualified\Name;

use \ADOConnection;

/**
 * summary
 */
class Name extends ExtendsName
{
    /**
     * summary
     */
    public function __construct()
    {
        $ado = new \ADOConnection();
        if ($ado) {
        	return true;
        } elsif($ado == false){
            return false;
        }
    }
}
