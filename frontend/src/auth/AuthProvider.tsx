import { useState, useEffect } from "react";
import { AuthContext } from "./AuthContext";
import auth from "./auth";

function AuthProvider({ children }) {
    const [user, setUser] = useState(null);

    useEffect(() => { (async () => {
        const token = localStorage.getItem("refreshToken");
        if (!token) return;
        const res = await auth.authFetch("/api/users/whoami", { method: "PUT" });
        if (res.status !== 200) return;
        const body = await res.json();
        setUser(body.username);
    })(); }, []);


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


    const value = {
        user,
        authFetch: auth.authFetch,
        register,
        login,
        logout
    };

    return <AuthContext value={value}>
        {children}
    </AuthContext>;
}

export default AuthProvider;

