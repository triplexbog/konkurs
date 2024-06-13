<?php
// Путь к вашему изображению
$imagePath = 'main-background.webp';

// Загрузка изображения
$image = imagecreatefromwebp($imagePath);
if (!$image) {
    die('Не удалось загрузить изображение.');
}

// Создание нового изображения для фона
$backgroundWidth = 150;
$backgroundHeight = 200;
$background = imagecreatetruecolor($backgroundWidth, $backgroundHeight);
if (!$background) {
    die('Не удалось создать изображение для фона.');
}

// Загрузка изображения для фона (размер 150x200)
$backgroundImage = imagecreatefrompng('Screenshot_2.png'); // Или любой другой формат, поддерживаемый GD

// Определение размеров исходного изображения
$imageWidth = imagesx($image);
$imageHeight = imagesy($image);

// Определение размеров изображения для фона
$bgImageWidth = imagesx($backgroundImage);
$bgImageHeight = imagesy($backgroundImage);

// Масштабирование фона
imagecopyresampled($background, $backgroundImage, 0, 0, 0, 0, $backgroundWidth, $backgroundHeight, $bgImageWidth, $bgImageHeight);

// Повторение фона на всей площади исходного изображения
for ($x = 0; $x < $imageWidth; $x += $backgroundWidth) {
    for ($y = 0; $y < $imageHeight; $y += $backgroundHeight) {
        imagecopy($image, $background, $x, $y, 0, 0, $backgroundWidth, $backgroundHeight);
    }
}

// Вывод итогового изображения
header('Content-Type: image/jpeg');
imagejpeg($image);

// Освобождение памяти
imagedestroy($image);
imagedestroy($background);
?>
