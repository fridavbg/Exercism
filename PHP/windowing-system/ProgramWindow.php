<?php
require_once 'Size.php';
require_once 'Position.php';

class ProgramWindow
{
    public $x;
    public $y;
    public $width;
    public $height;

    public function __construct()
    {
        $this->x = 0;
        $this->y = 0;
        $this->width = 800;
        $this->height = 600;
    }

    public function resize(Size $size)
    {
        $this->width = $size->width;
        $this->height = $size->height;
    }

    public function move(Position $position) 
    {
        $this->x = $position->x;
        $this->y = $position->y;
    }
}

$window = new ProgramWindow();
$position = new Position(80, 313);
$window->move($position);
print($window->y);
print($window->x);