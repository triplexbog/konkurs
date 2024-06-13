<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Список заказанных книг</title>
</head>
<body>
    <h2>Список заказанных книг</h2>

    <?php
    // Подключение к базе данных
    $servername = "localhost";
    $username = "username";
    $password = "password";
    $dbname = "mydatabase";

    $conn = new mysqli($servername, $username, $password, $dbname);

    // Проверка соединения
    if ($conn->connect_error) {
        die("Ошибка подключения: " . $conn->connect_error);
    }

    // SQL-запрос для получения списка заказанных книг
    $sql = "SELECT orders.order_id, orders.order_time, users.user_id, users.username, books.book_id, books.title
            FROM orders
            INNER JOIN users ON orders.user_id = users.user_id
            INNER JOIN ordered_books ON orders.order_id = ordered_books.order_id
            INNER JOIN books ON ordered_books.book_id = books.book_id";

    $result = $conn->query($sql);

    if ($result->num_rows > 0) {
        // Выводим данные в виде таблицы HTML
        echo "<table border='1'>
                <tr>
                    <th>Идентификатор заказа</th>
                    <th>Время заказа</th>
                    <th>Идентификатор пользователя</th>
                    <th>Имя пользователя</th>
                    <th>Идентификатор книги</th>
                    <th>Название книги</th>
                </tr>";
        // Выводим каждую строку результата запроса
        while($row = $result->fetch_assoc()) {
            echo "<tr>
                    <td>" . $row["order_id"] . "</td>
                    <td>" . $row["order_time"] . "</td>
                    <td>" . $row["user_id"] . "</td>
                    <td>" . $row["username"] . "</td>
                    <td>" . $row["book_id"] . "</td>
                    <td>" . $row["title"] . "</td>
                </tr>";
        }
        echo "</table>";
    } else {
        echo "Нет результатов";
    }
    $conn->close();
    ?>
</body>
</html>
