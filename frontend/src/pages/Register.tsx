import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { useAuth } from "../auth/useAuth";

function Register() {
    const Navigate = useNavigate();
    const { register } = useAuth();

    const [curUser, setCurUser] = useState("");
    const [curPass, setCurPass] = useState("");
    const [curPassConf, setCurPassConf] = useState("");

    const handleRegister = async () => {
        if (!curUser || !curPass) return;
        if (curPass !== curPassConf) return;
        if (await register(curUser, curPass)) Navigate("/");
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
            <label>confirm password</label>
            <input
                type="password"
                onChange={e => setCurPassConf(e.target.value)}
            />
            <button onClick={handleRegister}>submit</button>
        </div>
    </div>;
}

export default Register;

