document.addEventListener("DOMContentLoaded", function() {
    var square = document.getElementById("square");

    // Обработчик события перемещения мыши
    document.addEventListener("mousemove", function(event) {
        // Положение курсора мыши
        var mouseX = event.clientX;

        // Ширина экрана
        var screenWidth = window.innerWidth;

        // Определяем, находится ли курсор мыши в левой или правой части экрана
        // Если курсор находится в левой части экрана, то цвет квадрата становится белым
        // Если курсор находится в правой части экрана, то цвет квадрата становится черным
        if (mouseX < screenWidth / 2) {
            square.style.backgroundColor = "white";
        } else {
            square.style.backgroundColor = "black";
        }
    });
});
