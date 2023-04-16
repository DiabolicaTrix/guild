
// Le nom doit avoir au moi 3 caractères
function validateName(name: string) {
    if (!name) {
        return 'Nom est requis';
    }

    if (name.length < 3) {
        return 'Nom doit être plus long que 3 caractères';
    }

    return undefined;
}

// Le email doit être valide et non vide
function validateEmail(email: string) {
    if (!email) {
        return 'Email est requis';
    }

    if (!email.includes('@')) {
        return 'Email doit être valide';
    }

    return undefined;
}

// Les mots de passe doivent être identiques et répondre aux critères suivants:
// - Au moins 8 caractères
// - Au moins 1 chiffre
// - Au moins 1 lettre
// - Au moins 1 caractère spécial
function validatePassword(password: string, passwordConfirmation: string) {
    if (!password) {
        return 'Mot de passe est requis';
    }

    if (password.length < 8) {
        return 'Le mot de passe doit être plus long que 8 caractères';
    }

    if (!password.match(/\d/)) { // Au moins 1 chiffre
        return 'Le mot de passe doit contenir au moins 1 chiffre';
    }

    if (!password.match(/[a-zA-Z]/)) { // Au moins 1 lettre
        return 'Le mot de passe doit contenir au moins 1 lettre';
    }

    if (!password.match(/[^a-zA-Z0-9]/)) { // Au moins 1 caractère spécial
        return 'Le mot de passe doit contenir au moins 1 caractère spécial';
    }

    if (password !== passwordConfirmation) {
        return 'Les mots de passe doivent être identiques';
    }

    return undefined;
}


export { validateName, validateEmail, validatePassword }