import { Navigate, Outlet } from "react-router-dom";
import { useAuth } from "./useAuth";

function RequireNoLogin() {
    const { user } = useAuth();
    return user ? <Navigate to="/"/> : <Outlet/>;
}

export default RequireNoLogin;

