import { useCookies } from "vue3-cookies";

export default function auth(to, from) {
    console.log("Auth middleware")
    // Allow access to login and register pages
    if (to.path === '/login' || to.path === '/register') {
        return
    }

    const { cookies } = useCookies();
    const token = cookies.get('token');
    if (!token) {
        return '/login'
    }
}