// script.js

// The rules array is provided by rules.js

const passwordInput = document.getElementById('passwordInput');
const passwordLength = document.getElementById('passwordLength');
const ruleList = document.getElementById('ruleList');
const submitBtn = document.getElementById('submitBtn');
const message = document.getElementById('message');
const usernameInput = document.getElementById('usernameInput');

let visibleRuleCount = 0;
let ruleElements = new Map();

const updateRules = (password) => {
    let allVisibleRulesSatisfied = true;
    let newVisibleCount = 0;

    // Show at least one rule if the password is not empty
    if (password.length > 0) {
        newVisibleCount = 1;
    }

    // Determine how many subsequent rules should be visible
    let allPrecedingSatisfied = true;
    for (let i = 0; i < rules.length; i++) {
        if (allPrecedingSatisfied) {
            if (rules[i].check(password)) {
                newVisibleCount++;
            } else {
                allPrecedingSatisfied = false;
            }
        }
    }
    
    // Ensure the number of visible rules only increases
    visibleRuleCount = Math.max(visibleRuleCount, newVisibleCount);

    const unsatisfiedRules = [];
    const satisfiedRules = [];
    
    // Create or update all currently visible rules
    for (let i = 0; i < visibleRuleCount; i++) {
        const rule = rules[i];
        let ruleElement = ruleElements.get(rule.id);
        const isSatisfied = rule.check(password);

        if (!ruleElement) {
            ruleElement = document.createElement('li');
            ruleElement.classList.add('rule');
            ruleElements.set(rule.id, ruleElement);
        }
        
        const icon = isSatisfied ? '✔️' : '❌';
        ruleElement.innerHTML = `<span class="icon">${icon}</span> <span class="rule-text">${rule.text}</span>`;
        
        if (isSatisfied) {
            ruleElement.classList.remove('invalid');
            ruleElement.classList.add('valid');
            satisfiedRules.push({ element: ruleElement, index: i });
        } else {
            ruleElement.classList.remove('valid');
            ruleElement.classList.add('invalid');
            allVisibleRulesSatisfied = false;
            unsatisfiedRules.push({ element: ruleElement, index: i });
        }
        
        setTimeout(() => { ruleElement.classList.add('visible'); }, 50 * i);
    }
    
    satisfiedRules.sort((a, b) => b.index - a.index);
    
    const sortedRules = [...unsatisfiedRules.map(r => r.element), ...satisfiedRules.map(r => r.element)];
    ruleList.innerHTML = '';
    sortedRules.forEach(item => ruleList.appendChild(item));

    // Check for final submission condition
    if (allVisibleRulesSatisfied && visibleRuleCount === rules.length) {
        submitBtn.disabled = false;
    } else {
        submitBtn.disabled = true;
    }
};

if (passwordInput) {
    passwordInput.addEventListener('input', () => {
        if (passwordInput.value.length === 0) {
            ruleElements.forEach(el => el.classList.remove('visible'));
            visibleRuleCount = 0;
            passwordLength.innerText = '';
            submitBtn.disabled = true;
        } else {
            updateRules(passwordInput.value);
            passwordLength.innerText = passwordInput.value.length;
        }
    });
}


if (submitBtn) {
    submitBtn.addEventListener('click', async () => {
        const password = passwordInput.value;
        const satisfiedRules = [];
        
        let in_order = true;
        rules.forEach(rule => {
            if (in_order && rule.check(password)) {
                satisfiedRules.push(rule.id);
            }
            else {
                in_order = false;
            }
        });

        const data = {
            username: usernameInput.value,
            password: password,
            rules_satisfied: satisfiedRules
        };

        try {
            const response = await fetch('/register_attempt', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(data)
            });

            const result = await response.json();
            message.textContent = result.message;

            if (result.redirect_url) {
                window.location.href = result.redirect_url;
            }
        } catch (error) {
            message.textContent = 'An error occurred. Check the server.';
        }
    });
}
