import { useCookies } from 'vue3-cookies'

// Wrapper around fetch to add required headers
export const fetcher = async (url: string, options: RequestInit = {}) => {
    const { cookies } = useCookies()
    const update = { ...options }
    if (cookies.get('token')) {
        update.headers = {
            ...update.headers,
            'Authorization': `Bearer ${cookies.get('token')}`
        }
    }

    return fetch(url, update)
}