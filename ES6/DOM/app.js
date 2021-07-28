console.log('Here are the rectangle IDs')

const rW = document.getElementById('rectangleWrapper');
var rectangles = document.querySelectorAll('.rectangle');

for (const rec of rectangles) {
    console.log(rec.id);
}