// Variables globales
let verbsData = [];
const modal = document.getElementById('verb-modal');
const modalBody = document.getElementById('modal-body');
const closeBtn = document.querySelector('.close-btn');

// Cargar verbos desde JSON
async function loadVerbs() {
    try {
        const response = await fetch('verbs.json');
        const data = await response.json();
        verbsData = data.verbs;
        
        // Ordenar alfabéticamente
        verbsData.sort((a, b) => a.infinitive.localeCompare(b.infinitive));
        
        // Renderizar botones
        renderVerbButtons();
    } catch (error) {
        console.error('Error cargando los verbos:', error);
        document.getElementById('verbs-container').innerHTML = 
            '<p style="color: red; text-align: center;">Error cargando los verbos. Verifica el archivo verbs.json</p>';
    }
}

// Renderizar botones de verbos
function renderVerbButtons() {
    const container = document.getElementById('verbs-container');
    container.innerHTML = '';
    
    verbsData.forEach((verb, index) => {
        const btn = document.createElement('div');
        btn.className = 'verb-btn';
        btn.innerHTML = `
            <h3>${verb.infinitive}</h3>
            <p>${verb.translation}</p>
        `;
        btn.addEventListener('click', () => openModal(verb));
        container.appendChild(btn);
    });
}

// Abrir modal con conjugaciones
function openModal(verb) {
    modalBody.innerHTML = `
        <div class="modal-header">
            <h2>${verb.infinitive}</h2>
            <p class="translation">${verb.translation}</p>
        </div>
        <div class="modal-body">
            ${generateTenseSection('Presente Simple', verb.presentSimple)}
            ${generateTenseSection('Pasado Simple', verb.pastSimple)}
            ${generateTenseSection('Presente Perfecto', verb.presentPerfect)}
            ${generateTenseSection('Pasado Perfecto', verb.pastPerfect)}
            ${verb.modals ? generateModalsSection(verb.modals) : ''}
        </div>
    `;
    modal.classList.add('active');
    document.body.style.overflow = 'hidden';
}

// Generar sección de tiempo verbal
function generateTenseSection(tenseName, conjugations) {
    const persons = {
        'I': 'I (yo)',
        'you': 'You (tú)',
        'he/she/it': 'He/She/It (él/ella)',
        'we': 'We (nosotros)',
        'you_plural': 'You (ustedes)',
        'they': 'They (ellos/ellas)'
    };
    
    let html = `
        <div class="tense-section">
            <div class="tense-header">${tenseName}</div>
            <div class="tense-content">
                <table class="conjugation-table">
    `;
    
    for (const [person, data] of Object.entries(conjugations)) {
        html += `
            <tr>
                <td>${persons[person]}</td>
                <td>${data.form}</td>
                <td>${data.translation}</td>
            </tr>
        `;
    }
    
    html += `
                </table>
            </div>
        </div>
    `;
    
    return html;
}

// Cerrar modal
function closeModal() {
    modal.classList.remove('active');
    document.body.style.overflow = 'auto';
}

// Event listeners
closeBtn.addEventListener('click', closeModal);

modal.addEventListener('click', (e) => {
    if (e.target === modal) {
        closeModal();
    }
});

// Cerrar con tecla ESC
document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && modal.classList.contains('active')) {
        closeModal();
    }
});

// Inicializar
document.addEventListener('DOMContentLoaded', loadVerbs);


function generateModalsSection(modals) {
    let html = `
        <div class="tense-section">
            <div class="tense-header">✨ Verbos Modales</div>
            <div class="tense-content">
    `;
    
    const modalNames = {
        "can": "Can (poder - habilidad)",
        "cannot": "Can't (no poder)",
        "could": "Could (podría - condicional)",
        "couldn't": "Couldn't (no podría)",
        "should": "Should (debería - consejo)",
        "shouldn't": "Shouldn't (no debería)",
        "must": "Must (deber - obligación)",
        "must_not": "Must not (no deber - prohibición)",
        "might": "Might (podría - posibilidad)",
        "might_not": "Might not (podría no)",
        "could_have": "Could have (podría haber)",
        "should_have": "Should have (debería haber)",
        "must_have": "Must have (debe haber)",
        "might_have": "Might have (podría haber)"
    };
    
    for (const [key, modal] of Object.entries(modals)) {
        html += `
            <div style="margin-bottom: 1rem; padding: 0.75rem; background: #f8f9fa; border-radius: 8px;">
                <strong style="color: var(--primary-color);">${modalNames[key] || key}:</strong><br>
                <span style="font-weight: 500;">${modal.form}</span><br>
                <span style="color: #7f8c8d; font-style: italic;">${modal.translation}</span><br>
                <small style="color: var(--accent-color);">💡 ${modal.note}</small>
            </div>
        `;
    }
    
    html += `</div></div>`;
    return html;
}