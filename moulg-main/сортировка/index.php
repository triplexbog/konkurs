<!DOCTYPE html>
<html>
<head>
    <title>Сортировка букв</title>
</head>
<body>
    <h2>Введите строку для сортировки букв</h2>
    <form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>">
        Строка: <input type="text" name="input_string">
        <input type="submit" value="Сортировать">
    </form>

    <?php
    // Функция для сортировки букв в строке
    function sortString($str) {
        $chars = str_split($str); // Разбиваем строку на массив символов
        sort($chars); // Сортируем массив символов
        return implode('', $chars); // Объединяем символы обратно в строку
    }

    // Обработка данных формы
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $inputString = $_POST["input_string"];
        $sortedString = sortString($inputString);
        echo "<p>Отсортированная строка: " . htmlspecialchars($sortedString) . "</p>";
    }
    ?>
</body>
</html>
