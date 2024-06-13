document.addEventListener("DOMContentLoaded", function() {
    const canvas = document.getElementById("myCanvas");
    const ctx = canvas.getContext("2d");
    const rect = canvas.getBoundingClientRect(); // Получаем размеры и позицию canvas

    // Устанавливаем размеры canvas равные размерам окна браузера
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;

    let isDrawing = false; // Переменная для отслеживания состояния рисования
    let lastX = 0;
    let lastY = 0;

    // Функция для начала рисования
    function startDrawing(event) {
        isDrawing = true;
        [lastX, lastY] = [event.clientX - rect.left, event.clientY - rect.top];
    }

    // Функция для завершения рисования
    function stopDrawing() {
        isDrawing = false;
    }

    // Функция для рисования линии
    function draw(event) {
        if (!isDrawing) return;
        const x = event.clientX - rect.left;
        const y = event.clientY - rect.top;

        ctx.beginPath();
        ctx.moveTo(lastX, lastY);
        ctx.lineTo(x, y);
        ctx.strokeStyle = "#000"; // Цвет линии
        ctx.lineWidth = 2; // Толщина линии
        ctx.stroke();

        [lastX, lastY] = [x, y];
    }

    // Обработчики событий для начала и окончания рисования
    canvas.addEventListener("mousedown", startDrawing);
    canvas.addEventListener("mouseup", stopDrawing);
    canvas.addEventListener("mouseout", stopDrawing);
    canvas.addEventListener("mousemove", draw);
});
