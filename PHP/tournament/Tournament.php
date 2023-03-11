<?php

/*
 * By adding type hints and enabling strict type checking, code can become
 * easier to read, self-documenting and reduce the number of potential bugs.
 * By default, type declarations are non-strict, which means they will attempt
 * to change the original type to match the type specified by the
 * type-declaration.
 *
 * In other words, if you pass a string to a function requiring a float,
 * it will attempt to convert the string value to a float.
 *
 * To enable strict mode, a single declare directive must be placed at the top
 * of the file.
 * This means that the strictness of typing is configured on a per-file basis.
 * This directive not only affects the type declarations of parameters, but also
 * a function's return type.
 *
 * For more info review the Concept on strict type checking in the PHP track
 * <link>.
 *
 * To disable strict typing, comment out the directive below.
 */

declare(strict_types=1);

class Team
{
    public $name;
    public $matches_played;
    public $win;
    public $loss;
    public $draw;

    public function __construct($name)
    {
        $this->name = $name;
        $this->matches_played = 0;
        $this->win = 0;
        $this->loss = 0;
        $this->draw = 0;
    }

    public function points(): int
    {
        return ($this->win * 3) + $this->draw;
    }

    function matchWon()
    {
        $this->win++;
        $this->matches_played++;
    }

    function matchLost()
    {
        $this->loss++;
        $this->matches_played++;
    }

    function matchTied()
    {
        $this->draw++;
        $this->matches_played++;
    }
}



class Tournament
{
    private $teams;

    public function __construct()
    {
        $this->teams = [];
    }

    function createTeam($name): object
    {
        if (!isset($this->teams[$name])) {
            $this->teams[$name] = new Team($name);
        }
        return $this->teams[$name];
    }

    function createHeader(): string
    {
        return 'Team                           | MP |  W |  D |  L |  P';
    }

    function listTeam($team): string
    {
        return "\n" . str_pad($team->name, 31) . "|  " . str_pad((string) $team->matches_played, 2) . "|  " . str_pad((string) $team->win, 2) . "|  " . str_pad((string) $team->draw, 2) . "|  " . str_pad((string) $team->loss, 2) . "|  " . str_pad((string) $team->points(), 1);
    }

    function calculateScores($input)
    {
        $scores = explode("\n", $input);
        foreach ($scores as $score) {
            if ($score == null) {
                continue;
            }
            $match = explode(';', $score);
            $team1 = $this->createTeam($match[0]);
            $team2 = $this->createTeam($match[1]);
            $matchResult = $match[2];
            switch ($matchResult) {
                case 'win':
                    $team1->matchWon();
                    $team2->matchLost();
                    break;
                case 'draw':
                    $team1->matchTied();
                    $team2->matchTied();
                    break;
                case 'loss':
                    $team1->matchLost();
                    $team2->matchWon();
                    break;
            };
            uasort($this->teams, function ($a, $b) {
                if ($a->points() === $b->points()) {
                    return $a->name > $b->name ? 1 : 0;
                }
                return $a->points() < $b->points() ? 1 : -1;
            });
        }
        return $this->teams;
    }

    function tally($scores): string
    {
        $table = $this->createHeader();
        if (strlen($scores) > 0) {
            $this->calculateScores($scores);
        }
        foreach ($this->teams as $team) {
            $table .= $this->listTeam($team);
        }
        return $table;
    }
}

$tournament = new Tournament();
$scores =
    "Allegoric Alaskans;Blithering Badgers;loss\n" .
    "Allegoric Alaskans;Blithering Badgers;win";
var_dump($tournament->tally($scores));
