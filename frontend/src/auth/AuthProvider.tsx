import { useState, useEffect } from "react";
import { AuthContext } from "./AuthContext";
import auth from "./auth";

function AuthProvider({ children }) {
    const [user, setUser] = useState(null);

    useEffect(() => {
        const token = localStorage.getItem("refreshToken");
        if (!token) return;
        const payload = JSON.parse(atob(token.split('.')[1]));
        setUser(payload.sub);
    }, []);


    const authFetch = (url: string, req: RequestInit) => {
        return user ? auth.authFetch(url, req) : fetch(url, req);
    };

    const register = async (name: string, pass: string) => {
        if (user) throw new Error("cant register while logged in");
        if (!(await auth.register(name, pass))) return false;
        setUser(name);
        return true;
    };

    const login = async (name: string, pass: string) => {
        if (user) throw new Error("cant login while logged in");
        if (!(await auth.login(name, pass))) return false;
        setUser(name);
        return true;
    };

    const logout = async () => {
        if (!user) throw new Error("cant logout while not logged in");
        await auth.logout()
        setUser(null);
    };


    const value = { user, authFetch, register, login, logout };

    return <AuthContext value={value}>
        {children}
    </AuthContext>;
}

export default AuthProvider;

