import { useCookies } from 'vue3-cookies'
import jwt_decode from 'jwt-decode'

function extractUserFromSession() {
    const { cookies } = useCookies()
    const token = cookies.get('token')
    if (!token) {
        return null
    }

    const decoded = jwt_decode(token)

    return {
        user: decoded,
    };
}

export { extractUserFromSession }