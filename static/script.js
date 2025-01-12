const form = document.querySelector("form");
const spinner = document.getElementById("loading-spinner");

form.addEventListener("submit", () => {
  spinner.classList.remove("hidden");
});

const fileInput = document.querySelector('input[name="file"]');
const previewImage = document.getElementById("image-preview");
const previewContainer = document.querySelector(".border-dashed");

fileInput.addEventListener("change", function (event) {
  const file = fileInput.files[0];
  if (file) {
    const reader = new FileReader();

    reader.onload = function (e) {
      previewImage.src = e.target.result; // Set the preview source
      previewImage.classList.remove("hidden"); // Unhide the image
      setTimeout(() => {
        previewImage.classList.remove("opacity-0", "scale-90");
        previewImage.classList.add("opacity-100", "scale-100");
      }, 100);

      // Highlight the preview container
      previewContainer.classList.add("ring", "ring-blue-500", "ring-offset-2");
    };

    reader.readAsDataURL(file);
  }
});

fileInput.addEventListener("input", function () {
  if (!fileInput.files.length) {
    previewImage.classList.add("opacity-0", "scale-90");
    setTimeout(() => {
      previewImage.classList.add("hidden");
      previewImage.src = ""; // Reset the source

      // Remove container highlight
      previewContainer.classList.remove(
        "ring",
        "ring-blue-500",
        "ring-offset-2"
      );
    }, 500);
  }
});

