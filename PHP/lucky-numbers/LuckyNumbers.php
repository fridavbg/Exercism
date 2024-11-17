<?php

class LuckyNumbers {
    public function sumUp(array $digitsOfNumber1, array $digitsOfNumber2): int {
        $num1 = (int)implode('', $digitsOfNumber1);
        $num2 = (int)implode('', $digitsOfNumber2);
        return $num1 + $num2;
    }

    public function isPalindrome(int $number): bool {
        return strval($number) === strrev(strval($number));
    }

    public function validate(string $input): string {
        $num = (int)$input;
        if ($input === '') {
            return 'Required field';
        } elseif ($num <= 0) {
            return 'Must be a whole number larger than 0';
        } else {
            return '';
        }
    }
}
