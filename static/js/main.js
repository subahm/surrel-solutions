
// Mobile nav toggle
const toggle = document.querySelector('.nav-toggle');
const nav = document.getElementById('site-nav');
if (toggle && nav){
  toggle.addEventListener('click', () => {
    const open = nav.classList.toggle('open');
    toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
  });
}

// Basic client-side validation for contact form
const form = document.querySelector('.contact-form');
if (form){
  form.addEventListener('submit', (e) => {
    const name = form.querySelector('#name');
    const email = form.querySelector('#email');
    const message = form.querySelector('#message');
    let ok = true;
    [name,email,message].forEach(input => {
      if (!input.value.trim()){
        input.setAttribute('aria-invalid','true');
        ok = false;
      } else {
        input.removeAttribute('aria-invalid');
      }
    });
    if (!ok){
      e.preventDefault();
      alert('Please fill in your name, email, and message.');
    }
  });
}

// Letter-by-letter flip animation Surrel <-> Simple
document.addEventListener("DOMContentLoaded", () => {
  const flipWord = document.getElementById("flipWord");
  const words = ["Surrel", "Simple"];
  let currentIndex = 0;

  // Render initial word
  function renderWord(word) {
    flipWord.innerHTML = "";
    word.split("").forEach(letter => {
      const span = document.createElement("span");
      span.className = "flip-letter";
      span.textContent = letter;
      flipWord.appendChild(span);
    });
  }

  renderWord(words[currentIndex]);

  setInterval(() => {
    const nextIndex = (currentIndex + 1) % words.length;
    const currentSpans = flipWord.querySelectorAll(".flip-letter");
    const nextWord = words[nextIndex].split("");

    // Ensure equal length arrays (pad with empty letters)
    const maxLen = Math.max(currentSpans.length, nextWord.length);

    for (let i = 0; i < maxLen; i++) {
      const currentSpan = currentSpans[i];

      if (!currentSpan) {
        // Add missing letter for longer word
        const span = document.createElement("span");
        span.className = "flip-letter";
        span.textContent = "";
        flipWord.appendChild(span);
      }
    }

    const spans = flipWord.querySelectorAll(".flip-letter");

    spans.forEach((span, i) => {
      setTimeout(() => {
        span.classList.add("flip");
        setTimeout(() => {
          span.textContent = nextWord[i] || "";
          span.classList.remove("flip");
        }, 300); // mid-flip
      }, i * 100); // stagger letters
    });

    currentIndex = nextIndex;
  }, 2000); // every 2s (slightly longer for readability)
});

//methodology section
document.addEventListener('DOMContentLoaded', function() {
    const svgElements = [
        { id: 'planning-partition', textId: 'text-planning' },
        { id: 'design-partition', textId: 'text-designing' },
        { id: 'svg_14', textId: 'text-implementation' },
        { id: 'deployment-partition', textId: 'text-deployment' },
        { id: 'testing-partition', textId: 'text-testing' },
        { id: 'req-gathering-partition', textId: 'text-req-gathering' },
        { id: 'maintenance-partition', textId: 'text-maintenance' }
    ];

    const svgContainer = document.getElementById('svgContainer');
    let currentVisibleElement = null; // Track currently visible description

    if (svgContainer) {
        svgElements.forEach(({ id, textId }) => {
            const element = document.getElementById(id);
            const textElement = document.getElementById(textId);

            if (element && textElement) {
                element.addEventListener('click', function(event) {
                    event.stopPropagation();

                    // Toggle the active state
                    if (element.classList.contains('active')) {
                        element.classList.remove('active');
                    } else {
                        // Remove active class from any other element
                        svgElements.forEach(({ id }) => {
                            document.getElementById(id).classList.remove('active');
                        });
                        element.classList.add('active');
                    }

                    // Only move the SVG container if it's not already moved
                    if (!svgContainer.classList.contains('moved')) {
                        svgContainer.classList.add('moved');
                    }

                    // Hide the currently visible description, if any
                    if (currentVisibleElement && currentVisibleElement !== textElement) {
                        currentVisibleElement.classList.remove('visible');
                    }

                    // Show the clicked description
                    textElement.classList.add('visible');
                    currentVisibleElement = textElement;
                });
            } else {
                console.error(`Element with ID ${id} or ${textId} not found.`);
            }
        });

        document.addEventListener('click', function(event) {
            const clickedInside = svgElements.some(({ id }) =>
                document.getElementById(id).contains(event.target)
            );

            if (!clickedInside) {
                svgContainer.classList.remove('moved');

                // Remove the active class from all elements
                svgElements.forEach(({ id }) => {
                    document.getElementById(id).classList.remove('active');
                });

                if (currentVisibleElement) {
                    currentVisibleElement.classList.remove('visible');
                    currentVisibleElement = null; // Reset the current visible element
                }
            }
        });
    } else {
        console.error('Element with ID svgContainer not found.');
    }
});
