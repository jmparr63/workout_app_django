document.addEventListener('DOMContentLoaded', function() {
    const cardioCheckbox = document.getElementById('{{ form.cardio.id_for_label }}');
    const cardioSection = document.getElementById('cardio-section');
    const addExerciseButton = document.getElementById('add-exercise');
    const resistanceExercises = document.getElementById('resistance-exercises');
    let exerciseCount = { form.resistance_exercises.total_form_count };

    cardioCheckbox.addEventListener('change', function() {
        cardioSection.style.display = this.checked ? 'block' : 'none';
    });

    addExerciseButton.addEventListener('click', function() {
        const newExercise = resistanceExercises.children[0].cloneNode(true);
        exerciseCount++;
        newExercise.querySelector('h3').textContent = `Exercise ${exerciseCount}`;
        updateFormIndex(newExercise, exerciseCount - 1);
        resistanceExercises.appendChild(newExercise);
        updateManagementForm();
    });

    function updateFormIndex(element, index) {
        const inputs = element.querySelectorAll('input, select, textarea');
        inputs.forEach(input => {
            input.name = input.name.replace(/\d+/, index);
            input.id = input.id.replace(/\d+/, index);
        });
    }

    function updateManagementForm() {
        const totalForms = document.getElementById('id_resistance_exercises-TOTAL_FORMS');
        totalForms.value = exerciseCount;
    }
});