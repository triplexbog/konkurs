<!DOCTYPE html>
<html>
<head>
    <title>Поиск палиндрома</title>
</head>
<body>
    <form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>">
        Введите строку: <input type="text" name="input_string">
        <input type="submit" value="Найти палиндром">
    </form>

    <?php
    function longestPalindrome($s) {
        $n = strlen($s);
        $h = array_fill(0, $n, 0);
        $C = $R = 0; // центр и радиус или крайний правый палиндром
        $besti = $bestj = 0; // центр и радиус самого длинного палиндрома
        
        for ($i = 0; $i < $n; $i++) {
            if ($i < $C + $R) { // если есть пересечение
                $j = $h[$C - ($i - $C)]; // отражение
                if ($j < $C + $R - $i) { // случай A
                    $h[$i] = $j;
                    continue;
                } elseif ($j > $C + $R - $i) { // случай B
                    $h[$i] = $C + $R - $i;
                    continue;
                }
            } else { // если нет пересечения
                $j = 0;
            }
            
            while ($i - $j > 0 && $i + $j < $n - 1 && $s[$i - $j - 1] == $s[$i + $j + 1]) {
                $j++;
            }
            
            $h[$i] = $j;
            
            if ($j > $bestj) {
                $besti = $i;
                $bestj = $j;
            }
            
            if ($i + $j > $C + $R) {
                $C = $i;
                $R = $j;
            }
        }
        
        return substr($s, $besti - $bestj, 2 * $bestj + 1);
    }

    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $input_string = $_POST["input_string"];
        $longest_palindrome = longestPalindrome($input_string);
        echo "<p>Самый длинный палиндром: " . htmlspecialchars($longest_palindrome) . "</p>";
    }
    ?>
</body>
</html>