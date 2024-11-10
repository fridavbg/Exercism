<?php

class PizzaPi
{
    public function calculateDoughRequirement($numberOfPizzas, $numberOfPeople)
    {
        $grams = $numberOfPizzas * (($numberOfPeople * 20) + 200);
        return $grams;
    }

    public function calculateSauceRequirement($pizzas, $sauceCanVolume)
    {
        $saucePerPizza = 125;

        $cansOfSauce = $pizzas * $saucePerPizza / $sauceCanVolume;

        return $cansOfSauce;
    }

    public function calculateCheeseCubeCoverage($cheese_dimension, $thickness, $diameter)
    {
        $pizzas = pow($cheese_dimension, 3) / ($thickness * (M_PI * $diameter));
        return floor($pizzas);
    }

    public function calculateLeftOverSlices($pizzas, $friends)
    {
        $total_slices = ($pizzas * 8);
        $slices = $total_slices - ($friends * floor($total_slices / $friends));
        return $slices;
    }
}

