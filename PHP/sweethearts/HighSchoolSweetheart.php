<?php

class HighSchoolSweetheart
{
    public function firstLetter(string $name): string
    {
        $name = trim($name);
        return $name[0];
    }

    public function initial(string $name): string
    {
        $initial = strtoupper($this->firstLetter($name));
        return $initial . '.';
    }

    public function initials(string $name): string
    {
        $parts = explode(' ', $name);
        $firstNameLetter = $this->initial($parts[0][0]);
        $lastNameLetter = $this->initial($parts[1][0]);

        return  $firstNameLetter . ' ' . $lastNameLetter;;
    }

    public function pair(string $sweetheart_a, string $sweetheart_b): string
    {
        $initials_a = $this->initials($sweetheart_a);
        $initials_b = $this->initials($sweetheart_b);
        $pair = $initials_a . ' + ' . $initials_b;
        $pair = "     ******       ******\n"
            . "   **      **   **      **\n"
            . " **         ** **         **\n"
            . "**            *            **\n"
            . "**                         **\n"
            . "**     $initials_a  +  $initials_b     **\n"
            . " **                       **\n"
            . "   **                   **\n"
            . "     **               **\n"
            . "       **           **\n"
            . "         **       **\n"
            . "           **   **\n"
            . "             ***\n"
            . "              *";

        return $pair;
    }
}

$highschool_sweetheart = new HighSchoolSweetheart();

$highschool_sweetheart->pair('Avery Bryant', 'Charlie Dixon');
