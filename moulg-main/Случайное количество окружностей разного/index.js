document.addEventListener("DOMContentLoaded", function() {
    var circles = []; // Массив для хранения окружностей
    var numCircles = 10; // Количество окружностей

    // Создание и инициализация окружностей
    for (var i = 0; i < numCircles; i++) {
        createCircle();
    }

    // Функция для создания новой окружности
    function createCircle() {
        var circle = document.createElement("div");
        circle.classList.add("circle");
        circle.style.width = circle.style.height = (Math.random() * 50 + 10) + "px"; // Случайный размер окружности
        circle.style.top = Math.random() * (window.innerHeight - parseInt(circle.style.height)) + "px"; // Случайное вертикальное положение
        circle.style.left = Math.random() * (window.innerWidth - parseInt(circle.style.width)) + "px"; // Случайное горизонтальное положение
        document.body.appendChild(circle);
        circles.push(circle);
    }

    // Обработчик события перемещения мыши
    document.addEventListener("mousemove", function(event) {
        var mouseX = event.clientX;
        var mouseY = event.clientY;

        // Проверка коллизии с курсором мыши и отталкивание от него
        circles.forEach(function(circle) {
            var circleRect = circle.getBoundingClientRect();
            var circleCenterX = circleRect.left + circleRect.width / 2;
            var circleCenterY = circleRect.top + circleRect.height / 2;
            var dx = circleCenterX - mouseX;
            var dy = circleCenterY - mouseY;
            var distance = Math.sqrt(dx * dx + dy * dy);
            var minDistance = circleRect.width / 2 + 10; // Дистанция отталкивания

            if (distance < minDistance) {
                var angle = Math.atan2(dy, dx);
                var newX = circleCenterX + Math.cos(angle) * minDistance;
                var newY = circleCenterY + Math.sin(angle) * minDistance;
                circle.style.left = newX - circleRect.width / 2 + "px";
                circle.style.top = newY - circleRect.height / 2 + "px";
            }
        });
    });

    // Функция для обновления положения окружностей
    function moveCircles() {
        circles.forEach(function(circle) {
            var circleRect = circle.getBoundingClientRect();
            var dx = Math.random() * 4 - 2; // Случайное изменение положения по горизонтали
            var dy = Math.random() * 4 - 2; // Случайное изменение положения по вертикали
            var newX = circleRect.left + dx;
            var newY = circleRect.top + dy;

            // Проверка на столкновение с границами экрана
            if (newX < 0) newX = 0;
            if (newY < 0) newY = 0;
            if (newX + circleRect.width > window.innerWidth) newX = window.innerWidth - circleRect.width;
            if (newY + circleRect.height > window.innerHeight) newY = window.innerHeight - circleRect.height;

            circle.style.left = newX + "px";
            circle.style.top = newY + "px";
        });

        requestAnimationFrame(moveCircles);
    }

    // Запуск анимации
    moveCircles();
});
