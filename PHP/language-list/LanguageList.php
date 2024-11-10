<?php

function language_list(...$languages) {
    return [...$languages];
}

function add_language($list, $language) {
    return [...$list, $language];
}

function add_to_language_list($list, $language) {
    $list[] = $language;
    return $list;
}

function prune_language_list($language_list) {
    $language_list = language_list(...$language_list);
    array_shift($language_list);
    return $language_list;
}

function current_language($language_list) {
    $language_list = language_list(...$language_list);
    return $language_list[0];
}

function language_list_length($language_list) {
    $language_list = language_list(...$language_list);
    return count($language_list);
}
