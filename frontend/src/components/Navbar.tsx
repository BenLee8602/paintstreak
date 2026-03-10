import { Link } from "react-router-dom";
import "../styles/navbar.css"; 

function Navbar() {
    return <nav className="navbar">
        <div className="main-content">
            <Link to="/" className="title">PaintStreak</Link>
            <ul className="left">
                <li><Link to="/">Home</Link></li>
            </ul>
            <ul className="right">
                <li><Link to="/login">Login</Link></li>
                <li><Link to="/register">Register</Link></li>
            </ul>
        </div>
    </nav>;
}

export default Navbar;

