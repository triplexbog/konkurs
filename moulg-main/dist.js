function calculateDistance(x1, y1, x2, y2) {
    const deltaX = x2 - x1;
    const deltaY = y2 - y1;
    const distance = Math.sqrt(deltaX * deltaX + deltaY * deltaY);
    return distance;
}

// Пример использования функции
const distance = calculateDistance(0, 0, 6, 6);
console.log("Расстояние между точками: " + distance);

