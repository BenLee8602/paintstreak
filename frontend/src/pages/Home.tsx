import { useAuth } from "../auth/useAuth";

function Home() {
    const { user } = useAuth();

    return <p>{ user ? user : "no user" }</p>;
}

export default Home;

