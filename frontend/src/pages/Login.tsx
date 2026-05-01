import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { useAuth } from "../auth/useAuth";

function Login() {
    const Navigate = useNavigate();
    const { login } = useAuth();

    const [curUser, setCurUser] = useState("");
    const [curPass, setCurPass] = useState("");

    const handleLogin = async () => {
        if (!curUser || !curPass) return;
        if (await login(curUser, curPass)) Navigate("/");
    };

    return <div className="form-wrapper">
        <div className="form">
            <label>username</label>
            <input
                type="text"
                onChange={e => setCurUser(e.target.value)}
            />
            <label>password</label>
            <input
                type="password"
                onChange={e => setCurPass(e.target.value)}
            />
            <button onClick={handleLogin}>submit</button>
        </div>
    </div>;
}

export default Login;

