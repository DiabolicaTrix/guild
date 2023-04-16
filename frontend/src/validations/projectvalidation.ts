type ProjectErrors = {
    request?: string
    name?: string
    description?: string
}

// Name should have at least 3 characters and be non-empty
function validateName(name: string) {
    if (!name) {
        return 'Nom est requis';
    }

    if (name.length < 3) {
        return 'Nom doit être plus long que 3 caractères';
    }

    return undefined;
}

// Description should be non-empty and have at least 10 characters
function validateDescription(description: string) {
    if (!description) {
        return 'Description est requise';
    }

    if (description.length < 10) {
        return 'Description doit être plus longue que 10 caractères';
    }

    return undefined;
}

export { validateName, validateDescription };
export type { ProjectErrors };
