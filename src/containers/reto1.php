<?php
function anagram($palabra1, $palabra2)
    {
        if (count_chars($palabra1) == count_chars($palabra2))
            return "True";
        else 
            return "False";       
    }
  
    print(anagram('roto', 'toro'));
    print(anagram('loco', 'colo'));
?>