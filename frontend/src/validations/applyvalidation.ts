type ApplyErrors = {
    request?: string
    motivation?: string
}

// Motivation should be non-empty and at least 300 characters
function validateMotivation(motivation: string) {
    if (!motivation) {
        return 'Motivation est requise';
    }

    if (motivation.length < 3) {
        return 'Motivate doit être au moins 300 caractères';
    }

    return undefined;
}

export { validateMotivation };
export type { ApplyErrors };
