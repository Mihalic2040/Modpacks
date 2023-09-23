document.addEventListener("DOMContentLoaded", function () { 
    // Typing text animation script
    function typeText(element, texts) {
      let textIndex = 0;
      let charIndex = 0;
      let isDeleting = false;
  
      function type() {
        if (textIndex >= texts.length) {
          textIndex = 0;
        }
  
        const currentText = texts[textIndex];
        const typingSpeed = isDeleting ? 30 : 300;
  
        if (!isDeleting && charIndex < currentText.length) {
          element.textContent += currentText.charAt(charIndex);
          charIndex++;
        } else if (isDeleting && charIndex > 0) {
          element.textContent = currentText.substring(0, charIndex - 1);
          charIndex--;
        } else {
          isDeleting = !isDeleting;
          textIndex++;
        }
  
        setTimeout(type, typingSpeed);
      }
      type()
    }
  
    const typingElement = document.querySelector(".typing");
    typeText(typingElement, [
      "Mod developer",
      "Esthetic guru haha",
      "Cool guy",
      "Backend developer",
      "Open Source Contributor",
      // Add your other roles here
    ]);
  });