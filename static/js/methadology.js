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
