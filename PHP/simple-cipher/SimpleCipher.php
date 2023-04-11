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

class SimpleCipher
{
    public const LETTERS = "abcdefghijklmnopqrstuvwxyz";
    public string $key;
    public function __construct(string $key = null)
    {
        $key ??= $this -> generateKey();
        $this->validateKey($key);
        $this->key = $key;
    }

    public function encode(string $plainText): string
    {
        $result = "";
        for ($i=0; $i <= strlen($plainText) -1; $i++){
            $result .= $this->shift($plainText[$i], strpos(self::LETTERS,$this->key[$i]));
        }
        return $result;
    }

    public function decode(string $plainText): string
    {
        $result = "";
        for ($i=0; $i <= strlen($plainText) -1; $i++){
            $result .= $this->shift($plainText[$i], strpos(self::LETTERS,($this->key[$i])) * -1);
        }
        return $result;
    }

    private function validateKey(string $key){
        if (!ctype_lower($key)){
            throw new InValidArgumentException("Key contains no lower characters");
        }
    }

    private function shift($textChar, $keyPos) : string
    {
        return self::LETTERS[ (strpos(self::LETTERS, $textChar) + $keyPos) % 26];
    }

    private function generateKey(): string {
        $newKey = [];
        for ($i = 0 ; $i < 26; $i++){
            $newKey[]= self::LETTERS[random_int(0, 25)];
        }
        return implode('', $newKey);
    }
}