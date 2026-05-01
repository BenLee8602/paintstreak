import { useAuth } from "../auth/useAuth";

function Home() {
    const { user, authFetch } = useAuth();

    const aaa = async () => {
        const res = await authFetch("/api/users/", {
            method: "PUT"
        });
        console.log(await res.json());
    };

    if (!user) return <>no user</>;
    return <>
        <p>{ user }</p>
        <button onClick={aaa}>aaa</button>
    </>;
}

export default Home;

