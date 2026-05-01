import { BrowserRouter, Routes, Route } from "react-router-dom";
import AuthProvider from "./auth/AuthProvider.tsx";
import RequireNoLogin from "./auth/RequireNoLogin.tsx";
import Home from "./pages/Home";
import NotFound from "./pages/NotFound";
import Login from "./pages/Login";
import Register from "./pages/Register";
import Navbar from "./components/Navbar";

function App() {
    return <AuthProvider>
        <BrowserRouter>
            <Navbar/>
            <main className="main-content">
                <Routes>
                    <Route path="/" element={<Home/>}/>
                    <Route element={<RequireNoLogin/>}>
                        <Route path="/register" element={<Register/>}/>
                        <Route path="/login" element={<Login/>}/>
                    </Route>
                    <Route path="*" element={<NotFound/>}/>
                </Routes>
            </main>
        </BrowserRouter>
    </AuthProvider>;
}

export default App
