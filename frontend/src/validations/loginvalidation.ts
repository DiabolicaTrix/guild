// Le email doit être valide et non vide
function validateEmail(email: string) {
    if (!email) {
        return 'Email requis'
    }

    if (!email.includes('@')) {
        return 'Email invalide'
    }

    return undefined
}

// Le mot de passe doit être non vide
function validatePassword(password: string) {
    if (!password) {
        return 'Mot de passe requis'
    }
    return undefined
}

export { validateEmail, validatePassword }