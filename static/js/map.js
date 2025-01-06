const sliderTrack = document.querySelector('.slider-track');
const slides = document.querySelectorAll('.slider-item');
const prevBtn = document.getElementById('prev');
const nextBtn = document.getElementById('next');

let currentIndex = 0;
const itemsPerView = 4; // Bir vaqtning o'zida ko'rsatiladigan elementlar soni
const totalSlides = slides.length;

// Slayderni cheksiz aylanish uchun tayyorlash
function cloneSlides() {
  for (let i = 0; i < itemsPerView; i++) {
    const firstClone = slides[i].cloneNode(true);
    const lastClone = slides[totalSlides - 1 - i].cloneNode(true);
    sliderTrack.appendChild(firstClone);
    sliderTrack.insertBefore(lastClone, sliderTrack.firstChild);
  }
}

cloneSlides();

const slideWidth = 100 / itemsPerView;
sliderTrack.style.transform = `translateX(-${slideWidth * itemsPerView}%)`; // Boshlang'ich pozitsiya

function updateSlider() {
  sliderTrack.style.transition = 'transform 0.5s ease-in-out';
  sliderTrack.style.transform = `translateX(-${slideWidth * (currentIndex + itemsPerView)}%)`;
}

function showNextSlide() {
  currentIndex++;
  updateSlider();

  if (currentIndex >= totalSlides) {
    setTimeout(() => {
      sliderTrack.style.transition = 'none';
      currentIndex = 0;
      sliderTrack.style.transform = `translateX(-${slideWidth * itemsPerView}%)`;
    }, 500);
  }
}

function showPrevSlide() {
  currentIndex--;
  updateSlider();

  if (currentIndex < 0) {
    setTimeout(() => {
      sliderTrack.style.transition = 'none';
      currentIndex = totalSlides - 1;
      sliderTrack.style.transform = `translateX(-${slideWidth * (currentIndex + itemsPerView)}%)`;
    }, 500);
  }
}

// Auto-slide every 2 seconds
let autoSlide = setInterval(showNextSlide, 3000);

// Button click events
nextBtn.addEventListener('click', () => {
  clearInterval(autoSlide); // Auto-slide to'xtaydi
  showNextSlide();
  autoSlide = setInterval(showNextSlide, 2000); // Keyin qayta boshlanadi
});

prevBtn.addEventListener('click', () => {
  clearInterval(autoSlide);
  showPrevSlide();
  autoSlide = setInterval(showNextSlide, 2000);
});


const regions = document.querySelectorAll('.region');


// *****************************************************************************************

document.addEventListener("DOMContentLoaded", () => {
// Select all regions and info boxes
const regions = document.querySelectorAll(".region");
const infoBoxes = document.querySelectorAll(".position-absolute");

// Function to hide all info boxes
const hideAllInfoBoxes = () => {
infoBoxes.forEach(box => box.classList.add("d-none"));
};

// Add click event to each region
regions.forEach(region => {
region.addEventListener("click", () => {
  // Hide all info boxes
  hideAllInfoBoxes();

  // Get the corresponding info box by data-name
  const regionName = region.getAttribute("data-name");
  const infoBox = document.getElementById(regionName);

  if (infoBox) {
    // Show the selected info box
    infoBox.classList.remove("d-none");
  }
});
});

// Optional: Deselect by clicking outside
document.addEventListener("click", (e) => {
if (!e.target.closest(".region") && !e.target.closest(".position-absolute")) {
  hideAllInfoBoxes();
}
});
});

