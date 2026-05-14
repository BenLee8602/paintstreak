import { useState } from "react";
import { useAuth } from "../auth/useAuth";

function Home() {
    const { user, authFetch } = useAuth();

    const [name, setName] = useState("");

    const updateUser = async () => {
        let body = {};
        if (name) body["username"] = name;
        const res = await authFetch("/api/users", {
            method: "PUT",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(body)
        });
        console.log(res.status);
    };

    const deleteUser = async () => {
        const res = await authFetch("/api/users", { method: "DELETE" });
        console.log(res.status);
    };

    if (user === undefined) return <></>;
    if (user === null) return <p>no user</p>;
    return <>
        <p>{ user }</p>
        <input onChange={e => setName(e.target.value)}/>
        <button onClick={updateUser}>update</button>
        <button onClick={deleteUser}>delete</button>
    </>;
}

export default Home;

