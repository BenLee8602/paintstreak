import { BACKEND_URL } from "../config";


async function authFetch(url: string, req: RequestInit) {
    let token: string = localStorage.getItem("accessToken");
    if (token) {
        const payload = JSON.parse(atob(token.split('.')[1]));
        const now = Date.now() / 1000;
        if (payload.exp - 60 < now) token = null;
    }
    
    if (!token) {
        const res = await fetch(`${BACKEND_URL}/api/users/refresh`, {
            method: "PUT",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ token: localStorage.getItem("refreshToken") })
        });
        token = await res.json();
        localStorage.setItem("accessToken", token);
    }

    return fetch(`${BACKEND_URL}${url}`, {
        ...req,
        headers: {
            ...req.headers,
            Authorization: `Bearer ${token}`
        }
    });
}


async function register(user: string, pass: string) {
    const res = await fetch(`${BACKEND_URL}/api/users/register`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username: user, password: pass })
    });
    if (res.status !== 200) return false;
    localStorage.setItem("refreshToken", await res.json());
    return true;
}

async function login(user: string, pass: string): boolean {
    const res = await fetch(`${BACKEND_URL}/api/users/login`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username: user, password: pass })
    });
    if (res.status !== 200) return false;
    localStorage.setItem("refreshToken", await res.json());
    return true;
}

async function logout(): void {
    await fetch(`${BACKEND_URL}/api/users/logout`, {
        method: "DELETE",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ token: localStorage.getItem("refreshToken") })
    });
    localStorage.removeItem("refreshToken");
    localStorage.removeItem("accessToken");
}


export default {
    authFetch,
    register,
    login,
    logout
};

